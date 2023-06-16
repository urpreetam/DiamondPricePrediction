from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requiremetns(path:str)->List[str]:
    requirements=[]
    with open(path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements


setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='urpreetam',
    install_requires= get_requiremetns('requirements.txt'),
    packages=find_packages()
)