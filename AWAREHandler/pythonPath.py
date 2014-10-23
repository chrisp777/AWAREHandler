'''
Created on 23 Oct 2014

@author: Chris
'''
import os
try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []