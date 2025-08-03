from setuptools import find_packages, setup
setup(
    name="medical_chatbot",
    version="0.1.0",
    author="Matheshwara",
    author_email="msenthi7@umd.edu",
    packages=find_packages(), 
    install_requires=[] 
)

# find_packages: This line tells the setup function to automatically discover and include all Python packages in your project's directory structure.
# find_packages will try to find constructor file, (init.py) and whenever it sees it, this folder (src) will install as local package
# find_packages() is that it will only recognize a directory as a Python package if that directory contains an __init__.py file.
# src contains all importable python code, which is why that folder is installed as package
# install requires installs all requirements. 

# use pip install -r requirements.txt in bash
# -r is “Read from requirement file”
