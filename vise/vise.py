import Draft,Part
import FreeCAD, FreeCADGui
import FreeCADGui as Gui
from FreeCAD import Base 
from PySide import QtGui, QtCore
from math import fabs
import utils
import os.path

class Vise:
    def __init__ (self, obj):
        '''create a milling machine vise '''
        obj.addProperty("App::PropertyFloat", "JawOpening", "Parallel", "How wide the jaws of the vise are open")
        obj.JawOpening = 0.0
        obj.Proxy = self

    def execute(self, fp):
        self.p = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macro")
        self.macropath = self.p.GetString("MacroPath","")

        self.base = Part.Shape()
        if os.path.isfile(self.macropath+"/vise/vise_base.stp"):
            self.base.read(self.macropath+"/vise/vise_base.stp")
        else:
            vise_base_url = "https://raw.githubusercontent.com/danielfalck/FCparametric/master/vise/vise_base.stp"
            vise_base = utils.download(vise_base_url,force = True)
            self.base.read(vise_base)

        self.jaw = Part.Shape()
        if os.path.isfile(self.macropath+"/vise/vise_jaw.stp"):
            self.jaw.read(self.macropath+"/vise/vise_jaw.stp")
        else:
            vise_jaw_url = "https://raw.githubusercontent.com/danielfalck/FCparametric/master/vise/vise_jaw.stp"
            vise_jaw = utils.download(vise_jaw_url,force = True)
            self.jaw.read(vise_jaw)

        if 0<=fabs(fp.JawOpening)<= 223.52:
            self.jaw.Placement.Base.y = -(fabs(fp.JawOpening))
        else:
            self.jaw.Placement.Base.y = -223.52
        fp.Shape =Part.makeCompound([self.base,self.jaw])


class ViewProviderVise:
    def __init__(self, obj):
        "Set this object to the proxy object of the actual view provider"
        obj.Proxy = self

    def getIcon(self):

        self.p = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macro")
        self.macropath = self.p.GetString("MacroPath","")

        if os.path.isfile(self.macropath+"/vise/vise.svg"):
            i =QtGui.QIcon(self.macropath+"/vise/vise.svg")
        else:
            vise_icon_url = "https://raw.githubusercontent.com/danielfalck/FCparametric/master/vise/vise.svg"
            vise_icon = utils.download(vise_icon_url, force = True)
            i =QtGui.QIcon(vise_icon)
        p =  i.pixmap(128,128)
        a = QtCore.QByteArray()
        b = QtCore.QBuffer(a)
        b.open(QtCore.QIODevice.WriteOnly)
        p.save(b,"XPM")
        b.close()
        return str(a)




'''how to use:
obj =FreeCAD.ActiveDocument.addObject("Part::FeaturePython",'Vise')
Vise(obj)
ViewProviderVise(obj.ViewObject)
FreeCAD.ActiveDocument.recompute()
Once you have a vise in the view-
change how much the jaw opening is in the Data tab of the Property panel.
'''

