# Reading the file
f_obj = open('test.txt', 'r')
for line in f_obj:
    print(line.rstrip())
f_obj.close()
