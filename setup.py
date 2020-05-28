from setuptools import setup
from Cython.Build import cythonize

setup(
    name='functions',
    ext_modules=cythonize("functions.pyx"),
    zip_safe=False,
)

setup(
    name='auto_voice_channels',
    ext_modules=cythonize("auto_voice_channels.pyx"),
    zip_safe=False,
)

