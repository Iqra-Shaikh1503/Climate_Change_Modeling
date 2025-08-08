from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads dependencies from the specified requirements.txt file.

    Removes '-e .' if present to prevent setuptools from re-installing the local package.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='Climate_Change_Modeling',
    version='0.0.1',
    author='Iqra Shaikh',
    author_email='shaikhiqar1503@gmail.com',
    description='A machine learning project for climate change analysis and forecasting',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    include_package_data=True,
)
