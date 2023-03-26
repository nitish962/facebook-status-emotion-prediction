from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requriments(file_path:str)->List[str]:
    """this function will return the list of packages """
    requriments=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','')for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements         
    
    

setup(
    name ='facebook prediction',
    version='0.0.1',
    author='nitish',
    author_email='nitishraju962@gmail.com',
    packages=find_packages(),
    install_requires=get_requriments('requirement.txt')
    
    
      
)