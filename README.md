# capno-reader
This is a binary parser for MedTronic's Capnostream, which relies on [KaiTai](http://kaitai.io/) to handle the data structures described in [CapnostreamDataTransferProtocols.pdf](CapnostreamDataTransferProtocols.pdf). The final implementation is written entirely in Python 3, and converts Capnostream `.bin` files into `.csv` files.

The code was written as part Northwestern University's BME capstone design course, on behalf of my team's client: the **C**enter for **A**utonomic **M**edicine in **P**ediatrics at Lurie Children's Hospital in Chicago, IL.

For anyone interested in parsing Capnostream `.bin` files on their own, this code is available for free under the GNU GPL described in [license.txt](license.txt). However, you should be aware that a number of shortcuts were taken in developing this software. Edge cases were ignored, and QA testing focused exclusively on the CO2 readings that were of interest to our client. If you have any interest in collaborating on this project to produce a parser that examines Capnostream files more generally, please contact me.
