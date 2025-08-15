#Create a list to store student data i.e. name, age, course and is_attending. Display each element of list using for loop.
name=input("Enter Your name: ")
age=int(input("Enter Your age: "))
course=input("Enter your Course: ")
is_attending=True
student=[]
student.append(name)
student.append(age)
student.append(course)
student.append(is_attending)
for item in student:
    print(item)
