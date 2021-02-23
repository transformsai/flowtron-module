from distutils.core import setup
import os

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install


class PreDevelopCommand(develop):
    """Pre-installation for development mode."""

    def run(self):
        make_inits()
        develop.run(self)


class PreInstallCommand(install):
    """Pre-installation for installation mode."""

    def run(self):
        make_inits()
        install.run(self)


def make_inits():
    currentDir = os.path.dirname(__file__)
    touch(os.path.join(currentDir, "cheem"))
    touch(os.path.join(currentDir, "./src/flowtron/__init__.py"))
    touch(os.path.join(currentDir, "./src/flowtron/tacotron2/__init__.py"))
    touch(os.path.join(currentDir, "./src/flowtron/tacotron2/waveglow/__init__.py"))


def touch(path: str):
    basedir = os.path.dirname(path)
    if not os.path.exists(basedir):
        os.makedirs(basedir)

    with open(path, "a"):
        os.utime(path, None)


setup(
    name="flowtron-module",
    version="0.1.2",
    description="Pipelining to allow using flowtron as a pip module",
    author="NVIDIA",
    author_email="rafaelvalle@nvidia.com",
    package_dir={"": "src"},
    packages=["flowtron", "flowtron.tacotron2", "flowtron.tacotron2.waveglow"],
    cmdclass={
        "develop": PreDevelopCommand,
        "install": PreInstallCommand,
    },
    install_requires=[
        "torch==1.7.1",
        "matplotlib==3.3.2",
        "numpy==1.19.2",
        "inflect==4.1.0",
        "librosa==0.6.3",
        "scipy==1.5.2",
        "Unidecode==1.0.22",
        "pillow",
        "tensorboardX",
    ],
    license="Apache-2.0 License",
)
