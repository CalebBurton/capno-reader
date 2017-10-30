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
from byte_cleaner import clean_byte

PATH = "/Users/calebburton/Desktop/Capnostream Data/"

#-----------------------------------------------------------------------------
#                File Name                      | No. Messages | Validity
#-----------------------------------------------------------------------------
#FILENAME = "FCT_ADULT_170929_134350_B500001504_1"  #     550 (no good)
#FILENAME = "FCT_ADULT_171002_234909_B541112857_1"  #     136 (no good)
#FILENAME = "FCT_ADULT_171003_085043_B500001504_1"  #   4,766 (no good)
#FILENAME = "FCT_ADULT_171004_110830_B500001504_1"  # 271,033 (good at 12,232)
#FILENAME = "FCT_ADULT_171004_145424_B500001504_1"  # 114,769 (good at 79,850)
#FILENAME = "FCT_ADULT_171005_103607_B500001504_1"  # 102,614 (good at 88,432)
#FILENAME = "FCT_ADULT_171005_115824_B500001504_1"  #     183 (no good)
#FILENAME = "FCT_ADULT_171005_115833_B500001504_1"  #      64 (no good)
#FILENAME = "FCT_ADULT_171005_115845_B500001504_1"  # 284,498 (good at --,--1)
#FILENAME = "FTT_ADULT_170929_134316_B500001504_1"  #      36 (no good)

FILEIN = PATH + "dirty bin/" + FILENAME + ".bin"
FILEOUT = PATH + "clean bin/"  + FILENAME + ".bin"

CSV_OUT = PATH + "csv/CO2_" + FILENAME + ".csv"
CSV_BYTES = []

print('\nCleaning file (this may take a moment)...')
clean_byte(FILEIN, FILEOUT)

print('Reading file (this may take a moment)...')
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
