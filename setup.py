#!/usr/bin/env -e python

import setuptools
from pip.req import parse_requirements

setuptools.setup(
    name='OCCO-CloudHandler',
    version='0.1.0',
    author='Adam Visegradi',
    author_email='adam.visegradi@sztaki.mta.hu',
    namespace_packages=['occo', 'occo.cloudhandler.backends'],
    py_modules=['occo.cloudhandler.backends.dummy',
                'occo.cloudhandler.backends.boto'],
    packages=['occo.cloudhandler'],
    scripts=[],
    url='http://www.lpds.sztaki.hu/',
    license='LICENSE.txt',
    description='OCCO Cloud Handler',
    long_description=open('README.txt').read(),
    install_requires=['argparse',
                      'PyYAML',
                      'python-dateutil',
                      'boto',
                      'OCCO-Util',
                      'OCCO-InfoBroker',
                      'drett-client'],
)
