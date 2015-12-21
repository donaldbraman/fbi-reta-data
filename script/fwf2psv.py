### This is a python 3 script that converts the FBI UCR RETA master files into pipe-separated ascii text files. 
### It's not clear why the files have occassional non-ascii characters, but I replace them with ascii. 
### The aim is to create files that can be easily imported into a database. 

import zipfile
import struct
from os.path import expanduser
import os 
import re
import zipfile
import os.path

home_dir = '..'
source_dir = home_dir + '/masterfiles/'
output_dir = home_dir + '/recoded-data/'

# unzip the files we'll be using
# 

# a combination recipe for the field widths. See the readme.md for details on each field. 
file_header_widths = (1, 2, 7, 2, 1, 2, 5, 2, 1, 7, 1, 6, 4, 2, 1, 9, 3, 3, 9, 3, 3, 9, 3, 3, 9, 9, 9, 1, 1, 1, 1, 24, 6, 30, 30, 30, 30, 5, 1, 29)
monthly_header_widths = (2, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1) 
cards_0123_widths = (5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5) 
card_4_widths = (3, 3, 7)
mw =  monthly_header_widths + cards_0123_widths * 4 + card_4_widths  # monthly field widths 
field_widths =  file_header_widths + mw * 12                         # add them all up
sum(field_widths)                                                    # check to make sure it adds up to 7385

# set up replacements for negative values
def correction(matchobj): 
    if matchobj.group()[5]=='J': 
        return matchobj.group()[0] + '-' + matchobj.group()[1:5] + '1' 
    elif matchobj.group()[5]=='K': 
        return matchobj.group()[0] + '-' + matchobj.group()[1:5] + '2' 
    elif matchobj.group()[5]=='L': 
        return matchobj.group()[0] + '-' + matchobj.group()[1:5] + '3' 
    elif matchobj.group()[5]=='M': 
        return matchobj.group()[0] + '-' + matchobj.group()[1:5] + '4' 
    elif matchobj.group()[5]=='N': 
        return matchobj.group()[0] + '-' + matchobj.group()[1:5] + '5' 
    elif matchobj.group()[5]=='O': 
        return matchobj.group()[0] + '-' + matchobj.group()[1:5] + '6' 
    elif matchobj.group()[5]=='P': 
        return matchobj.group()[0] + '-' + matchobj.group()[1:5] + '7' 
    elif matchobj.group()[5]=='Q': 
        return matchobj.group()[0] + '-' + matchobj.group()[1:5] + '8' 
    elif matchobj.group()[5]=='R': 
        return matchobj.group()[0] + '-' + matchobj.group()[1:5] + '9' 
    else:
        return matchobj.group()[0] + '-' + matchobj.group()[1:5] + '0'

def dequote(matchobj): 
    if matchobj.group()[0] == """'""": 
        return ' ' 
    elif matchobj.group()[0] == '''"''': 
        return ' ' 

# There are many odd characters and typos that need fixing in the data.  
# Many of these were discovered by examing the data, and more may exist.  

def clean_line(line_in):  # convert input to bytes and results back to strings
  fmtstring = ''.join('%ds' % f for f in field_widths)      # concatenate field widths 
  aline = line_in.encode('ascii', 'replace')                # replace non-ascii characters with ?
  bline = struct.Struct(fmtstring).unpack_from(aline)       # slice into bytes
  sline = tuple(s.decode() for s in bline)                  # convert into strings
  pline = "|".join(sline)                                   # rejoin with pipe seperator
  cline = re.sub('\|\d{4}[J-R, \}]', correction, pline)     # correct for negative number symbols
  qline = re.sub('[\',\"]', dequote, cline)                 # remove quotation marks
#  oline = re.sub('000000000   ...\|', '000000000000000|', qline)  # mark funky population groups as missing
  return qline

for year_num in range(1960, 2011):                         # one for each year that we have data
  file_in_name = "RETA" + str(year_num) + ".txt"           # old prefix + year + old suffix
  file_out_name = "reta_" + str(year_num) + "_data.psv"    # new prefix + year + new suffix
  i = open(source_dir + file_in_name, encoding="latin-1")  # for some reason the RETA files are encode as latin-1 rather than ascii
  o = open(output_dir + file_out_name, "w")                # open the output file
  print('processing' , file_in_name)                       # just to keep track of progress
  line_in = i.readline()                                   # as johnny cash would say, "one piece at at time!" 
  line_number = 0                                          # line number for debugging
  while line_in: 
    line_number = line_number + 1                           # increase the line number
    if len(line_in) > 7385:                                 # if the line is long enough
      line_out = clean_line(line_in)                        # parse the line for pipe-fitting
      print(line_out, file=o)                               # write to the year output file
      line_in = i.readline()                                # read the next line
    elif len(line_out) < 7386 and len(line_out) > 2:        # if the line is too short but not blank then diagnose below
      print(line_in)                                        # we want to know what it looks like
      print('line number',                                  # and we want to know which line, etc.
            line_number, 
            'in file',  
            file_in_name, 
            'is', 
            len(line_in), 
            'chars long')
      line_in = i.readline()
    else:
      line_in = i.readline()
  i.close()                                                # close the source file
  o.close()                                                # close the output file
  
  z=output_dir + file_out_name +'.zip'                     # generate zipped version for github
  x='./'+ file_out_name
  z=zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED)
  z.write(output_dir + file_out_name ,x)
  z.close()
  os.remove(output_dir+file_out_name)
  
print('All done!')

