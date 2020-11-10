#===============================================================================
# content                 = create cube class
#
# version                 = 0.0.1
# creation date           = 2020-11-03
#
# how to                  = 
# dependencies            = - Visual Studio Code 1.50.1
#                           - Sublime Text 3.2.2 
# to dos                  = 
#
# author                  = Kalvin Irawan <kalvin.irawan@gmail.com>
#===============================================================================


#===============================================================================
# CLASS
class Cube():
 
    def __init__(self, name):
        self.name = name

        self.size      = [0,0,0]
        self.rotate    = [0,0,0]
        self.translate = [0,0,0]

        self.color     = [0,0,0]

    def print_infos(self):
        print(self.name,
            '\nsize: ', self.size,
            '\nrotate: ' , self.rotate,
            '\ntranslate: ', self.translate,
            '\ncolor: ', self.color)

# create object
cube_A = Cube(name='prp_cube_A')
cube_B = Cube(name='prp_cube_B')

# override
cube_A.size = [1,4,5]
cube_A.translate = [150,30,305]
cube_A.color = [240,185,255]

cube_B.rotate = [4,45,64.7]
cube_B.color = [255,50,85]

cube_A.print_infos()
cube_B.print_infos()

# comment