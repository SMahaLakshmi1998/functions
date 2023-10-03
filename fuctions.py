# users_List=[]
# user=int(input("Enter no of users: "))

# for i in range(user):

#   name,age,email=input("Enter name, age, email: ").split()

#   def func1():
#     userList=list((name,age,email))
#     return userList

#   a=func1()

#   def func2():
#     user_dict={}
#     user_dict.update({"Name":a[0]})
#     user_dict.update({"Age":a[1]})
#     user_dict.update({"Email":a[2]})
#     return user_dict

#   b=func2()

#   def func3():
#     mobileNo=input("Enter mobile No: ")
#     mobile_dict={}
#     mobile_dict.update({"mobile_No":mobileNo})
#     return mobile_dict

#   c=func3()

#   def func4():
#     mobile2=input("Enter mobile number to change: ")
#     c.update({"mobile_No":mobile2})
#     b["Mobile_No"]=mobile2
#     users_List.append(b)
    
#   func4()    


# print(users_List)


user=[]
user=int(input("Enter the number of users:"))
for i in range(user):


    name=input("Enter the name:")
    age=input("Enter the age:")
    email=input("Enter the emai id:")
    def hello1():
        list1=(name,email,age)
        return list1
    a=hello1()

    def hello2():
        s={}
        s={"Name":name,"email":email,"Age":age}
        return s
    b=hello2

    def hello3():
        mob=input("Enter the mobile number:")
        mobile={}
        mobile.update({"Mobileno":mob})
        return mobile
    c=hello3()

    def hello4():
        
        newnbr=input("Enter the new mobile number:")
        c.update({"newnumber":newnbr})
        b["Mobile number2:"]=newnbr
        user.append(b)
    hello4()
print(user)







        


