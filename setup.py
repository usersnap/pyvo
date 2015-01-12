import os
from setuptools import setup, find_packages
from pyvo import VERSION, DEV_STATUS

setup(
    name='pyvo',
    version='.'.join(map(str, VERSION)),
    description='Pivotal Tracker REST API v5 client',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    keywords='python pivotal tracker',
    author='Michael Bourke',
    author_email='git@elementality.com',
    url='https://github.com/iter8ve/pyvo',
    license='MIT license',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: %s' % DEV_STATUS,
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    ],
    install_requires=[
        'requests',
        'purl'
    ],
)
