from distutils.core import setup, Extension
import numpy as np

msslDir = '<path_to_mssl_io_libraries>' # download the I/O lib from European Space Agency's website
                                        # https://earth.esa.int/web/guest/software-tools/-/article/software-routines-7114
                                        # install in this path
incDirs = [msslDir+'/mssl_shared',
           msslDir+'/mssl_cryosat']
libDirs = [msslDir+'/mssl_shared',
           msslDir+'/mssl_cryosat']

cryoSat_ext = Extension(
                         "csarray",
                         sources = ["src/pycsarray.c",
                                     "src/csarray.c"],
                         include_dirs = incDirs,
                         libraries = ['mssl_cryosat','mssl_shared', 'm'],
                         library_dirs = libDirs,
                         extra_compile_args = ['-Wall', '-Iinclude']
                         )

setup (
       author = 'Jack Ogaja',
       name = 'cryoSatArray',
       version = '0.1.0',
       ext_modules = [cryoSat_ext],
       include_dirs = [np.get_include()]
      )

