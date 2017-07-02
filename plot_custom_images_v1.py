import os, sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from DataParseApp import dataparseDialog
projectpath=os.path.split(os.path.abspath(__file__))[0]
sys.path.append(os.path.join(projectpath,'ui'))

pythoncodepath=os.path.split(projectpath)[0]
jcapdataprocesspath=os.path.join(pythoncodepath, 'JCAPDataProcess')
sys.path.append(jcapdataprocesspath)


sys.path.append(os.path.join(jcapdataprocesspath,'AuxPrograms'))
from fcns_ui import *
from fcns_io import *

platemapvisprocesspath=os.path.join(pythoncodepath, 'JCAPPlatemapVisualize')
sys.path.append(platemapvisprocesspath)


import numpy as np

###############UPDATE THIS TO BE THE FOLDER CONTAINING parameters.py
paramsfolder=r'K:\users\hte\Raman\40374\20170630analysis'
#paramsfolder=r'K:\users\hte\Raman\33444\20170608analysis'

#if not paramsfolder is None:
sys.path.append(paramsfolder)
from parameters import *


class MainMenu(QMainWindow):
    def __init__(self, previousmm, execute=True, **kwargs):
        super(MainMenu, self).__init__(None)
        self.parseui=dataparseDialog(self, title='Visualize ANA, EXP, RUN data', **kwargs)
        #self.alignui=plateimagealignDialog(self, manual_image_init_bool=False)
        if execute:
            self.parseui.exec_()


mainapp=QApplication(sys.argv)
form=MainMenu(None, execute=False)
#form.show()
#form.setFocus()
#mainapp.exec_()

parseui=form.parseui

parseui.rawpathLineEdit.setText(pathd['ramanfile'])
parseui.infopathLineEdit.setText(pathd['infopck'])
parseui.getinfo(ramaninfop=pathd['infopck'], ramanfp=pathd['ramanfile'])#opens or creates
parseui.savepathLineEdit.setText(pathd['spectrafolder'])
parseui.match(copypath=pathd['map'])
parseui.readresultsfolder()

parseui.plotComboBox.setCurrentIndex(12)
os.chdir(r'K:\users\hte\Raman\40374\20170630analysis\images_each_sample')
x0, x1=260, 430
fig=parseui.plotw_xy.fig
ax=parseui.plotw_xy.axes
for i in range(len(parseui.samplespectra_filedlist)):
    parseui.sampleComboBox.setCurrentIndex(i)
    s='Sample%s' %str(parseui.sampleComboBox.currentText())
    fn=s.partition(' ')[0]+'.png'
    parseui.plot()
    fig.savefig(fn)
    if '-' in s:
        continue
    fn2=fn[:-4]+'_zoom.png'
    ym=max([y[(parseui.plot_x>-x0) & (parseui.plot_x<=x1)].max() for y in parseui.plot_ylist])
    ax.set_xlim(x0, x1)
    ax.set_ylim(0, ym)
    fig.savefig(fn2)
        

parseui.exec_()
