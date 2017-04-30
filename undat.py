from struct import unpack
import os
import sys


def undat (src, dst):
    datfile = open(src, 'rb')

    buffer = datfile.read(28)

    header = unpack('<LLL16s', buffer)

    buffer = datfile.read(8)
    while buffer:
        subheader = unpack('<lHH', buffer)
        path = datfile.read(subheader[1])
        path = ''.join([ chr(ord(c) ^ 0xFF) for c in path])
        print path
    
        if subheader[0] != -1:
            if not os.path.exists(dst + os.path.dirname(path)):
                os.makedirs(dst + os.path.dirname(path))
            file = open(dst + path, 'wb')
            buffer = datfile.read(subheader[0])
            buffer = ''.join([chr(ord(c) ^ 0xFF) for c in buffer])
            file.write(buffer)
            file.close();
        else:
            os.makedirs(dst + path)
        
        buffer = datfile.read(8)

    datfile.close()

def usage():
    print ("Usage:")
    print (sys.argv[0] + " <datfile> <output_dir>")

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        usage()
    else:
        undat(sys.argv[1], sys.argv[2])
