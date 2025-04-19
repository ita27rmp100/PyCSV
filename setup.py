from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Simple library to handle with .csv files'
LONG_DESCRIPTION = 'This library has a nine function to import the data from csv files , organize the data that you import ... etc.'

# Setting up
setup(
    name="PyCSV",
    version=VERSION,
    author="Tayeb Abderahim Ismail",
    author_email="tayebabderahim27@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'os'],
    keywords=['python', 'csv', 'excel', 'file management'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)