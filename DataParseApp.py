import sys,os, pickle, numpy, pylab, operator
from shutil import copy as copyfile
from PyQt4.QtCore import *
from PyQt4.QtGui import *
projectpath=os.path.split(os.path.abspath(__file__))[0]
sys.path.append(os.path.join(projectpath,'ui'))

pythoncodepath=os.path.split(projectpath)[0]
jcapdataprocesspath=os.path.join(pythoncodepath, 'JCAPDataProcess')
sys.path.append(os.path.join(jcapdataprocesspath,'AuxPrograms'))
from fcns_ui import *
from fcns_io import *
from fcns_compplots import plotwidget
from DataParseDialog import Ui_DataParseDialog



class dataparseDialog(QDialog, Ui_DataParseDialog):
    def __init__(self, parent=None, title='', folderpath=None):
        super(dataparseDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.parent=parent
        
        button_fcn=[\
        (self.rawpathPushButton, self.selectrawpath), \
        (self.infopathPushButton, self.selectinfopath), \
        (self.infopathnewPushButton, self.selectinfopathnew), \
        (self.savepathPushButton, self.selectsavefolder), \
        (self.getinfoPushButton, self.getinfo), \
        (self.matchPushButton, self.match), \
        (self.copymatchPushButton, self.copymatch), \
        (self.extractPushButton, self.extract), \
        (self.readfolderPushButton, self.readresultsfolder), \
        (self.avePushButton, self.saveave), \

        ]
        QObject.connect(self.sampleComboBox,SIGNAL("activated(QString)"), self.plot)
        #(self.UndoExpPushButton, self.undoexpfile), \
        for button, fcn in button_fcn:
            QObject.connect(button, SIGNAL("pressed()"), fcn)
        self.ramaninfod={}
        self.processclass=processspectrafile()
        self.processclass_ave=processspectrafile()
        self.plotwsetup()
        
    def selectrawpath(self, markstr='Renishaw .txt file from file converter'):
        le=self.rawpathLineEdit
        self.selectfile(le=le, markstr=markstr, new=False)
    def selectinfopath(self, markstr='File for saving Raman metadata'):
        le=self.infopathLineEdit
        self.selectfile(le=le, markstr=markstr, new=False)
    def selectinfopathnew(self, markstr='File for saving Raman metadata'):
        le=self.infopathLineEdit
        self.selectfile(le=le, markstr=markstr, new=True)
    def selectfile(self, le=None, markstr='select file', new=False, xpath=None):
        if xpath is None:
            xpath=str(le.text()) if not le is None else ''
        if new:
            p=mygetsavefile(parent=self, xpath=xpath, markstr=markstr)
        else:
            p=mygetopenfile(parent=self, xpath=xpath, markstr=markstr)
        if not le is None and len(p)>0:
            le.setText(p)
        return p
    def selectsavefolder(self, markstr='folder for saving map file and extracted spectra'):
        le=self.savepathLineEdit
        folderpath=mygetdir(self, markstr=markstr)
        if len(folderpath)>0:
            le.setText(folderpath)
        return folderpath
        
    def getinfo(self):
        ramaninfop=str(self.infopathLineEdit.text())
        if os.path.isfile(ramaninfop):
            with open(ramaninfop, mode='r') as f:
                self.ramaninfod=pickle.load(f)
                self.updateinfobrowser()
            return
        
        ramanfp=str(self.rawpathLineEdit.text())
        tryagain=not os.path.isfile(ramanfp)
        while tryagain:
            self.selectrawpath()
            tryagain=messageDialog(self, 'Renishaw file does not exist. Try again?').exec_()
            if tryagain:
                self.selectrawpath()
                ramanfp=str(self.rawpathLineEdit.text())
                tryagain=not os.path.isfile(ramanfp)
            else:
                return
        with open(ramanfp,'r') as fls:
            for flidx,line in enumerate(fls):
                if line.split(':')[0].strip()=='number of spectra':
                    num_spectra=int(line.split(':')[-1].strip())
                    print 'numspect:',num_spectra

                if line.split(':')[0].strip()=='xdata':
                    print 'xdata'
                    xstr=line.split(':')[-1].strip().rstrip(',')
                    xarray=numpy.array([float(p) for p in xstr.split(',')])
                
                if line.split(':')[0].strip()=='ydata':
                    print 'ydata'
                    ystr=line.split(':')[-1].strip().rstrip(',')
                    yarray=numpy.array([float(p) for p in ystr.split(',')])
                    
                if line.split(':')[0].strip()=='Wavenumbers':
                    print line[:400]
                    wvl_str=line.split(':')[-1].strip().rstrip(',')

                if line.split(':')[0].strip().startswith('Spectrum 0'):
                    print line[:400]
                    spec0lineind=flidx
                    break
        Wavenumbers_str=wvl_str.split(',')
        self.ramaninfod={}
        self.ramaninfod['number of spectra']=num_spectra
        self.ramaninfod['xdata']=xarray
        self.ramaninfod['ydata']=yarray
        self.ramaninfod['Wavenumbers_str']=Wavenumbers_str
        self.ramaninfod['Spectrum 0 index']=spec0lineind

        ramaninfop=str(self.infopathLineEdit.text())
        if len(ramaninfop)>0:
            try:
                with open(ramaninfop, mode='w') as f:
                    pickle.dump(self.ramaninfod, f)
            except:
                messageDialog(self, 'Failed to save info file').exec_()
        self.updateinfobrowser()
    
    def updateinfobrowser(self):
        slist=['Num. Spectra: %d' %self.ramaninfod['number of spectra']]
        for k in ['xdata', 'ydata']:
            c=k[0]
            slist+=['%s: %.1f to %.1f' %(c, min(self.ramaninfod[k]), max(self.ramaninfod[k]))]
        self.ramaninfoTextBrowser.setText('\n'.join(slist))
    def readinfotable(self):
        filestr=str(self.sampleinfoTextBrowser.toPlainText())
        sampletable_keys=str(self.infokeysLineEdit.text()).split(',')
        sampletable_keys=[k.strip() for k in sampletable_keys if len(k.strip())>0]
        if len(sampletable_keys)!=5:
            return 'did not find 5 keys in %s' %','.join(sampletable_keys)
        
        lines=filestr.split('\n')
        l_lines=[[s.strip() for s in l.split('\t')] for l in lines if len(l.split('\t'))>=5]
        sampletable_colinds=[l_lines[0].index(s) for s in sampletable_keys if s in l_lines[0]]
        if len(sampletable_colinds)!=5:
            return 'did not find 5 columns, only found these column indeces: %s' %','.join(['%d' %i for i in sampletable_colinds])
        self.smparr, self.xrng_0,self.xrng_1,self.yrng_0,self.yrng_1=[numpy.float32([l[i] for l in l_lines[1:]]) for i in sampletable_colinds]
        self.smparr=numpy.int32(self.smparr)#not great practice to confer str to float to int but oh well
        return False
    def match(self, copypath=None):
        savefolder=str(self.savepathLineEdit.text())
        tryagain=not os.path.isdir(savefolder)
        while tryagain:
            self.selectrawpath()
            tryagain=messageDialog(self, 'Save folder does not exist. Try again?').exec_()
            if tryagain:
                self.selectrawpath()
                savefolder=str(self.savepathLineEdit.text())
                tryagain=not os.path.isdir(savefolder)
            else:
                return True
        
        smp_spectrumindex_map_path=os.path.join(savefolder, 'raman_sample_index_map.map')
        
        reqdkeys=['xdata','ydata','Wavenumbers_str','Spectrum 0 index']
        if False in [k in self.ramaninfod.keys() for k in reqdkeys]:
            messageDialog(self, 'Raman info incomplete. Try "Get Raman File Info"').exec_()
            return True
        xarray, yarray, self.Wavenumbers_str, self.spec0lineind=[self.ramaninfod[k] for k in reqdkeys]
        
        if not copypath is None:
            if not are_paths_equivalent(copypath, smp_spectrumindex_map_path):
                copyfile(copypath, smp_spectrumindex_map_path)
            with open(smp_spectrumindex_map_path, mode='r') as f:
                lines=f.readlines()
            strpairs=[l.split(':') for l in lines]
            self.smp_inds_list=[(int(smpstr), numpy.int32(indsstr.split(','))) for smpstr, indsstr in strpairs]
            return False
            
        errormsg=self.readinfotable()
        if errormsg:
            messageDialog(self, errormsg).exec_()
            return True
        
        

        self.smp_inds_list=[]
        allinds=set([])
        for smpv, a, b, c, d in zip(self.smparr, self.xrng_0,self.xrng_1,self.yrng_0,self.yrng_1):

            inds=numpy.where(((xarray-a)>=0)&((xarray-b)<=0)&((yarray-c)>=0)&((yarray-d)<=0))[0]
            indsunique=sorted(list(set(inds).difference(allinds)))#any spectrum can only be used once due to way file is parsed below
            if len(indsunique)!=len(inds):
                print 'not all inds used in sample %d because Raman spectra were used in other sample' %smpv
            self.smp_inds_list+=[(smpv, indsunique)]
            allinds=allinds.union(indsunique)
        with open(smp_spectrumindex_map_path, mode='w') as f:
            f.write('\n'.join(['%d:%s' %(smpv, ','.join(['%d' %i for i in inds])) for smpv, inds in self.smp_inds_list]))
        
        return False
    def copymatch(self):
        p=mygetopenfile(parent=self, xpath=str(self.savepathLineEdit.text()), markstr='Select Raman .map file for desired sample_no list')
        if len(p)==0:
            return
        self.match(copypath=p)
        
    def extract(self):
        ramanfp=str(self.rawpathLineEdit.text())
        tryagain=not os.path.isfile(ramanfp)
        while tryagain:
            self.selectrawpath()
            tryagain=messageDialog(self, 'Renishaw file does not exist. Try again?').exec_()
            if tryagain:
                self.selectrawpath()
                ramanfp=str(self.rawpathLineEdit.text())
                tryagain=not os.path.isfile(ramanfp)
            else:
                return
                
        savefolder=str(self.savepathLineEdit.text())#dont' check because just checked in last step

        
        ramanind_smp=sorted([(self.spec0lineind+ind, smpv) for smpv, inds in self.smp_inds_list for ind in inds])
        smp_filelines=numpy.int32([smpv for fileind, smpv in ramanind_smp])
        fileind_filelines=numpy.array([fileind for fileind, smpv in ramanind_smp])
        specind_filelines=fileind_filelines-self.spec0lineind
        ramanfilelines=[]
        with open(ramanfp,'r') as fls:

            fileind, k=ramanind_smp.pop(0)
            for count,line in enumerate(fls):
                if count==fileind:
                    ramanfilelines+=[line]
                    print fileind, k, len(ramanind_smp)
                    #print line
                    if len(ramanind_smp)==0:
                        break
                    fileind, k=ramanind_smp.pop(0)
        
        self.sampleComboBox.clear()
        self.samplespectra_filedlist=[]
        smpset=sorted(list(set(smp_filelines)))
        
        
            
        
        for count, smpv in enumerate(smpset):
            inds_fileinds=numpy.where(smp_filelines==smpv)[0]
            strlist=[['wavenumbers']+['spectrum_%d' %specind_filelines[i] for i in inds_fileinds]]
            list_lines=[ramanfilelines[i].split(':')[-1].strip().rstrip(',').split(',') for i in inds_fileinds]
            strlist+=[[wnv]+[listv[count] for listv in list_lines] for count, wnv in enumerate(self.Wavenumbers_str)]
            fp=os.path.join(savefolder, 'Sample%d_selectspectra.rmn' %smpv)
            filed={}
            filed['num_header_lines']=3
            filed['num_data_rows']=len(self.Wavenumbers_str)
            filed['num_data_columns']=len(inds_fileinds)+1
            filed['path']=fp
            
            headstrlist=['%d\t%d\t%d\t%d' %(1, filed['num_data_columns'], filed['num_data_rows'], filed['num_header_lines']-2)]
            try:#this info not availebl if sample info read from file
                selecttableind=list(self.smparr).index(smpv)
                headstrlist+=['%s: %.1f' %(k, arr[selecttableind]) for k, arr in zip('xrng_0,xrng_1,yrng_0,yrng_1'.split(','), [self.xrng_0,self.xrng_1,self.yrng_0,self.yrng_1])]
                filed['num_header_lines']+=4
            except:
                pass
            headstrlist+=['raman_file_lines_spectra: %s' %','.join(['%d' %fileind_filelines[i] for i in inds_fileinds])]
            s='\n'.join(headstrlist+['\t'.join([v for v in l]) for l in strlist])

            with open(fp, mode='w') as f:
                f.write(s)
            self.sampleComboBox.insertItem(count, '%d (%d)' %(smpv, len(inds_fileinds)))
            self.samplespectra_filedlist+=[filed]
        self.plotw_xy.axes.cla()
    
    def readresultsfolder(self):
        folder=str(self.savepathLineEdit.text())
        fns=os.listdir(folder)
        fns_select=sorted([fn for fn in fns if fn.endswith('selectspectra.rmn')])

        p_select=sorted([os.path.join(folder, fn) for fn in fns_select])
        p_ave=sorted([os.path.join(folder, fn.replace('selectspectra', 'ave')) if fn.replace('selectspectra', 'ave') in fns else None for fn in fns_select])
        if len(p_select)==0:
            return
        
        self.sampleComboBox.clear()
        self.samplespectra_filedlist=[]
        self.avespectra_filedlist=[]
            
        for count, (p, pa) in enumerate(zip(p_select, p_ave)):
            smpv=int(p.rpartition('Sample')[2].partition('_')[0])
            with open(p, mode='r') as f:
                chs=f.read(100)
            garb, ncols, nrows, nheadlinesminus2=numpy.int32(chs.partition('\n')[0].strip().split('\t'))
            filed={}
            filed['num_header_lines']=nheadlinesminus2+2
            filed['num_data_rows']=nrows
            filed['num_data_columns']=ncols
            filed['path']=p

            self.sampleComboBox.insertItem(count, '%d (%d)' %(smpv, ncols-1))
            self.samplespectra_filedlist+=[filed]
            if pa is None:
                self.avespectra_filedlist+=[None]
                continue
            with open(pa, mode='r') as f:
                chs=f.read(100)
            garb, ncols, nrows, nheadlinesminus2=numpy.int32(chs.partition('\n')[0].strip().split('\t'))
            filed={}
            filed['num_header_lines']=nheadlinesminus2+2
            filed['num_data_rows']=nrows
            filed['num_data_columns']=ncols
            filed['path']=pa
            self.avespectra_filedlist+=[filed]
        self.plotw_xy.axes.cla()
    
    def saveave(self):
        self.readresultsfolder()
        self.avespectra_filedlist=[]
        for selectfiled in self.samplespectra_filedlist:
            self.processclass.setfiled(selectfiled)
            x, ylist=self.processclass.fcndict['mean']()
            y=ylist[0]
            folder, fn=os.path.split(selectfiled['path'])
            fp=os.path.join(folder, fn.replace('selectspectra', 'ave'))
            filed={}
            filed['num_header_lines']=2
            filed['num_data_rows']=len(x)
            filed['num_data_columns']=2
            filed['path']=fp

            headstrlist=['%d\t%d\t%d\t%d' %(1, filed['num_data_columns'], filed['num_data_rows'], filed['num_header_lines']-2)]
            headstrlist+=['wavenumbers\tspectrum_ave']
            datalines=['%.3f\t%.3f' %tup for tup in zip(x, y)]
            s='\n'.join(headstrlist+datalines)

            with open(fp, mode='w') as f:
                f.write(s)
            self.avespectra_filedlist+=[filed]
                
    def plotwsetup(self):
#        self.xyplotstyled=dict({}, marker='o', ms=5, c='b', ls='-', lw=0.7, right_marker='None', right_ms=3, right_ls=':', right_lw=0.7, select_ms=6, select_c='r', right_c='g')
        self.xyplotcolorrotation=['b', 'k', 'm', 'y', 'c','r', 'g']

        self.plotw_xy=plotwidget(self)
        self.plotw_xy2=plotwidget(self)
        
        for b, w in [\
            (self.textBrowser_xy, self.plotw_xy), \
            (self.textBrowser_xy2, self.plotw_xy2), \
            ]:
            w.setGeometry(b.geometry())
            b.hide()
            
        self.plotw_xy.fig.subplots_adjust(left=.22, bottom=.17)
        self.plotw_xy2.fig.subplots_adjust(left=.22, bottom=.17)
        
        self.plotComboBox.clear()
        for count, k in enumerate(self.processclass.fcnnamelist):
            self.plotComboBox.insertItem(count, k)
    
    def plot(self):
        self.plotw_xy.axes.cla()
        self.plotw_xy2.axes.cla()
        fileind=int(self.sampleComboBox.currentIndex())
        self.processclass.setfiled(self.samplespectra_filedlist[fileind])
        fcnname=str(self.plotComboBox.currentText())
        x, ylist=self.processclass.fcndict[fcnname]()
        for count, y in enumerate(ylist):
            c=self.xyplotcolorrotation[count%len(self.xyplotcolorrotation)]
            self.plotw_xy.axes.plot(x, y, c)
        
        
        
        filed=self.avespectra_filedlist[fileind]
        if not filed is None:
            self.processclass_ave.setfiled(filed)
            x, ylist=self.processclass_ave.first()
            for count, y in enumerate(ylist):
                c=self.xyplotcolorrotation[count%len(self.xyplotcolorrotation)]
                self.plotw_xy2.axes.plot(x, y, c)
        
        self.plotw_xy.fig.canvas.draw()
        self.plotw_xy2.fig.canvas.draw()
class processspectrafile():
    def __init__(self):
        self.fcnnamelist=['first', 'random10', 'minarea', 'maxarea', 'area3points', 'area5points', 'area9points', 'mindiff', 'maxdiff', 'diff3points', 'diff9points', 'mean']
        self.fcns=[self.first, self.random10, self.minarea, self.maxarea, self.minmaxmidarea, self.area5points, self.area9points, self.mindiff, self.maxdiff, self.diff3points, self.diff9points, self.meanfcn]
        self.fcndict=dict([(k, fcn) for k, fcn in zip(self.fcnnamelist, self.fcns)])
    
    def setfiled(self, filed):
        self.filed=filed
    def readselcols(self, selcolinds=None):
        return readtxt_selectcolumns(self.filed['path'], selcolinds=selcolinds, delim='\t', num_header_lines=self.filed['num_header_lines'], floatintstr=float, zipclass=None, lines=None)
    def first(self):
        arr=self.readselcols(selcolinds=[0, 1])
        return arr[0], [arr[1]]
    def random10(self):
        selcolinds=[0]
        selcolinds+=sorted(list(numpy.random.randint(self.filed['num_data_columns']-1, size=10)+1))
        arr=self.readselcols(selcolinds=selcolinds)
        return arr[0], arr[1:]
    def minarea(self, minbool=True):
        arr=self.readselcols(selcolinds=None)
        areas=arr[1:].sum(axis=1)
        if minbool:
            i=numpy.argmin(areas)
        else:
            i=numpy.argmax(areas)
        return arr[0], [arr[i+1]]
    def maxarea(self):
        return self.minarea(minbool=False)
    def minmaxmidarea(self, npts=3):
        arr=self.readselcols(selcolinds=None)
        areas=arr[1:].sum(axis=1)
        inds=numpy.argsort(areas)
        selinds=inds[numpy.int32(numpy.round(numpy.linspace(0,1,num=npts)*(len(areas)-1)))]+1
        return arr[0], arr[selinds]
    def area5points(self):
        return self.minmaxmidarea(npts=5)
    def area9points(self):
        return self.minmaxmidarea(npts=9)
    
    def mindiff(self, indlist_or_numpts=[0]):
        arr=self.readselcols(selcolinds=None)
        m=arr[1:].mean(axis=0)
        inds=numpy.argsort([((v-m)**2).sum() for v in arr[1:]])
        if isinstance(indlist_or_numpts, int):
            selinds=inds[numpy.int32(numpy.round(numpy.linspace(0,1,num=indlist_or_numpts)*(len(arr)-2)))]+1
        else:
            selinds=inds[indlist_or_numpts]+1
        return arr[0], arr[selinds]
    
    def maxdiff(self):
        return self.mindiff(indlist_or_numpts=[-1])
    def diff3points(self):
        return self.mindiff(indlist_or_numpts=3)
    def diff9points(self):
        return self.mindiff(indlist_or_numpts=9)
    def meanfcn(self):
        arr=self.readselcols(selcolinds=None)
        m=arr[1:].mean(axis=0)
        return arr[0], [m]
if __name__ == "__main__":
    class MainMenu(QMainWindow):
        def __init__(self, previousmm, execute=True, **kwargs):
            super(MainMenu, self).__init__(None)
            self.parseui=dataparseDialog(self, title='Visualize ANA, EXP, RUN data', **kwargs)
#            p=r'\\htejcap.caltech.edu\share\home\processes\analysis\temp\20150909.230012.done\20150909.230012.ana'
#            self.visui.importana(p=p)
#            self.visui.plotfom()

            self.parseui.rawpathLineEdit.setText('K:/users/hte/Raman/30058/30058-map--5s-.txt')
            self.parseui.infopathLineEdit.setText('K:/users/hte/Raman/30058/30058-map--5s-.pck')
            self.parseui.savepathLineEdit.setText(r'K:\users\hte\Raman\30058\30058_map28_curated_EM_components_Sm2MnNiO6_type')
            self.parseui.infokeysLineEdit.setText('platemap 28 sample no,x_range0,x_range1,y_range0,y_range1')
            sampletablefile=r'K:\users\hte\Raman\30058\30058_map28_curated_EM_components_Sm2MnNiO6_type.txt'
            with open(sampletablefile, mode='r') as f:
                filestr=f.read()
            self.parseui.sampleinfoTextBrowser.setText(filestr)
#            self.parseui.rawpathLineEdit.setText('K:/users/hte/Raman/30058/30058-map--5s-.txt')
#            self.parseui.infopathLineEdit.setText('K:/users/hte/Raman/30058/20160511test/30058-map--5s-.pck')
#            self.parseui.savepathLineEdit.setText(r'K:\users\hte\Raman\30058\20160511test')
#            self.parseui.infokeysLineEdit.setText('platemap_samp_no,xrng_0,xrng_1,yrng_0,yrng_1')
#            sampletablefile=r'K:\users\hte\Raman\30058\201605test\select_smps.txt'
#            with open(sampletablefile, mode='r') as f:
#                filestr=f.read()
#            self.parseui.sampleinfoTextBrowser.setText(filestr)
            if execute:
                self.parseui.exec_()

    mainapp=QApplication(sys.argv)
    form=MainMenu(None)
    form.show()
    form.setFocus()
    mainapp.exec_()
    
    
