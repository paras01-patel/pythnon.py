# # # tpyes of user define function 



# # # 1 . on thee basis arguument
# # # 2. on the basis of argument and return type 




# # # 1 . on thee basis arguument


# # # a.Positional argument

# # # example

# # # 1.add two number


# # def add(a,b):
# #     print(a+b)
# # add(5,10)

# # # 2.subtraction

# # def sub (a,b):
# #     print(a-b)
# # sub(10,5)

# # # 3.student information

# # def student(name,age):
# #     print(name, age)
# # student("paras",20)


# # # 4.area of reactangle

# # def area(length,width):
# #     print(length*width)
# # area(10,10)

# # # 5.full name print

# # def full_name(first,last):
# #     print(first+last)
# # full_name("paras","chandrawanshi")


# # # 6.mutiple three number

# # def mul(a,b,c):
# #     print(a*b*c)
# # mul(2,4,5)

# # # 7.slow city and country

# # def cou(city,country):
# #     print(city,country)
# # cou("bhopal","india")

# # # 8.power calculation

# # def power(a,b):
# #     print(a ** b)
# # power(5,3)


# # # 9.mark display

# # def mark(math,science,hindi):
# #     print("math",math)
# #     print("science",science)
# #     print("hindi",hindi)
# # mark(50,100,500)



# # b.defealt posiotional argrument

# #1. defealt name

# def greet(name="Guest"):
#     print("Hello", name)

# # greet()
# greet("Paras")



# # 2. defelt b


# def add(a, b=10):
#     print(a + b)

# add(5)
# add(5, 20)


# # 3.defualt city


# def info(name, city="Bhopal"):
#     print(name, "from", city)

# info("Paras")
# info("Aman", "Indore")

# # 4.default item 


# def show(price, item="Pen"):
#     print(item, "=", price)

# show(50)
# show(150, "Notebook")


# # 5.default a and b 

# def sub(a=10, b=5):
#     print(a - b)

# sub()
# sub(20)
# sub(20, 3)







# # c. variable length argument



# #  Basic Example:
# def show(*args):
#     print(args)

# show(1, 2, 3)
# show(10)
# show(5, 6, 7, 8, 9)


#                                     #   Output hamesha tuple me aata hai.

# #  Example 2: Sum of All Numbers
# def add_all(*args):
#     print(sum(args))

# add_all(1, 2, 3)
# add_all(10, 20)

# #  Example 3: Names List
# def students(*args):
#     for name in args:
#         print(name)

# students("Paras", "Aman", "Rohit")

# #  Example 4: Find Maximum
# def find_max(*args):
#     print(max(args))

# find_max(10, 4, 22, 7)

# #  Example 5: Mixed Values
# def info(*args):
#     print("Total items:", len(args))
#     print(args)

# info("Paras", 20, "Bhopal", 90)

# # Example 6: Product of Numbers
# def multiply(*args):
#     m = 1
#     for x in args:
#         m *= x
#     print(m)

# multiply(2, 3, 4)

# # Example 7: Show Even Numbers
# def even_numbers(*args):
#     for n in args:
#         if n % 2 == 0:
#             print(n)

# even_numbers(1,2,3,4,5,6)

# # Example 8: Item Counter
# def count_items(*args):
#     print("Items:", len(args))

# count_items(10, 20, 30, 40)

# #  Example 9: Print in Reverse
# def reverse_args(*args):
#     print(args[::-1])

# reverse_args(1, 2, 3, 4)

# # Example 10: First & Last Value
# def first_last(*args):
#     print("First:", args[0])
#     print("Last:", args[-1])

# first_last(10, 20, 30, 40)




# d.  variable length keyword argument (**args)




# #  Combine *args and kwargs
# def demo(*args, **kwargs):
#     print("Args:", args)
#     print("Kwargs:", kwargs)

# demo(1, 2, 3, name="Paras", age=20)


# # 2 Each Key-Value Print
# def info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, "=", value)

# info(id=101, branch="CSE", year=2)


# # Basic Example


# def show(**kwargs):
#     print(kwargs)

# show(name="Paras", age=20, city="Bhopal")










# 2.on the basis of arugument & return type 



# a.with argument and with return type 


# 1.add two number

# def sum(a,b):
#     return a+b
# print(sum(10,20))


# 2.sub

# def sub(a,b):
#     return a-b
# c=sub(10,5)
# print(c)


# 3.multiple 

# def multiple(a,b):
#     return a*b
# print(multiple(5,5))


# 4. even and odd 

# def evenodd(n):
#     if n%2==0:
#         return "even"
#     return "odd"
# print(evenodd(5))


# 5.sqare od a number

# def sqare(n):
#     return n*n
# print(sqare(5))


