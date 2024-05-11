n=int(input())

class Student:
    def __init__(self,height,weight,number):
        self.height,self.weight,self.number=height,weight,number

students=[]
for i in range(1,n+1):
    height,weight=tuple(map(int,input().split()))
    students.append(Student(height,weight,i))

students.sort(key=lambda x:(x.height,-x.weight))

for student in students:
    print(student.height,student.weight,student.number)