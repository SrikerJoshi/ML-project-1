from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''this function is used to read the requirements from the requirements.txt file as a list of strings'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements

setup(
    name='Ml_project',
    version='0.0.1',
    author='sriker joshi',
    author_email='sriker.sj@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)