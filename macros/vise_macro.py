import FreeCAD
import sys

def download(url,force=False):
    '''downloads a file from the given URL and saves it in the
    macro path. Returns the path to the saved file'''
    import urllib2, os
    name = url.split('/')[-1]
    p = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macro")
    macropath = p.GetString("MacroPath","")
    if not macropath:
        macropath = FreeCAD.ConfigGet("UserAppData")
    filepath = os.path.join(macropath,name)
    if os.path.exists(filepath) and not(force):
        return filepath
    try:
        FreeCAD.Console.PrintMessage("downloading "+url+" ...\n")
        response = urllib2.urlopen(url)
        s = response.read()
        f = open(filepath,'wb')
        f.write(s)
        f.close()
    except:
        return None
    else:
        return filepath

try:
    import vise,utils

except:
    libsok =False

if not libsok:

#download the python script 
    baseurl = "https://raw.githubusercontent.com/danielfalck/FCparametric/master/python/"
    files = ['vise.py', 'utils.py']
    for f in files:
        p = download(baseurl+f, force = True
    d = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macro")
    macropath = d.GetString("MacroPath","")
    sys.path.append(macropath)
    import vise,utils



obj =FreeCAD.ActiveDocument.addObject("Part::FeaturePython",'Vise')
vise.Vise(obj)
vise.ViewProviderVise(obj.ViewObject)
FreeCAD.ActiveDocument.recompute()


