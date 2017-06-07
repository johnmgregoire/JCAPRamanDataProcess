import sys,os, pickle, numpy, pylab, operator, itertools
import cv2
from shutil import copy as copyfile
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import matplotlib.pyplot as plt
from DataParseApp import dataparseDialog
from sklearn.decomposition import NMF

projectpath=os.path.split(os.path.abspath(__file__))[0]
sys.path.append(os.path.join(projectpath,'ui'))

pythoncodepath=os.path.split(projectpath)[0]
jcapdataprocesspath=os.path.join(pythoncodepath, 'JCAPDataProcess')
sys.path.append(jcapdataprocesspath)
from VisualizeDataApp import visdataDialog

sys.path.append(os.path.join(jcapdataprocesspath,'AuxPrograms'))
from fcns_ui import *
from fcns_io import *

platemapvisprocesspath=os.path.join(pythoncodepath, 'JCAPPlatemapVisualize')
sys.path.append(platemapvisprocesspath)
from plate_image_align_Dialog import plateimagealignDialog

import numpy as np

###############UPDATE THIS TO BE THE FOLDER CONTAINING parameters.py
paramsfolder=r'K:\users\hte\Raman\39664\20170607analysis'

if not paramsfolder is None:
    sys.path.append(paramsfolder)
    from parameters import *
else:
    plateidstr='3344'

    pathd={'ramanfile':r'K:\users\hte\Raman\33444\HSS_33444_map-1-_CRR-EM-copy.txt'}
    pathd['mainfolder']=os.path.split(pathd['ramanfile'])[0]
    pathd['savefolder']=os.path.join(pathd['mainfolder'], '20170607analysis')
    pathd['infopck']=pathd['ramanfile'][:-4]+'__info.pck'
    pathd['allspectra']=os.path.join(pathd['savefolder'],'allspectra.npy')
    pathd['nmfdata']=os.path.join(pathd['savefolder'],'nmf4.pck')
    pathd['edges']=os.path.join(pathd['savefolder'],'edges.png')
    pathd['mapfill']=os.path.join(pathd['savefolder'],'blobmap.png')
    pathd['blobd']=os.path.join(pathd['savefolder'],'blobd.pck')
    pathd['alignedsamples']=os.path.join(pathd['savefolder'],'alignedsamples.png')
    pathd['alignedsamplestxt']=os.path.join(pathd['savefolder'],'alignedsamples.txt')
    pathd['spectrafolder']=os.path.join(pathd['savefolder'],'sample_spectra')
    pathd['map']=os.path.join(pathd['spectrafolder'],'raman_sample_index_map.map')
    pathd['samplepixels']=os.path.join(pathd['spectrafolder'],'samplepixels.png')
    pathd['udibasepath']=os.path.join(pathd['savefolder'],'ave_rmn_')

    udi_ternary_projection_inds=[0, 1, 2]#only used for the all.udi file

    sample_list=[1850,1851,1852,1853,1854,1855,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917,1918,1919,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,2033,2034,2035,2036,2037,2038,2039,2040,2041,2042,2043,2044,2045,2046,2047,2097,2098,2099,2100,2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111]
    dx_smp=1.
    dy_smp=1.

    default_sample_blob_dict=dict({}, \
    smp_is_square=0, smp_width=1., bcknd_is_square=0,  bcknd_min_width=1.3, bcknd_max_width=1.4, removedups=1\
    )

    show_help_messages=True




platemappath=getplatemappath_plateid(plateidstr)

if not os.path.isdir(pathd['mainfolder']):
    print 'NOT A VALID FOLDER'
if not os.path.isdir(pathd['savefolder']):
    os.mkdir(pathd['savefolder'])
if not os.path.isdir(pathd['spectrafolder']):
    os.mkdir(pathd['spectrafolder'])
    
class MainMenu(QMainWindow):
    def __init__(self, previousmm, execute=True, **kwargs):
        super(MainMenu, self).__init__(None)
        self.parseui=dataparseDialog(self, title='Visualize ANA, EXP, RUN data', **kwargs)
        self.alignui=plateimagealignDialog(self, manual_image_init_bool=False)
        if execute:
            self.parseui.exec_()

n_components=4
def doNMF(datan,n_components=4):
    # from Mitsu
    #alternatively PCA ... might me faster
    nmf=NMF(n_components=n_components,init='nndsvd')
    data_decomp_all=nmf.fit_transform(datan)
    data_components_all=nmf.components_
    return data_decomp_all,data_components_all

