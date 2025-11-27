# 1.prime number

# num=int(input("enter a number"))
# for i in range(1,num+1):
#     if i%num ==0:
#         print("prime number",i)
#     else:
#         print("not prime number")


# 2.factorial

# num=int(input("enter a number"))
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(fact)

# 3. print same value in list 


# l1=[10,20,30,40]
# l2=[30,40,50,60]
# for i in l1: 
#     for j in l2:
#         if i ==j:
#             print(j)
            
            
            
# 4.print duplicate values


# l=["apple","banana","apple"]
# coutt=0
# if "apple"== "apple":
#     res=coutt=coutt+1
#     print(res)
    
    
    
age =int (input("enter a number"))
if age >0 and age<=12:
    print("child")
elif age>=13 and age<=19:
    print("teenagar")
elif age >=20 and age<=59:
    print("adult")
else:
    print("senoir citizen")
    
    
    
    
list=["paras","vikas","paras"]
print(list.count("paras"))