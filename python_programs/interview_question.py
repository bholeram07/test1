str='a3b4c8'
output=""
for i in str:
    if i.isalpha():
        var=i
    else:
        num=int(i)
        output=output+(var*num)
print(output)