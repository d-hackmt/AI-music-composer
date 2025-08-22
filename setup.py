from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


# Install all requirements and packages

setup(
    name="AI MUSIC COMPOSER",
    version="0.1",
    author="dmt",
    packages=find_packages(),
    install_requires = requirements,
)