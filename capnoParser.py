''' Overall wrapper program '''

from capnoStructs import Capno
from byteCleaner import cleanByte


path = "/Users/calebburton/Documents/GitHub/capnoReader/"
fileIn = path + "capnostream_dirty.bin"
fileOut = path + "capnostream_clean.bin"

#cleanByte(fileIn, fileOut)

c = Capno.from_file(fileOut)
print(len(c.every_message))

# for j in c.every_message:
#     print(j.msg_code)