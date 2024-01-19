a=[3,2,44,12,34,23,17,10]
fh=open('output7.txt','w')
print(a)
fh.write(f'the given list is {str(a)}\n')
b=int(input('choose one 1.asscending order 2.descending order:'))
if(b==1):
    a.sort()
    print(a)
    fh.write(f'asscending order {str(a)}')
if (b==2):
    a.sort(reverse=True)
    print(a)
    fh.write(f'descending order {str(a)}')

fh.close()