# Reading the file
f_obj = open('test.txt', 'r')
for line in f_obj:
    print(line, end='')
f_obj.close()
