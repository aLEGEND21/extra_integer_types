from setuptools import setup
import setuptools

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='extra_integer_types',
    url='https://github.com/aLEGEND21/extra_integer_types',
    author='aLEGEND21',
    author_email='_',
    # Needed to actually package something
    packages=setuptools.find_packages(),
    # Needed for dependencies
    install_requires=[],
    # *strongly* suggested for sharing
    version='0.1.0',
    # The license can be anything you like
    license='MIT',
    description='Get more classes that numbers can be sorted into.',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
