#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import subprocess
from setuptools import setup, find_packages
from webdav.client import __version__ as version

from setuptools.command.test import test as TestCommand
from setuptools.command.install import install as InstallCommand

requirements = "libxml2-dev libxslt-dev python-dev libcurl4-openssl-dev python-pycurl"

class Install(InstallCommand):
    
    def run(self):
        
        params = "{install -y} {requirements}".format(requirements=requirements)
        cmd = "{command} {params}".format(command="apt-get", params=params)
        #proc = subprocess.Popen(cmd, shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
        proc = subprocess.Popen(cmd, shell=True)
        proc.wait()
        InstallCommand.run(self)

class Test(TestCommand):
    
    user_options = [('pytest-args=', 'a', "")]

    def initialize_options(self):
        
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name     = 'webdavclient',
    version  = version,
    packages = find_packages(),
    requires = ['python (>= 2.7.6)'],
    install_requires=['pycurl', 'lxml', 'argcomplete'],
    scripts = ['wdc'],
    tests_require=['pytest', 'pyhamcrest', 'junit-xml', 'pytest-allure-adaptor'],
    cmdclass = {'install': Install, 'test': Test},
    description  = 'Webdav API, resource API и wdc для WebDAV-серверов (Yandex.Disk, Dropbox, Google Disk, Box, 4shared и т.д.)',
    long_description = open('README.rst').read(),
    author = 'Designerror',
    author_email = 'designerror@yandex.ru',
    url          = 'https://github.com/designerror/webdavclient',
    download_url = 'https://github.com/designerror/webdavclient/tarball/master',
    license      = 'MIT License',
    keywords     = 'webdav, client, python, module, library, packet, Yandex.Disk, Dropbox, Google Disk, Box, 4shared',
    classifiers  = [
        'Environment :: Console',
        'Environment :: Web Environment', 
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
