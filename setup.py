from distutils.core import setup
import py2exe, sys, os

setup(
    console=[{
        "script":"wol.py",
    }],
    options = {
        "py2exe": {
            "bundle_files": 1,
            "optimize": 2,
            "compressed": 1,
            "ascii": False,
        }
    },
    data_files=["README.md","LICENSE",],
    zipfile = None,
    #zipfile = "python.lib",
    version = "1.0",
    name = "wol",
    description = "A simple command line magic packet sender for WOL enabled devices",
    author = "Petros Kyladitis",
    author_email ="petros.kyladitis@gmail.com",
    license = "FreeBSD Licence",
    url = "http://www.multipetros.gr",
    )
