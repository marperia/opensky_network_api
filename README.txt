# Opensky-network.org API
API for opensky-network.org to find planes near special place.

Usage:

    from opensky_network_api import main

    main.find_planes_around(latitude, longtitude, radius)

or, simple

    main.find_planes_around()

Where latitude and longtitude in diaposone from -180 to 180° (e.g. -15.2353) and from -90° to 90° and radius from 1 to 1000 km (e.g. 450). Default values are 2.349014°, 48.864716° (Paris) and 450 km.
