from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(filepath: str) -> List[str]:
    packages = []

    with open(filepath) as f:
        packages = [x.strip() for x in f.readlines()]
        if HYPEN_E_DOT in packages:
            packages.remove(HYPEN_E_DOT)

setup(
    name="ml-pipeline",
    version="0.0.1",
    description="Repo for ML pipeline",
    author="Hyder",
    author_email="hyderrezatelegraphy@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)