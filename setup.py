import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-bcf-cas',
    version='0.1.2',
    packages=['bcf_cas'],
    include_package_data=True,
    license='GPL-3 License',
    description='A django app for enabling CAS auth.',
    long_description=README,
    url='https://github.com/nickeddy',
    author='Nicholas Eddy',
    author_email='eddy.nicholas@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
