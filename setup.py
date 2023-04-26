# setup.py
from setuptools import setup, find_packages

setup(
    name='random_name',
    version='0.1',
    description='generate a random network name',
    author='klaudyu',
    py_modules=['random_name'],
    packages=find_packages(),
    package_data={
	'random_name':['nouns.txt','adjectives.txt'],
    },
    author_email='klaudyu@gmail.com',
    url='https://github.com/klaudyu/random_name',
    install_requires=['numpy'],
)
