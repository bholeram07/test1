f=open('/Users/apple/Desktop/file_handle/file1.txt',mode='r')

if f:
    print("File Successfully Opened")
print("File name is ",f.name)
print(f.mode)
print("Is File Closed ? ", f.closed)
f.close()
print("Is File Closed ? ", f.closed)
