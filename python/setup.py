#!/usr/bin/python
from setuptools import setup, Extension
from setuptools.command.egg_info import egg_info
import os, sys

class EggInfoCommand(egg_info):
    def run(self):
        if "build" in self.distribution.command_obj:
            build_command = self.distribution.command_obj["build"]
            self.egg_base = build_command.build_base
            self.egg_info = os.path.join(self.egg_base, os.path.basename(self.egg_info))
        egg_info.run(self)

SRC_PATH = os.path.dirname(os.path.dirname(sys.argv[0]))

phonetisaurusmodule = Extension(
    'Phonetisaurus',
    include_dirs=[os.path.join(SRC_PATH,'src')],
    libraries=['fst', 'fstfar', 'fstscript'],
    library_dirs=[os.path.abspath('./build')],
    sources=['Phonetisaurus-binding.cc', os.path.join(SRC_PATH,'src/lib/util.cc')],
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
    cmdclass={"egg_info" : EggInfoCommand},
    package_dir={"" : os.path.join(SRC_PATH,"python")},
    ext_modules  = [phonetisaurusmodule],
    include_package_data = True,
    install_requires = ["argparse", "bottle"],
    zip_safe     = False
)
