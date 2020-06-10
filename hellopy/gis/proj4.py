'''
Pyproj
https://github.com/pyproj4/pyproj

To install, follow
http://pyproj4.github.io/pyproj/stable/installation.html

ridiculous trouble:
If this file named as 'pyproj.py', you won't import Proj from pyproj.

@author: odys-z@github.com
'''
# from pyproj import Proj, transform
from pyproj import Proj, transform

def main():
    epsg = Epsg('epsg:3857', 'epsg:4326')
    x, y = epsg.convert(-11705274.6374, 4826473.6922)
    print(x, y)

    x, y = epsg.inverse(x, y)
    print(x, y)

class Epsg(object):
    '''
        usage: 
        ------
            epsg = Epsg('epsg:3857', 'epsg:4326')
            x, y = epsg.convert(-11705274.6374, 4826473.6922)
            x, y: 39.72785727727917 -105.15027111593008
    '''
       
    def __init__(self, fromESPG, toESPG):
        # inProj = Proj('epsg:3857')
        # outProj = Proj('epsg:4326')
        self.epsg0 = Proj(fromESPG)
        self.epsg1 = Proj( toESPG )

    def convert(self, x, y):
        # x1,y1 = -11705274.6374,4826473.6922
        x2, y2 = transform(self.epsg0, self.epsg1, x, y)
        return x2, y2

    def inverse(self, x, y):
        x2, y2 = transform(self.epsg1, self.epsg0, x, y)
        return x2, y2

main()