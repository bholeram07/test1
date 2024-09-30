import os
file_list=[]
while True:
    file_name=input("Enter the file name ")
    file_list.append(file_name)
    a=input("Do you want to continue y/n").lower()
    if a!='y':
        break

for files in file_list:
    filename=files+".txt"
    f=open(filename,mode='r')
    merged_data=merged_data+f.read()+'\n'
    f.close()
print(merged_data)
    

