"""Setup script for hpc."""
import sys
import platform
import os
from subprocess import Popen, PIPE
from distutils import sysconfig
from setuptools import setup,find_packages
import datetime

print find_packages()
##with open('requirements.txt', 'r') as f:
##    for lib in f.readlines():
##        cmd = ['pip', 'install', lib ]
##        res = Popen(cmd, stdout=PIPE, stderr=PIPE, stdin=PIPE)
##        print res.stdout.read()
path = r'C:\Python27\Lib\site-packages'
##print res
for x in os.listdir(path):
    if x.startswith('pack1'):
        print x
        ver = float(x.split('-')[1])+1.0
        break
print ver
setup(name='pack1',
      version=str(ver),
      description='teaching',
      packages=find_packages(),
      zip_safe=False)

time_stamp = "\n\n****Installation Completed at " + str(datetime.datetime.now().strftime('%Y%m%d')) + "****\n\n"
print time_stamp
