# -*- coding: utf-8 -*-
from math import cos, fabs, radians
import urllib3
from json import loads

DEG_CONST = 111.32138


def planes(url='https://opensky-network.org/api/states/all', ident='states'):
    """

    :param url: URI of opensky-network API.
    :param ident: JSON identificator for planes
    :return: Returns plane ID, latitude and longtitude.
    """

    data = loads(
        urllib3.PoolManager().request('GET', url).data.decode('utf-8')
    )
    return data[ident]


def around(y, x, radius=1):
    """

    :param x: latitude. Sets in degrees and decimal (15 degrees and 30 minutes is 15.5).
    :param y: longtitude. The same as x.
    :param radius: Radius around point in km.
    :return: Set of four coordinates: x1, x2, y1 and y2.
    """
    if x > 90 or x < -90 or y > 180 or y < -180:
        raise ValueError('Coordinates are too small or too big!')
    if radius > 1000 or radius < 1:
        raise ValueError('Radius is too big or too small!')

    # translate radius to degrees and return diaposone
    r = radius/DEG_CONST*cos(radians(fabs(x)))
    # TODO if y + r > 180 or < 0 _or -90_ or x > 90 or < 0
    return x-r, x+r, y-r, y+r


def find(pl_coords, *args):
    """

    :param pl_coords: Data about planes which got coordinates.
    :param args: Coordinates of circle in deegres.
    :return: ID of plane (string)
    """

    if args[0][0] < pl_coords[6] < args[0][1] and args[0][2] < pl_coords[5] < args[0][3]:
        return pl_coords[0]


def find_planes_around(la=2.349014, lo=48.864716, ra=450):
    return list(
        filter(
            None,
            [
                find(
                    x, around(la, lo, ra)
                ) for x in
                filter(
                    lambda x: x[0] is not None and x[6] is not None and x[5] is not None, planes()
                )
            ]
        )
    )


if __name__ == '__main__':
    print(find_planes_around())
