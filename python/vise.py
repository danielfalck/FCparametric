import Draft,Part
import FreeCAD, FreeCADGui
import FreeCADGui as Gui
from FreeCAD import Base 
from PySide import QtGui, QtCore
from math import fabs

class Vise:
'''
how to use:
obj =FreeCAD.ActiveDocument.addObject("Part::FeaturePython",'Vise')
Vise(obj)
ViewProviderVise(obj.ViewObject)
FreeCAD.ActiveDocument.recompute()
Once you have a vise in the view-
change how much the jaw opening is in the Data tab of the Property panel.
'''

    def __init__ (self, obj):
        '''create a milling machine vise '''
        obj.addProperty("App::PropertyFloat", "JawOpening", "Parallel", "How wide the jaws of the vise are open")
        obj.JawOpening = 0.0
        obj.Proxy = self

    def execute(self, fp):
        self.base = Part.Shape()
        self.base.read("vise_base.stp")
        self.jaw = Part.Shape()
        self.jaw.read("vise_jaw.stp")
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
        i =QtGui.QIcon("/home/danfalck/Documents/freecad/stock3.svg")
        p =  i.pixmap(128,128)
        a = QtCore.QByteArray()
        b = QtCore.QBuffer(a)
        b.open(QtCore.QIODevice.WriteOnly)
        p.save(b,"XPM")
        b.close()
        return str(a)

#how to use:
#obj =FreeCAD.ActiveDocument.addObject("Part::FeaturePython",'Vise')
#Vise(obj)
#ViewProviderVise(obj.ViewObject)
#FreeCAD.ActiveDocument.recompute()


