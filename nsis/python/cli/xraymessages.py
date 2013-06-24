
#Copyright (c) 2009, 2010, Bruno Golosio, Antonio Brunetti, Manuel Sanchez del Rio, Tom Schoonjans and Teemu Ikonen
#All rights reserved.

#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#    * The names of the contributors may not be used to endorse or promote products derived from this software without specific prior written permission.

#THIS SOFTWARE IS PROVIDED BY Bruno Golosio, Antonio Brunetti, Manuel Sanchez del Rio, Tom Schoonjans and Teemu Ikonen ''AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL Bruno Golosio, Antonio Brunetti, Manuel Sanchez del Rio, Tom Schoonjans and Teemu Ikonen BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from _winreg import *
from __future__ import print_function


def display_banner():
	key = OpenKey(HKEY_LOCAL_MACHINE,r'Software\xraylib',0,KEY_READ)
	res = QueryValueEx(key,"")

	print ()
	fp = open(res[0]+'\\Doc\\xraybanner.txt', 'r')
	for line in fp.readlines():
		print (line, end="")
	fp.close()
	print ()
	CloseKey(key)

def display_options():
	print ()
	print (" - Type 'xraylib -h' to see a list of the available functions")
	print (" - Type 'xraylib -d' to see the X-ray data documentation")
	print (" - Type 'xraylib -f function-name' to get help on a" \
          " specific function")

def display_usage():
	print ()
	print (" usage: xraylib 'expression'")
	print ("     where 'expression' is any mathematical expression")
	print ("     that can contain X-ray library functions.")
	display_options()

def display_help():
	key = OpenKey(HKEY_LOCAL_MACHINE,r'Software\xraylib',0,KEY_READ)
	res = QueryValueEx(key,"")
	print ()
	print ("Available X-ray library functions")
	print ()
    	fp = open(res[0]+'\\Doc\\xrayfunc.txt', 'r')
    	for line in fp.readlines():
		print (line, end="")
	fp.close()
    	CloseKey(key)
    	display_usage()

def display_doc():
	key = OpenKey(HKEY_LOCAL_MACHINE,r'Software\xraylib',0,KEY_READ)
	res = QueryValueEx(key,"")
	print ()
	print ("X-ray data documentation")
	print ()
    	fp = open(res[0]+'\\Doc\\xraydoc.txt', 'r')
    	for line in fp.readlines():
		print (line, end="")
	fp.close()
    	CloseKey(key)
	print ()

