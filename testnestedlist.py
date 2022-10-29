"""""
PROBLEM: https://www.hackerrank.com/challenges/nested-list/problem

STEPS:
1. Make a list of students and their grades (nested)
2.Make a list of the grades:
    2.a. remove duplicates
    2.b. arrange
3. Match students with the 2nd lowest grade
4.Make a list of students in step(3)
    4.a. aarange them
    4.b. print each on a separate line
"""

"""____________________STEP:1____________________"""
num=int(input("enter number of students:"))
full_list=[]
marks=[]

for i in range(num):
    name=input("enter name:")
    score=float(input("enter grade:"))
    full_list.append([name,score])
    marks.append(score)



"""____________________STEP:2____________________"""
marks=sorted(set(marks))

print(marks)
"""____________________STEP:3____________________"""
if len(marks) == 1:
    map=marks[0]
else:
    map=marks[1]

filter=[]

for x in full_list:
    if  map == full_list[1]:
        filter.append(x[0])
"""____________________STEP:4____________________"""
print(filter)
filter.sort()

for j in filter:
    print(j)

print(filter)









