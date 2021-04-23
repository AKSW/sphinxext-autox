import os
import sphinx.ext

__version__ = '0.0.1'

# override sphinx.ext with our patched versions
sphinx.ext.__path__.insert(
    0,
    os.path.abspath(
        os.sep.join([os.path.dirname(__file__), '..', 'sphinx', 'ext'])))
print("SPHINX EXT PATH IS NOW", sphinx.ext.__path__)

def setup(app):
    return dict()
