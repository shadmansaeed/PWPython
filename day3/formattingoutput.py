# name="John"
# age=30
# sal=50000.50

name,age,sal="john",30,50000.50

# Approach1
print(name,age,sal)


# Approach2
# Name is: John
# Age is: 30
# Salary is: 50000.50

print("Name is:" +name) # valid because these two are string
#print("Age is:" + age) #not valid
print("Age is:",age) # , is valid for all these cases
print("Salary is:",sal)

# Approach3
#  %s--> string   %d-->numeric    %g=decimal

# print("Name:%s  Age:%d  Salary:%g " %(name,age,sal))    #This is hard, i am not using this in future
# print("Age:%d  Name:%s  Salary:%g " %(age,name,sal))
#
# # Approach 4   {}  format()
# print("Name:{} Age:{} salary:{}".format(name,age,sal))

# Approach 4   {}  format()
print("Name:{0} Age:{1} salary:{2}".format(name,age,sal))
print("Salary:{2} Name:{0} Age:{1}".format(name,age,sal))

print("welcome to \n python")  # new line

print("welcome\t to python")  # Tab space

