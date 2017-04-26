import os
import time

print 'Starting RC4 test'

timeStart = time.time()
os.system('python RC4.py')
print 'RC4 ran in ' + str(time.time() - timeStart) + ' seconds'

timeStart = time.time()
print 'Starting CBC'
os.system('python CBCblock.py')
print 'CBC ran in ' + str(time.time() - timeStart) + ' seconds'

timeStart = time.time()
print 'Starting CTR'
os.system('python CTRblock.py')
print 'CTR ran in ' + str(time.time() - timeStart) + ' seconds'
