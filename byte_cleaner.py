''' Sub-function to pre-process capnostream binary output

    Copyright (C) 2017 Caleb Burton

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

    See the GNU General Public License at <http://www.gnu.org/licenses/>
    for more details. Note that The GNU General Public License does NOT
    permit incorporating this code into proprietary programs.

    Questions about this code can be directed to @CalebBurton on GitHub
'''


def clean_byte(file_in, file_out):
    "Opens a binary file and folds any 0x80 bytes into the following byte,\
     as per Capnostream data transfer prototcols"

    with open(file_in, "rb") as fr:
        b = fr.read()
        barr = bytearray(b)
        byte_locs = [i for i, x in enumerate(barr) if x == 0x80]
        bad_bytes = []

        for l in byte_locs:
            barr[l] = barr[l] + barr[l+1]
            bad_bytes.append(l+1)
            # if i < 5:
            #     print(l, '\t', barr[l], '\t', barr[l+1])

        #print('old len: ', len(barr))
        for b in reversed(bad_bytes):
            del(barr[b])
        #print('new len: ', len(barr))

    with open(file_out, "wb") as fw:
        fw.write(barr)
