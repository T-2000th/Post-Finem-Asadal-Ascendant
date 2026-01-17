import re

import os
os.chdir(os.path.dirname(__file__))

def format_file(filename):
   with open(filename, 'r') as f:
      content = f.read()
      if content[-1] != '\n':
            content += '\n'

      found_matches = re.finditer(r'\n(\d+\.\d+\.\d+)\s+=\s+{', content)
      deletethese = []
      for match in found_matches:
         date = match[1]
         date = date.split('.')
         year = date[0]
         year = int(year)
         if year <= 1444:
            continue
         
         endpos = 0
         indent = 1
         ending = False
         for i, char in enumerate(content[match.end(0):]):
            if ending == True:
               if char == '\n':
                  endpos = match.end(0) + i
                  break
               else:
                  continue
            if char == '{':
               indent += 1
            if char == '}':
               indent -= 1
               if indent == 0:
                  ending = True
         deletethese.append([match.start(0) + 1, endpos + 1])
      
      for delete in reversed(deletethese):
         contentbefore = content[:delete[0]]
         contentafter = content[delete[1]:]
         content = contentbefore + contentafter
   with open(filename, 'w') as f:
      f.write(content)

import glob
list_of_files = glob.glob('*.txt')
for unchanged in list_of_files:
   format_file(unchanged)
# print( len( list_of_files ) )