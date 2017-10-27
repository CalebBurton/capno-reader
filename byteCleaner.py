from enum import Enum


def cleanByte( fileIn, fileOut ):
    "Opens a binary file and folds any 0x80 bytes into the following byte,\
     as per Capnostream data transfer prototcols"
    
    with open(fileIn, "rb") as fr:
        b = fr.read()
        barr = bytearray(b)
        byteLocs = [i for i, x in enumerate(barr) if x == 0x80]
        badBytes = []

        for i, l in enumerate(byteLocs):
            barr[l] = barr[l] + barr[l+1]
            badBytes.append(l+1)
            # if i < 5:
            #     print(l, '\t', barr[l], '\t', barr[l+1])

        targ = len(barr)
        #print('old len: ', len(barr))
        for i, b in enumerate(reversed(badBytes)):
            del(barr[b])
        
        #print('new len: ', len(barr))
        
    with open(fileOut, "wb") as fw:
         fw.write(barr)

path = "/Users/calebburton/Documents/GitHub/capnoReader/"
fileIn = path + "capnostream_dirty.bin"
fileOut = path + "capnostream_clean.bin"

cleanByte(fileIn, fileOut)