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
import sys

def test0():
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

    x, y = epsg.convert(11582404.84, 3604991.03);
    print('\n[ {1}, {0} ]'.format(x, y))

    x, y = epsg.convert(11582615.46, 3605028.85);
    print('\n[ {1}, {0} ]'.format(x, y))

    x, y = epsg.convert(11582610.8,3605054.72);
    print('\n[ {1}, {0} ]'.format(x, y))

    x, y = epsg.convert(11582397.7,3605018.89);
    print('\n[ {1}, {0} ]'.format(x, y))

def north4thRing():
    epsg = Epsg('epsg:3857', 'epsg:4326')
    for xy in [ [11578238.61,3604584.74], [11578499.09,3604564.42], [11579118.56,3604502.63],
                [11579607.44,3604468.45], [11579607.44,3600000], [11579000,3600000] ]:
        x, y = epsg.convert(xy[0], xy[1])
        print('[ {1}, {0} ],'.format(x, y))

def c4326_3857(argv):
    epsg = Epsg( 'epsg:4326', 'epsg:3857' )
    y, x = float(argv[2]), float(argv[3])
    # 104.01623725891113, 30.58287876835149
    x, y = epsg.convert(x, y)
    print('{0}, {1}'.format(x, y))

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

options = {0 : test0,        # default
           1 : north4thRing, # 四环路北段
		   2 : c4326_3857,
}

def main():
	if len(sys.argv) > 1:
		i = int(sys.argv[1])
		if i in options:
			options[i](sys.argv)
		else:
			print(str(options))
	else:
		test0()

main()