def rgb_comp(arr2d, affine=True):
    cmy_cmyk=lambda a:a[:3]*(1.-a[3])+a[3]
    rgb_cmy=lambda a:1.-a
    rgb_cmyk=lambda a:rgb_cmy(cmy_cmyk(a))


    return numpy.array([rgb_cmyk(a) for a in arr2d])
        
def imGen(data_decomp_all,ramaninfod,cmykindeces=[3, 2, 1, 0]):
    cmykvals=copy.copy(data_decomp_all[:, cmykindeces])
    cmykvals/=cmykvals.max(axis=0)[numpy.newaxis, :]
    img=numpy.reshape(rgb_comp(cmykvals), (ramaninfod['xshape'], ramaninfod['yshape'], 3))
    return img

def findEdges(img_gray):
    #this uses automatic thresholding from one of the cv2 tutorials
    sigma = 0.33
    v = np.median(img_gray)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edges = cv2.Canny(np.uint8(img_gray),lower,upper)
    return edges

def findContours(edges):
    #the contours are now found by searching the most external convex hull
    #this way mos of the not fully closed samples are detected as well
    im2, contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
    iWithContour = cv2.drawContours(edges, contours, -1, (255,20,100), 5)
    mapimage = np.zeros_like(edges)
    #this fills the contours
    for i in range(len(contours)):
        cv2.drawContours(mapimage, contours, i, color=255, thickness=-1)
    #this is to calculate the center of each contour
    x=[]
    y=[]
    for c in contours:
        # compute the center of the contour
        M = cv2.moments(c)
        try:
            x.append(M['m10']/(M['m00']))
            y.append(M['m01']/(M['m00']))
        except:
            #this was nessesary as the divisor is sometimes 0
            #yield good results but should be done with caution
            x.append(M['m10']/(M['m00']+1e-23))
            y.append(M['m01']/(M['m00']+1e-23))
    return iWithContour, mapimage, contours, x, y
    


mainapp=QApplication(sys.argv)
form=MainMenu(None, execute=False)
#form.show()
#form.setFocus()
#mainapp.exec_()

parseui=form.parseui
alignui=form.alignui
parseui.rawpathLineEdit.setText(pathd['ramanfile'])
parseui.infopathLineEdit.setText(pathd['infopck'])
parseui.getinfo(ramaninfop=pathd['infopck'], ramanfp=pathd['ramanfile'])#opens or creates

if os.path.isfile(pathd['allspectra']):
    with open(pathd['allspectra'], mode='rb') as f:
        fullramandataarray=numpy.load(f)
elif 0:
    fullramandataarray=parseui.readfullramanarray(pathd['ramanfile'])#opens or creates
    with open(pathd['allspectra'], mode='wb') as f:
        numpy.save(f, fullramandataarray)
    
ramaninfod=parseui.ramaninfod
#ramaninfod['number of spectra']
#ramaninfod['xdata']
#ramaninfod['ydata']
#ramaninfod['Wavenumbers_str']
#ramaninfod['Spectrum 0 index']
ramaninfod['xdata']/=1000.
ramaninfod['ydata']/=1000.#convert to mm
ramaninfod['xshape']= len(np.unique(ramaninfod['xdata']))
ramaninfod['yshape']= len(np.unique(ramaninfod['ydata']))

ramaninfod['dx']= (ramaninfod['xdata'].max()-ramaninfod['xdata'].min())/(ramaninfod['xshape']-1)
ramaninfod['dy']= (ramaninfod['ydata'].max()-ramaninfod['ydata'].min())/(ramaninfod['yshape']-1)

nx=dx_smp/ramaninfod['dx']
ny=dy_smp/ramaninfod['dy']
ntot=nx*ny

ramanreshape=lambda arr: np.reshape(arr, (ramaninfod['xshape'], ramaninfod['yshape'])).T[::-1, ::-1]

ramannewshape=(ramaninfod['yshape'], ramaninfod['xshape'])

image_of_x=ramanreshape(ramaninfod['xdata'])
image_of_y=ramanreshape(ramaninfod['ydata'])
    
    
#extent=[ramaninfod['xdata'].max(), ramaninfod['xdata'].min(), ramaninfod['ydata'].min(), ramaninfod['ydata'].max()]
#extent=[ramaninfod['xdata'].max(), ramaninfod['xdata'].min(), ramaninfod['ydata'].max(), ramaninfod['ydata'].min()]
extent=[image_of_x[0, 0], image_of_x[-1, -1], image_of_y[0, 0], image_of_y[-1, -1]]

def ramanimshow(im, **kwargs):
    plt.imshow(im, origin='lower', interpolation='none', aspect=1, extent=extent, **kwargs)

