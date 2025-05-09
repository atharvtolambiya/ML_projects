from setuptools import find_packages , setup
from typing import List


def get_requirments(file_path:str) -> List[str]:

  requirment = []
  with open(file_path) as file_obj:
    requirment = file_obj.readlines()
    requirment = [req.replace('\n','') for req in requirment]

    if('-e.' in requirment):
      requirment.remove('-e.')

  return requirment

setup(

  name = 'ML_project',
  version= '0.0.1',
  author='Atharv',
  author_email="tolambiyaatharv@gmail.com",
  packages=find_packages(),
  install_requires = get_requirments('requirments.txt')
)