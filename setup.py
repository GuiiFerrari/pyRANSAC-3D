import setuptools
import os
import numpy

from glob import glob

BASEDIR = os.path.abspath(os.path.dirname(__file__))
DIR_PATH = os.path.join("pyransac3d", "_pyransac3d")
CPPFILES = glob(os.path.join(DIR_PATH, "*.cpp")) + glob(os.path.join(DIR_PATH, "*.c"))
HEADERS = glob(os.path.join(DIR_PATH, "*.h"))
HEADERS_FILES = [os.path.basename(path) for path in HEADERS]

module = setuptools.Extension(
    "pyransac3d._pyransac3d",
    sources=CPPFILES,
    include_dirs=[
        numpy.get_include(),
        os.path.join(BASEDIR, "pyransac3d", "_pyransac3d"),
        os.path.join(BASEDIR, "pyransac3d"),
        DIR_PATH,
    ],
    library_dirs=[
        DIR_PATH,
        os.path.join(BASEDIR, "pyransac3d", "_pyransac3d"),
        os.path.join(BASEDIR, "pyransac3d"),
        # os.path.join(BASEDIR, "pyransac3d", "_pyransac3d"),
        "user32",
    ],
    extra_compile_args=[r"-O2"],
    # libraries=["user32"],
    # depends=HEADERS_FILES,
    # extra_link_args=[],
)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyransac3d",
    version="0.6.1",
    author="Leonardo Mariga",
    author_email="leomariga@gmail.com",
    description=(
        "A python tool for fitting primitives 3D shapes in"
        "point clouds using RANSAC algorithm "
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leomariga/pyRANSAC-3D",
    packages=setuptools.find_packages() + [module.name],
    keywords=(
        "point-cloud,segmentation,ransac,cuboid,3d-reconstruction,cylinder,planes"
        ",plane-detection,ransac-algorithm "
    ),
    project_urls={
        "Documentation": "https://leomariga.github.io/pyRANSAC-3D/",
        "Source": "https://github.com/leomariga/pyRANSAC-3D",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    ext_modules=[module],
    install_requires=["setuptools >= 74.1", "numpy"],
    include=["pyransac/_pyransac/*"],
    include_package_data=True,
)
