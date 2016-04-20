try:
    from setuptools import setup, Extension
except ImportError :
    raise ImportError("setuptools module required, please go to https://pypi.python.org/pypi/setuptools and follow the instructions for installing setuptools")


setup(
    name='dedupe-variable-person',
    url='https://github.com/datamade/dedupe-variables-person',
    version='0.0.1',
    description='Variable type for American Person Names',
    packages=['dedupe.variables'],
    install_requires=['dedupe-variables-name']
    license='The MIT License: http://www.opensource.org/licenses/mit-license.php'
    )
