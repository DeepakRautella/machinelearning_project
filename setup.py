from setuptools import setup,find_packages
from typing import List

#Declaring vvariables for setup function
PROJECT_NAME="Housing Prediction"
VERSION="0.0.3"
AUTHOR="Deepak rautella"
DESCRIPTION="This is a first FSDS batch Machine Learning Project"
PACKAGES=["housing"] #list of folders passing as package or find_packages
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    
    Description: This function is going to return list of requirement
       mentioned in requiements.txt file
       
       return this function is  going to return a list of which contain name of 
       librarires mentioned i n requirements file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
    )
