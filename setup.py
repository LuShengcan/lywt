from setuptools import find_packages, setup

# Package meta-data.
NAME = 'lywt'
DESCRIPTION = 'LuShengcan 的工具包'
URL = 'https://gitee.com/LuShengcan/lywt.git'
AUTHOR_EMAIL = 'shengcan_lu@foxmail.com'
AUTHOR = 'LuShengcan'
REQUIRES_PYTHON = '>=3.0'
VERSION = '0.1.1'

# What packages are required for this module to be executed?
# REQUIRED = ['requests', 'bs4', 'lxml', 'windnd', 'Crypto']
REQUIRED = []

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    install_requires=REQUIRED,
    license="MIT"
)
