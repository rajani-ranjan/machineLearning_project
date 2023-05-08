from setuptools import find_packages, setup
from typing import List

heifen_e_dot = '-e .'


def get_requirements(file_path)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements =[]
    with open(file_path,'r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if heifen_e_dot in requirements:
            requirements.remove(heifen_e_dot)
    return requirements

setup(
    name = "ml_project",
    version = '0.0.1',
    author = 'Rajani Ranjan Kumar',
    author_email = 'right.rajveer.96@gmail.com',
    description = 'Machine Learning Project',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)