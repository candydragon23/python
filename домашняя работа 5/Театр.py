file1 = open('roles.txt', 'r', encoding = 'utf-8')
file2 = open('output.txt', 'w', encoding = 'utf-8')
lines = file1.readlines()
lines.remove('roles:\n')
rolelines = {}
roles = []
isRole = True
index = -1
for line in lines:
    line = line.replace('  ', '')
    line = line.replace('\xa0—', ' —')
    if line != "textLines:\n" and isRole == True:
        roles.append(line[:-1])
    else:
        isRole = False
    if not isRole:
        index += 1
        if line[0] != ' ':
            key = line[:line.find(':')]
            if not line[line.find(':') + 2:].isspace() and len(line[line.find(':') + 2:]) > 0:
                rolelines.setdefault(key, []).append(str(index) + ') ' + line[line.find(':') + 2:])
        else:
          rolelines.setdefault(key, []).append(str(index) + ') ' + line[1:])
for role in roles:
    file2.write(str(role) + ':\n')
    try:
      for line in rolelines[role]:
          file2.write(line)
    except KeyError:
      file2.write('')
    file2.write('\n')
file2.close()