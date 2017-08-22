#!/usr/bin/python
from setuptools import setup, Extension
import os

phonetisaurusmodule = Extension(
    'Phonetisaurus',
    include_dirs=['/usr/local/include', '../src'],
    libraries=['c++'],
    library_dirs=[os.path.abspath('./build')],
    sources=['test.cc'],
    language='c++',
    extra_compile_args=['-std=c++11', '-v'],
)


#Install phonetisaurus 
setup (
    name         = 'phonetisaurus',
    version      = '0.3',
    description  = 'Phonetisaurus G2P python package (OpenFst-1.6.x)',
    url          = 'http://code.google.com/p/phonetisaurus',
    author       = 'Josef Novak',
    author_email = 'josef.robert.novak@gmail.com',
    license      = 'BSD',
    packages     = ['phonetisaurus'],
    ext_modules  = [phonetisaurusmodule],
    include_package_data = True,
    install_requires = ["argparse", "bottle"],
    zip_safe     = False
)
