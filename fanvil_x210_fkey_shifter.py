#!/usr/bin/env python
import re, pytz
from datetime import datetime
from pprint import pprint

first_fkey = int(input("Input the number of the function key you want to start shifting from: "))
last_fkey = int(input("Input the number of the function key that will shift last: "))
page_to_edit = int(input("Input the number of the page in which the function keys will be edited: "))
source_file = input("Input the name of the source configuration xml file: ")

current_date = datetime.now(pytz.utc).strftime ('%d-%b-%Y')
dest_file = source_file.split('.')[0] + '_' + str(current_date) + '.xml' # Destination file name like source_file_current_day.xml
regex = (r'<internal index="(?P<page>\d+)"'
         r'|<Fkey index="(?P<fkey>\d+)"')
opnd_src_file = open(source_file)
proxy_list = opnd_src_file.readlines()

for count, line in enumerate(proxy_list):
    match = re.search(regex, line)
    if match:
        if match.lastgroup == 'page':
            page = match.group('page')        
        if int(page) == page_to_edit and match.lastgroup == 'fkey':
            fkey = int(match.group('fkey'))
            if fkey >= first_fkey and fkey <= last_fkey:
                proxy_list[count] = f'            <Fkey index="{fkey + 1}">\n'

opnd_src_file.close()

# write proxy_list to dest_file       
dest = open(dest_file, 'w')
dest.writelines(proxy_list)
dest.close()
