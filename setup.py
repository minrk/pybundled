"""
Example package for bundling a C dependency as a Python Extension
if it is not found.

This example is a Cython project, but it doesn't need to be.
"""

from __future__ import print_function

import glob
import os
import sys
pjoin = os.path.join

from distutils.core import setup
from distutils.extension import Extension

# if not using Cython, get build_ext from distutils
# from distutils.command.build_ext import build_ext
from Cython.Distutils import build_ext

def line():
    print('-' * 60)

class DetectBundled(build_ext):
    description = "Locate libbundled, and bundle it as an extension if we can't find it"
    
    already_run = False
    
    def build_extensions(self):
        """we don't actually want to do any compilation"""
        return
    
    def run(self):
        if self.already_run:
            # don't run more than once
            return
        # build_ext.run configures the compiler and calls self.build_extensions (no-op)
        build_ext.run(self)
        
        # check if we can link a simple program against libbundled
        cc = self.compiler
        line()
        print("Checking for libbundled")
        cc.output_dir = self.build_temp
        if cc.has_function("bundled_version", libraries=["bundled"]):
            print("Found libbundled")
            line()
            # nothing to update
        else:
            self.bundle_extension()
            line()
        # prevent running a second time
        self.already_run = True
    
    def bundle_extension(self):
        """prepare for libbundled as an extension
        
        - update compilation of existing extensions
        - create libbundled extension
        """
        print("libbundled not found, building libbundled as an Extension")
        for ext in self.distribution.ext_modules:
            # don't link libbundled, it will be loaded at runtime
            if 'bundled' in ext.libraries:
                ext.libraries.remove('bundled')
            # add the header directory from the local bundled sources
            if "libbundled" not in ext.include_dirs:
                ext.include_dirs.append("libbundled")
        
        # build libbundled as a Python Extension
        # In this case, libbundled is trivial - it links no external libraries,
        # so we only need to include its .c sources.
        libbundled = Extension(
            'pybundled.libbundled',
            sources = glob.glob(pjoin('libbundled', '*.c'))
        )
        
        # build libbundled first:
        self.distribution.ext_modules.insert(0, libbundled)


def detect_first(command):
    """decorator to run detect before a given command"""
    class detect_then_run(command):
        def run(self):
            self.distribution.run_command('detect')
            return command.run(self)
        
    return detect_then_run

# register the detect command
# and replace build_ext with a copy that ensures `detect` is run first
cmdclass = {
    'detect' : DetectBundled,
    'build_ext' : detect_first(build_ext),
}

# initially, the Extensions
extensions = [
    Extension(
        'pybundled.bundled',
        sources = [
            pjoin('pybundled', 'bundled.pyx'),
            pjoin('pybundled', 'libbundled.pxd'),
        ],
        libraries = [
            'bundled'
        ]
    )
]

package_data = {
    'pybundled' : [
        '*.pyx',
        '*.pxd',
    ]
}
setup_args = dict(
    name = "pybundled",
    version = "0.0.1",
    packages = ['pybundled'],
    ext_modules = extensions,
    package_data = package_data,
    author = "Min Ragan-Kelley",
    author_email = "zeromq-dev@lists.zeromq.org",
    url = 'http://github.com/minrk/pybundled',
    description = "Example for bundling a library",
    long_description = __doc__,
    license = "Public Domain",
    cmdclass = cmdclass,
)

setup(**setup_args)