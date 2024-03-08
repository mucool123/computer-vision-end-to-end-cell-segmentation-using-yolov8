# Import the necessary functions from setuptools
from setuptools import find_packages, setup

# Setup function to configure package details
setup(
    # Package name, used for distribution
    name = 'cellSegmentation',
    
    # Version of the package. Following semantic versioning: Major.Minor.Patch
    version= '0.0.0',
    
    # Name of the author of the package
    author= 'Mukul Gharpure',
    
    # Email address of the author
    author_email= 'gharpuremukul786@gmail.com',
    
    # Automatically find packages included in this distribution
    # find_packages() detects directories with an __init__.py file
    # and includes them as packages
    packages= find_packages(),
    
    # List of dependencies required to use the package
    # Since it's an empty list here, no external packages are required
    install_requires = []
)
