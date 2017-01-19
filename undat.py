from struct import unpack
import os

datfile = open('file.dat', 'rb')

buffer = datfile.read(28)

header = unpack('<LLL16s', buffer)

print header

buffer = datfile.read(8)
while buffer:
    subheader = unpack('<lHH', buffer)
    print subheader
    path = datfile.read(subheader[1])
    path = ''.join([ chr(ord(c) ^ 0xFF) for c in path])
    print path
    
    if subheader[0] != -1:
        if not os.path.exists('out' + os.path.dirname(path)):
            os.makedirs('out' + os.path.dirname(path))
        file = open('out' + path, 'wb')
        buffer = datfile.read(subheader[0])
        buffer = ''.join([chr(ord(c) ^ 0xFF) for c in buffer])
        file.write(buffer)
        file.close();
    else:
        os.makedirs('out' + path)
        
    buffer = datfile.read(8)

datfile.close()
