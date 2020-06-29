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

def north4thRing(arg):
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

def c3857_4326(argv):
    epsg = Epsg( 'epsg:3857', 'epsg:4326' )
    x, y = float(argv[2]), float(argv[3])
    # 104.01623725891113, 30.58287876835149
    y, x = epsg.convert(x, y)
    print('{0}, {1}'.format(x, y))

def ring4Circle(argv):
    pos = [
    [ 104.07262802124022, 30.72597392766885 ], [ 104.04584884643555, 30.728408697633384 ],
    [ 104.01864051818848, 30.708855021221527 ], [ 104.00190353393555, 30.702434647871947 ],
    [ 103.98164749145508, 30.66213151789336 ], [ 103.98130416870117, 30.653862130404377 ],
    [ 103.99932861328124, 30.62845887475364 ], [ 104.0185546875, 30.614055811000792 ],
    [ 104.04353141784668, 30.601054282909143 ], [ 104.07846450805664, 30.60024162945578 ],
    [ 104.09494400024414, 30.596695425524466 ], [ 104.11983489990234, 30.599798361062593 ],
    [ 104.1331386566162, 30.60689041196974 ], [ 104.14283752441406, 30.61974343067441 ],
    [ 104.14369583129881, 30.62506142209331 ], [ 104.16069030761719, 30.666856564516053 ],
    [ 104.15863037109375, 30.703172643553152 ], [ 104.15142059326172, 30.71025711487616 ],
    [ 104.1342544555664, 30.713799155433104 ], [ 104.12120819091797, 30.719997413394207 ],
    [ 104.08584594726562, 30.72235854972469 ], [ 104.07264947891234, 30.725937036741882 ] ]
    epsg = Epsg( 'epsg:4326', 'epsg:3857' )
    for xy in pos:
        x, y = epsg.convert(xy[1], xy[0])
        print('[{0:.2f}, {1:.2f}]'.format(x, y), end=', ')
    print('')

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
           3 : c3857_4326,
           4: ring4Circle,   # ring4 light path
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
