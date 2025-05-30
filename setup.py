import os

from Cython.Distutils import build_ext
import numpy as np
from setuptools import Extension
from setuptools import find_packages
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), "README.md"),
          encoding='utf-8') as readme:
    long_description = readme.read()

genome_module = Extension(
    "selene_sdk.sequences._sequence",
    ["selene_sdk/sequences/_sequence.pyx"],
    include_dirs=[np.get_include()])

genomic_features_module = Extension(
    "selene_sdk.targets._genomic_features",
    ["selene_sdk/targets/_genomic_features.pyx"],
    include_dirs=[np.get_include()])

ext_modules = [genome_module, genomic_features_module]
cmdclass = {'build_ext': build_ext}

setup(name="selene-sdk",
      version="0.6.0",
      long_description=long_description,
      long_description_content_type='text/markdown',
      description=("framework for developing sequence-level "
                   "deep learning networks"),
      packages=find_packages(),
      url="https://github.com/FunctionLab/selene",
      package_data={
        "selene_sdk.interpret": [
            "data/gencode_v28_hg38/*",
            "data/gencode_v28_hg19/*"
        ],
        "selene_sdk.sequences": [
            "data/*"
        ]
      },
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
      ],
      ext_modules=ext_modules,
      cmdclass=cmdclass,
      python_requires='>=3.9',
      install_requires=[
        "cython>=0.29.24",
        'click',
        "h5py",
        "matplotlib>=2.2.3",
        "numpy>=1.21.4",
        "pandas",
        "plotly",
        "pyfaidx",
        "pytabix",
        "pyyaml>=5.1",
        "ruamel.yaml",
        "scikit-learn",
        "scipy",
        "seaborn",
        "statsmodels",
        "torch>=1.0.0, <=2.3.1",
    ],
    entry_points={
        'console_scripts': [
            'selene_sdk = selene_sdk.cli:main',
        ],
    },
)
