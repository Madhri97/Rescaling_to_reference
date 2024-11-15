import sys

dictionary={}
total=0
for line in sys.stdin:
    item=line.split("\t")
    length=int(item[3])
    if length in dictionary:
        dictionary[length]+=1
    else:
        dictionary[length]=1
    total+=1
for i in dictionary:
    normal=dictionary[i]/total
    print(str(i)+"\t"+str(normal))
with open('total_new.txt', 'w')as f:
    f.write(str(total))
