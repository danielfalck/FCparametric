import FreeCAD

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