if os.path.isfile(pathd['nmfdata']):
    with open(pathd['nmfdata'], mode='rb') as f:
        tempd=pickle.load(f)
    data_decomp_all,data_components_all,rgbimagedata=[tempd[k] for k in 'data_decomp_all,data_components_all,rgbimagedata'.split(',')]
elif 1:
    with open(os.path.join(pathd['savefolder'],'data_decomp_all_protocol2.pck'), mode='rb') as f:
        data_decomp_all=pickle.load(f)
    with open(os.path.join(pathd['savefolder'],'data_components_all_protocol2.pck'), mode='rb') as f:
        data_components_all=pickle.load(f)
    #rgbimagedata=imGen(data_decomp_all,ramaninfod)
    rgbimagedata=np.zeros(ramannewshape+(3,), dtype='float32')
    for i, arr in enumerate(data_decomp_all[:, :3].T):
        rgbimagedata[:, :, i]=np.array([ramanreshape(arr/arr.max())])
else:
    data_decomp_all,data_components_all = doNMF(datan,4)
    #rgbimagedata=imGen(data_decomp_all,ramaninfod)
    rgbimagedata=np.zeros(ramannewshape+(3,), dtype='float32')
    for i, arr in enumerate(data_decomp_all[:, :3].T):
        rgbimagedata[:, :, i]=np.array([ramanreshape(arr/arr.max())])
    tempd=dict(zip('data_decomp_all,data_components_all,rgbimagedata'.split(','), data_decomp_all,data_components_all,rgbimagedata))
    with open(pathd['nmfdata'], mode='wb') as f:
        tempd=pickle.dump(tempd, f)



if 1 and os.path.isfile(pathd['blobd']):
    with open(pathd['blobd'], mode='rb') as f:
        blobd=pickle.load(f)
else:
    edges = np.zeros(ramannewshape, dtype='uint8')
    plt.clf()
    for i in range(n_components):
        arr=np.uint8(ramanreshape(data_decomp_all[:,i])/data_decomp_all[:,i].max()*254)
        edgetemp=findEdges(arr)
    #    plt.imshow(edgetemp)
    #    plt.show()
        edges[np.where(edgetemp>0)] = 244

    ramanimshow(edges)
    plt.savefig(pathd['edges'])
    plt.clf()

    im2, contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)

    image_of_inds=ramanreshape(numpy.arange(ramaninfod['number of spectra']))
    

    mapfill = np.zeros(ramannewshape, dtype='uint8')
    blobd={}
    l_mask=[cv2.drawContours(np.zeros(ramannewshape, dtype='uint8'), contours, i, color=1, thickness=-1) for i in range(len(contours))]
    l_imageinds=[numpy.where(mask==1) for mask in l_mask]
    l_xycen=np.array([[image_of_x[imageinds].mean(), image_of_y[imageinds].mean()] for imageinds in l_imageinds])

    indstomerge=sorted([(count2+count+1, count) for count, xy0 in enumerate(l_xycen) for count2, xy1 in enumerate(l_xycen[count+1:]) if ((xy0-xy1)**2).sum()<(dx_smp**2+dy_smp**2)/10.])[::-1]
    #indstomerge has highest index first so merge going down 
    for indhigh, indlow in indstomerge:
        imageinds=l_imageinds.pop(indhigh)
        mask=l_mask.pop(indhigh)
        l_mask[indlow][imageinds]=1#update only the masks and then update everythign else afterwards

    l_imageinds=[numpy.where(mask==1) for mask in l_mask]
    l_xycen=np.array([[image_of_x[imageinds].mean(), image_of_y[imageinds].mean()] for imageinds in l_imageinds])

    for imageinds, mask in zip(l_imageinds, l_mask):
        indsinblob=sorted(list(image_of_inds[imageinds]))
        relx=(image_of_x[imageinds].max()-image_of_x[imageinds].min())/dx_smp
        rely=(image_of_y[imageinds].max()-image_of_y[imageinds].min())/dy_smp

        if relx<0.5 or relx>1.4 or rely<0.5 or rely>1.4 or len(indsinblob)<ntot*0.5 or  len(indsinblob)>ntot*1.5:
            print 'skipped blob that was %.2f, %.2f of expected size with %d pixels' %(relx, rely, len(indsinblob))
            continue
        if numpy.any(mapfill[imageinds]==1):
            print 'overlapping blobs detected'
        

        xc=image_of_x[imageinds].mean()
        yc=image_of_y[imageinds].mean()
        mapfill[imageinds]=1
        blobd[(xc, yc)]=indsinblob
    plt.clf()
    ramanimshow(mapfill)
    plt.savefig(pathd['mapfill'])
    if show_help_messages:
        messageDialog(form, 'The auto detected and cleaned up blobs will be shown.\nThis is an image using the Raman motor coordinates').exec_()
    plt.show()
    
    with open(pathd['blobd'], mode='wb') as f:
        pickle.dump(blobd, f)


