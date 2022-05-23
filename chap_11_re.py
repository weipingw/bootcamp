import re
line = "this is a test"
if re.search('^that', line):
  print(line)
else:
  print('NO')