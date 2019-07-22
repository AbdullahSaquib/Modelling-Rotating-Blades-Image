# Modelling-Rotating-Blades-Image
Modelling an Image of Rotating Fan Blades Captured By a Camera

Modelling an Image of Rotating Fan Blades Captured By a Camera.pdf
This PDF file contains the abstract, introduction, theory, mathematical models, simulations pictures and conclusion of the project. 

rfb.py
This file contains a class named Blade. The class Blade has methods which can evaluate Blade occupation time (tc), restricted blade occupation time (tr), and opacity (Pr). The attributes of the Blade class are the width (w), angular speed (omg), initial position (pi), final position after exposure time (pf). Blade has a class attribute named ts, which stores the exposure time of the camera. The class method set_ts can be used to set the value of exposure time at runtime. 

draw1.py
This files imports the Blade class and creates four Blades. To plot the opacity as a function of angular position python's turtle library is used. The file is used to create single image of a fan blade. 

draw2.py
This file is just looped vesion of draw1.py. It was used to create many images of varying angular speed and exposure time in one go. This is actually used to generate the images used in the PDF version of the project. However, the output images are .eps file.

Folder 'Rotating Blade Images' contains the simulated fan blades images at varying angular speed and varying exposure time. It also contains the images of actual rotating blades.
