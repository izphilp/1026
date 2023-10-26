# Writing into a file
f_obj = open('test.txt', 'w')
f_obj.write('Welcome\nThis is a file')
f_obj.close()

# Reading the file
f_obj = open('test.txt', 'r')
for line in f_obj:
    print(line)
f_obj.close()
