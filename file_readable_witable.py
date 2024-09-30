f=open('/Users/apple/Desktop/file_handle/file1.txt',mode='r')
if f:
    print("File Successfully opened")
print(f.readable()) #return true if file open in read mode
print(f.writable()) #true if file is opened in write mode