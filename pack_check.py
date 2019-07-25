#from pack1 import a
#print dir(a)

#import pack1
#from pack1 import b
import os
print os.getcwd()
os.chdir('..')
print os.getcwd()
import pack1
import sys
print sys.path
