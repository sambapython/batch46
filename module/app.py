#fun()
"""
searching: sys.path
	It's looks for .py file, If it's find .py
							 then look for .pyc file also.
							 	if it's find .pyc file, then it looks for 
							 	modified date abd time of .py and .pyc.
							 	if .pyc modified date and time> .py modified time
							 	then it's not compile the file. 
							 	if .pyc modified date and time< .py modified time
							 	then it's compile the file.
							 If it's not find .pyc then it will create.
	It's not find .py file then it look for .pyc file.
		if it's find .pyc then it will consider that
		if it's not find .pyc file also then it will throw an error.

"""
"""
import sys
print sys.path
import f2
"""
'''
import sys
sys.path.reverse()
print sys.path
import f1
'''
'''
import sys
sys.path.append("/home/khyaathi-python")
print sys.path
import f2
'''
'''
import f1
f1.fun()
print f1.a
print f1.b
'''
'''
import f1
f1.fun()
print f1.a
print f1.b
#print f1.c
import sys
print sys.path
'''
'''
import abcd
abcd.file1.fun()
'''
'''
import abcd
abcd.file1.fun()
'''
'''
from abcd import file1
file1.fun()

'''
'''
import abcd
abcd.file1.fun()
'''
'''
from abcd import file1
file1.fun()
'''

from abcd import file1,file2
file1.fun()
file2.fun()
