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
    print('http://geojson.io}')

    epsg = Epsg('epsg:3857', 'epsg:4326')
    x, y = epsg.convert(0, 0) # 0, 0
    print('3857: x, y [0, 0], -> 4326: {1}, {0}'.format(x, y))

    x, y = epsg.inverse(0, 1) # 111319.49, 0
    print('4326: x, y [0, 1], -> 3857: {0}, {1}'.format(x, y))

    x, y = epsg.inverse(1, 0) # 0, 111325.14
    print('4326: x, y [1, 0], -> 3857: {0}, {1}'.format(x, y))

    x, y = epsg.inverse(0, 180) # 20037508.24, 0
    print('4326: x, y [0, 180], -> 3857: {0}, {1}'.format(x, y))

    x, y = epsg.inverse(0, -180)
    print('4326: x, y [0, -180], -> 3857: {0}, {1}'.format(x, y))

    x, y = epsg.inverse(0, 360)
    print('4326: x, y [0, 360], -> 3857: {0}, {1}'.format(x, y))

    x, y = epsg.inverse(0, 90)
    print('4326: x, y [0, 90], -> 3857: {0}, {1}'.format(x, y))

    print('\n3857: x -11705274.637, y 4826473.6922 ->')
    x, y = epsg.convert(-11705274.6374, 4826473.6922)
    print('4326: {1}, {0}'.format(x, y))

    x, y = epsg.inverse(x, y)
    print('3857: {0}, {1}'.format(x, y))

    print('\n成金青立交桥')
    x, y = epsg.convert(11598279.62, 3598920.63)
    print('"coordinates": [ {1}, {0} ]'.format(x, y))

    print('\n螺狮坝立交桥桥')
    x, y = epsg.convert(11599843.29, 3590647.533)
    print('"coordinates": [ {1}, {0} ]'.format(x, y))

    print('\n四环路北段')
    coord3857 =[[11578238.61,3604584.74], [11578499.09,3604564.42], [11579118.56,3604502.63],
                [11579607.44,3604468.45], [11579940.05,3604472.72], [11580199.1 ,3604493.16],
                [11580506.52,3604537.1 ], [11581002.7 ,3604653.29], [11581199.92,3604702.98],
                [11581342.03,3604737.26], [11581657.42,3604813.96], [11581768.07,3604840.96],
                [11581899.73,3604873.09], [11582034.35,3604905.77], [11582135.58,3604930.33],
                [11582270.45,3604963.08], [11582365.35,3604982.13],
                [11582404.8400000000,      3604991.030000000]];

    for p in coord3857:
        x, y = epsg.convert(p[0], p[1])
        print('[ {1}, {0} ],'.format(x, y))


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