alignui.knownblobsdict=blobd
alignui.openAddFile(p=platemappath)
alignui.image=rgbimagedata
alignui.motimage_extent=extent #left,right,bottom,top in mm
alignui.reloadimagewithextent()
#alignui.plotw_motimage.axes.imshow(alignui.image, origin='lower', interpolation='none', aspect=1, extent=alignui.motimage_extent)

xarr, yarr=np.array(blobd.keys()).T
alignui.plotw_motimage.axes.plot(xarr, yarr, 'wx', ms=4)
alignui.plotw_motimage.fig.canvas.draw()

if show_help_messages:
    messageDialog(form, 'NMF analysis done and now plotting NMF image\nwith identified samples marked +. User can choose sample_no and \nright click to add calibration points.\nDo this for at least 1 sample marked with +.').exec_()
alignui.exec_()

alignui.sampleLineEdit.setText(','.join(['%d' %smp for smp in sample_list]))
alignui.addValuesSample()

if show_help_messages:
    messageDialog(form, 'sample_no for export have been added. Check that \nthere are no NaN and if there are manually add calibration points\nas necessary and then remove+re-add the NaN samples.').exec_()

alignui.exec_()

alignui.plotw_motimage.fig.savefig(pathd['alignedsamples'])
with open(pathd['alignedsamplestxt'], mode='w') as f:
    f.write(str(alignui.browser.toPlainText()))
alignui.openpckinfo(p=pathd['infopck'])
alignui.infox/=1000.
alignui.infoy/=1000.
alignui.perform_genmapfile(p=pathd['map'], **default_sample_blob_dict)


mapfill2=np.zeros(ramaninfod['number of spectra'], dtype='uint8')
for smp, inds in alignui.smp_inds_list__map:
    mapfill2[inds]=2 if smp>0 else 1
mapfill2=ramanreshape(mapfill2)
plt.clf()
ramanimshow(mapfill2, vmin=0, vmax=2, cmap='gnuplot')
plt.savefig(pathd['samplepixels'])

if show_help_messages:
    messageDialog(form, 'The NMF-identified samples use custom blob shapes and\nthe rest of the requested samples use default sample shape, resulting\nin the following map of pixels that will be exported.').exec_()
    
plt.show()
    


parseui.savepathLineEdit.setText(pathd['spectrafolder'])
parseui.match(copypath=pathd['map'])
parseui.extract()
parseui.saveave()
#parseui.readresultsfolder()

if show_help_messages:
    messageDialog(form, 'The .rmn files have now been saved, so you can use\nthis next dialog to visualize data or close it to generate\nthe .udi files and open in JCAPDataProcess Visualizer').exec_()
parseui.exec_()

#only initialize visdataDialog so only created when necessary

visui=visdataDialog(form, title='Visualize ANA, EXP, RUN data')
            
visui.openontheflyfolder(folderpath=pathd['spectrafolder'], plateidstr=plateidstr)
visui.BatchComboBox.setCurrentIndex(2)
visui.runbatchprocess()
savep=pathd['udibasepath']+'all.udi'
visui.get_xy_plate_info_browsersamples(saveudibool=True, ternary_el_inds_for_udi_export=udi_ternary_projection_inds, savep=savep)
for i, indstup in enumerate(itertools.combinations(range(len(visui.ellabels)), 3)):
    excludeinds=[ind for ind in range(len(visui.ellabels)) if not ind in indstup]
    inds_where_excluded_els_all_zero=numpy.where(visui.fomplotd['comps'][:, excludeinds].max(axis=1)==0)[0]
    if len(inds_where_excluded_els_all_zero)==0:
        continue
    smplist=[visui.fomplotd['sample_no'][fomplotind] for fomplotind in inds_where_excluded_els_all_zero]
    visui.remallsamples()
    visui.addrem_select_fomplotdinds(remove=False, smplist=smplist)
    savep=''.join([pathd['udibasepath']]+[visui.ellabels[ind] for ind in indstup]+['.udi'])
    visui.get_xy_plate_info_browsersamples(saveudibool=True, ternary_el_inds_for_udi_export=indstup, savep=savep)

if show_help_messages:
    messageDialog(form, 'udi files now saved and JCAPDataProcess\nVisualizer will be opened for your use.').exec_()
visui.exec_()

if show_help_messages:
    messageDialog(form, 'There is nothing more to do and continuing will raise an error.').exec_()
errorattheend
