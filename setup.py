from setuptools import setup
from Cython.Build import cythonize

setup(
    name='functions',
    ext_modules=cythonize("functions_dev.pyx"),
    zip_safe=False,
)

setup(
    name='auto_voice_channels',
    ext_modules=cythonize("auto_voice_channels_dev.pyx"),
    zip_safe=False,
)

