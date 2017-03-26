#!/usr/bin/python 

from subprocess import check_output, Popen, PIPE

output = check_output(["sudo", "./receiveExample.cpp_exe"], shell=False)
print "The output is:", output
# p = Popen(["sudo", "./receiveExample.cpp_exe"], shell=False, stdout=PIPE, stdin=PIPE)
# output = p.stdout

