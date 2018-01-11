#!/usr./bin/python
import os,sys,re
import subprocess
from subprocess import Popen,PIPE

## call wait for the process to finish, then pass the returncode back
proc = subprocess.call(["cat","1.txt"])
print(proc)

## save output
proc = subprocess.check_output(["cat","1.txt"])
print(proc)

## Popen
proc = Popen(['cat','1.txt'],stdin=PIPE,stdout=PIPE,stderr=PIPE)
out,err = proc.communicate()
print(out)
