from os.path import join as pjoin
from setuptools import setup, find_packages
from torch.utils.cpp_extension import CUDAExtension, BuildExtension

def install_requires():
    """Generate list with dependency requirements"""

    deps = []
    with open("requirements.txt", "r") as f:
        for line in f:
            deps.append(line[:-1])
    return deps

setup(
    name="usip",
    version="0.1.0",
    install_requires=install_requires(),
    packages=find_packages(),
    ext_modules=[
        CUDAExtension('index_max', [
            pjoin('ext','index_max','index_max.cpp'),
            pjoin('ext','index_max','index_max_cuda.cu')
        ]),
        CUDAExtension('ball_query', [
            pjoin('ext','ball_query','ball_query.cpp'),
            pjoin('ext','ball_query','ball_query_cuda.cu')
        ]),
    ],
    cmdclass={'build_ext': BuildExtension},
    python_requires=">=3.6",
)