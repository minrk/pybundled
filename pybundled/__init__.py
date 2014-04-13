# load libbundled extension, if there is one:
try:
    from . import libbundled
except ImportError:
    pass

# import Cython extension
from .bundled import *