from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='opensky_network_api',
    version='1.0',
    packages=find_packages(),
    long_description=open('README.txt').read(),
    author='marperia',
    author_email='golden.mountains@yandex.ru',
    url='https://github.com/marperia/opensky_network_api/',
    description='API for opensky-network.org to find planes near special place.',
    download_url='https://github.com/marperia/opensky_network_api/archive/master.zip',
    license='Apache License, Version 2.0, see LICENSE file',
    install_requires=['urllib3', 'json', 'math'],
)