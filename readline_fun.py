f=open('/Users/apple/Desktop/file_handle/file1.txt',mode='r')
if f:
    print("File Successfully opened")
data=f.readlines()
print(data)
f.close()