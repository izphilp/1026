# Writing into a file
f_obj = open('test.txt', 'w')
f_obj.write('Welcome\nThis is a file')
f_obj.close()

# Reading the file
f_obj = open('test.txt', 'r')
content = f_obj.read()
print(content)
f_obj.close()
