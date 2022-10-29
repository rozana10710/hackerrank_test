"""URL : https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=next-challenge&h_v=zen"""

from logging import exception


def av(list):
    sum=0
    for r in list :
        sum=sum+r
    return float(sum/len(list))

n=int(input("enter number of students:"))
DB={}
for x in range(n):
    name= input("Enter name:")
    marks=[]
    for i in range (3):
        marks.append(float(input("Enter grade:")))
    DB.update({name:marks})


query= input("Enter query:")

if query in DB:
    res=DB[query]
    result=av(res)
    print(format(result,'.2f'))
else:
    raise exception ("Student does not exist")

