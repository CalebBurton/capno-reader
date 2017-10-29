''' Overall wrapper program to parse the binary output from Medtronic's capnostream devices

    Copyright (C) 2017 Caleb Burton

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

    See the GNU General Public License at <http://www.gnu.org/licenses/>
    for more details. Note that The GNU General Public License does NOT
    permit incorporating this code into proprietary programs.

    Questions about this code can be directed to @CalebBurton on GitHub
'''

import csv
from capno_structs import Capno
#from byte_cleaner import clean_byte

PATH = "/Users/calebburton/Documents/GitHub/capnoReader/"
FILEIN = PATH + "capnostream_dirty.bin"
FILEOUT = PATH + "capnostream_clean.bin"

CSV_OUT = PATH + "capno.csv"
CSV_BYTES = []

print('\nReading file (this may take a moment)...')

#clean_byte(FILEIN, FILEOUT)

C = Capno.from_file(FILEOUT)
print('File parsed. Total messages found: ', len(C.every_message))

with open(CSV_OUT, 'w') as csvfile:
    FILEWRITER = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    FILEWRITER.writerow(['Wave Message Number',
                         'Instantaneous CO2 Value',
                         'CO2_Malfunction',
                         'Filterline Not Connected',
                         'Purging in Progress',
                         'SFM in Progress',
                         'End of Breath Indication',
                         'Occlusion in Gas Input Line',
                         'Initialization',
                         'Invalid CO2 Value'])
    print('Header written.\nWriting data.', end='')
    for msgNo, CapnoMsg in enumerate(C.every_message):
        if CapnoMsg.msg_code == Capno.CapCodes.co2_wave_code:
            FILEWRITER.writerow([CapnoMsg.msg_body.wave_message_number,
                                 CapnoMsg.msg_body.instantaneous_co2_value,
                                 CapnoMsg.msg_body.fast_status.co2_malfunction,
                                 CapnoMsg.msg_body.fast_status.filterline_not_connected,
                                 CapnoMsg.msg_body.fast_status.purging_in_progress,
                                 CapnoMsg.msg_body.fast_status.sfm_in_progress,
                                 CapnoMsg.msg_body.fast_status.end_of_breath_indication,
                                 CapnoMsg.msg_body.fast_status.occlusion_in_gas_input_line,
                                 CapnoMsg.msg_body.fast_status.initialization,
                                 CapnoMsg.msg_body.fast_status.invalid_co2_value])
            # if not(msgNo % 25000):
            #     print('.', end='')
    print('\nFile successfully written to "', CSV_OUT, '"\n')


# for j in c.every_message:
#     print(j.msg_code)
