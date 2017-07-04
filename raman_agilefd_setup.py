# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 16:09:50 2017

@author: sksuram
"""
import sys,os, pickle, numpy, pylab, operator, itertools
import cv2
from shutil import copy as copyfile
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import matplotlib.pyplot as plt
plt.ion()
from DataParseApp import dataparseDialog
from sklearn.decomposition import NMF
#from PlateAlignViaEdge_v7 import *

from PlateAlignViaEdge_v8 import MainMenu,save_raman_udi
#print dasf
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



avefiles=[]
parentfold=r'K:\users\hte\Raman\39664\for AgileFD'
sys.path.append(parentfold)
from parameters_agilefd import *

print plateidstr
smp_fold=os.path.join(parentfold,'samples')
smp_spect_fold=os.path.join(parentfold,'samples','sample_spectra')

substrate_fold=os.path.join(parentfold,'substrate')
substrate_spect_fold=os.path.join(parentfold,'substrate','sample_spectra')

if gen_smp_substrate_spect:
    if not 'sample_spectra' in os.listdir(parentfold):
        subfolders=map(lambda x:os.path.join(parentfold,x),os.listdir(parentfold))
        subfolders=[x for x in subfolders if os.path.isdir(x)]
        for subf in subfolders:
            if not 'sample_spectra' in os.listdir(subf):
                continue
            else:
                temp_avefiles=filter(lambda x:x.endswith('_ave.rmn'),os.listdir(os.path.join(subf,'sample_spectra')))
                avefiles+=map(lambda x:os.path.join(subf,'sample_spectra',x),temp_avefiles)
    

    if not os.path.exists(smp_spect_fold):
        os.makedirs(smp_spect_fold)
       
    if not os.path.exists(substrate_spect_fold):
        os.makedirs(substrate_spect_fold)
    
    for x in avefiles:
        if os.path.basename(x).split('Sample')[-1][0]=='-':
            newf=x.replace('Sample-','Sample')
            copyfile(x,os.path.join(substrate_spect_fold,os.path.basename(newf)))
        else:
            copyfile(x,os.path.join(smp_spect_fold,os.path.basename(x)))



if gen_udis:
    mainapp=QApplication(sys.argv)
    form=MainMenu(None, execute=False)    
    visui=visdataDialog(form, title='Visualize ANA, EXP, RUN data')
    smp_pathd={'spectrafolder':smp_spect_fold,'udibasepath':os.path.join(smp_fold,'ave_rmn_')}
    substrate_pathd={'spectrafolder':substrate_spect_fold,'udibasepath':os.path.join(substrate_fold,'ave_rmn_')}
    i=0
    for pathd in [smp_pathd,substrate_pathd]:    
#        visui.exec_() 
        print i
        i+=1
        save_raman_udi(visui,pathd,udi_ternary_projection_inds,plateidstr,saveall=False)