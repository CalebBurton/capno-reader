import array
import struct
import zlib
from enum import Enum

from capnoStructs import Capno

g = Capno.from_file("/Users/calebburton/Desktop/capnostream.bin")

for j in g.every_message:
    print(j.msg_code)