from distutils.core import setup

setup(
    name="flowtron-module",
    version="0.1",
    description="Pipelining to allow using flowtron as a pip module",
    author="NVIDIA",
    author_email="rafaelvalle@nvidia.com",
    url="https://transforms.ai/",
    package_dir={"": "src"},
    packages=["flowtron"],
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
