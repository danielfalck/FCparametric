FCparametric
============

Parametric objects for FreeCAD

FreeCAD is a very powerful open source solid modelling program. One of the reasons that it is powerful is that it uses python scripting and can use scriptable CAD objects. 

This is my repo for parametric parts. Hopefully it will inspire others to add on to it.

In the '/macros' directory, there will be macros that download and run scripts from other directories. The macros should be set up to check and see if a file has already been downloaded, to save some time.

The first macro that I have set up is for making a 3D parametric vise, with movable jaw. In the '/vise' directory, there are python scripts, 3D step files, and an SVG file for the vise icon. In the '/macros' directory is the vise_macro.py file that will do the downloading and manipulating of the files.  It creates a '/vise' directory and populates it - in the user's macro file directory.vise_macro.py also imports the python scripts in that directory and creates the vise in the currently active FreeCAD document.

Open up the vise_macro.py file- clicking on it and then clicking on 'Raw' in Github is a perfectly fine way of getting at it. Copy and paste the contents of that file into the FreeCAD python console or paste it into the FreeCAD macro editor and then press the 'play' button. Save it as a macro, if it is of any use to you.

Dan Falck
