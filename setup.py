from xml.etree.ElementTree import VERSION
from setuptools import setup
from typing import List

def get_requirements_list()->List[str]:
    pass

#Declaring vvariables for setup function
PROJECT_NAME="Housing Prediction"
VERSUON="0.0.1"
AUTHOR="Deepak rautella"
DESCRIPTION="This is a first FSDS batch Machine Learning Project"
PACKAGES=["housing"] #list of folders passing as package

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
    
)