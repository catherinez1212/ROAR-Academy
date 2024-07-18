import os

filename = 'motto.txt'

try: 
    path = os.path.dirname(os.path.abspath(__file__))
    file1 = open(path+'/'+filename, 'w')
    file1.write('Fiat Lux!\n')
    file1.close()
    file1 = open(path+'/'+filename, 'a')
    file1.write('Let there be light!')
except IOError:
    print('IOError')
    exit
finally:
    file1.close()