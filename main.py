from os import getcwd
from random import shuffle
from string import ascii_letters as al
import subprocess as sp
from  zipfile import ZipFile
al = list(al + '1234567890')
shuffle(al)
al = ''.join(al[:10])

path = getcwd()+'\\temp'
print(path)
ZipFile(al+'.zip', 'w')
a = "7z a -tzip {}.zip {}".format(al, path)
print(a)

sp.check_call(a)