from setuptools import setup
from Cython.Build import cythonize

setup(
    name='auto_voice_channels',
    ext_modules=cythonize("auto_voice_channels.pyx"),
    zip_safe=False,
)