''' list:= 
# 1.collection of element
# 2.represented [] with comma(,)
3.indexing supported
4.slining supported
5.duplicate are allowed
6.mutable are allowed


in buiuld function 

l = [10, 20, 0, 5]

print(len(l))        # 1. length of list
print(min(l))        # 2. smallest value
print(max(l))        # 3. largest value
print(sum(l))        # 4. sum of all elements
print(sorted(l))     # 5. returns new sorted list
print(list("abc"))   # 6. converts iterable to list
print(any(l))        # 7. True if any element is True
print(all(l))        # 8. True only if all are True
print(list(enumerate(l)))   # 9. index + value pairs
print(list(reversed(l)))    # 10. reversed list




method in list 


append() – list ke end me element add karta hai

insert() – kisi specific index par element lagata hai

extend() – ek list ko dusri list me jod deta hai

remove() – kisi specific element ko hata deta hai

pop() – index se element nikalta hai (default last)

clear() – poori list ko khali kar deta hai

sort() – list ko ascending order me sort karta hai

reverse() – list ko ulta kar deta hai (reverse order)

count() – element kitni baar aaya, uska count deta hai

index() – element ka index number batata hai

copy() – list ki shallow copy banata hai



'''

# methods in list 


# 1.append()


# l=[1,2,3,4,5]
# l.append(4)
# print(l)


# 2.insert() indexing ke hisab se insert karta hai

# l=[1,2,3,4,5]
# l.insert(2,15)
# print(l)


# 3.extend()  = ek list ko dusri list me add karta hai with the help of [ ]

# l=[1,2,3,4,5]
# l.extend([1,3464,45,4,6,6,43,])
# print(l)


# 4.remove()

# l=[2,3,4,5]
# l.remove(2)
# print(l)


# 5.prp = indexing ke hisab se kam karta hai 

# l=["paras ","vikas","jatin","sujal","raj"]
# l.pop(0)
# print(l)


# 5.clear()

# l=[1,2,3,4,5]
# l.clear()
# print(l)


# 6.indexing() =indexing hamesha 0 se start hoti hai 



# l=[1,2,3,4,5,6]
# print(l.index(2))


# 7.count()=count kitna hai ki kitne harr element aaya hai 

# l=[1,2,3,4,5,5,5,5]
# res=l.count(5)
# print(res)


# 8.sort() =assending order me deta hai 

# l=[2,24,424,4,4,21,34,34]
# l.sort()
# print(l)


# 9.reverse()=sare elments ko ulta kar dete haai

# l=[324,43,34,2334,545,4352,234,5235,4]
# l.reverse()
# print(l)


# 10.copy()=ek new list banti hai 

# l=["paras","aakash","ajay","udit","prem"]
# l1=l.copy()
# print(l1)
# print(l)












# 1) List me se maximum number find karo without max

# l=[2,3,4,4,56,6,7]
# max=l[0]
# for i in l:
#     if i> max:
#         max=i
# print(max)
        
    
    # with max 
    
       
# l=[223,224,24,22,2]
# res=max(l)
# print(res)

# 2. minimum without manimum 

# l=[4,3,32,2,2334,223]
# l1=l[0]
# for i in l:
#     if i < l1:
#         li=i
# print(li)

# with minimum 

# l=[12,3,3,3,23436,6,565474,44,4]
# print(min(l))



#3. print even number


# l=[1,2,3,4,5,6,7,8,9,10]
# for i in l:
#     if i %2==0:
#         print("even nummber", i)


# 4.print odd nunber


# l=[12,3,2,42,4,5,5,3]
# for i in l:
#     if i % 2 !=0:
#         print("odd",i)

# 5.sum all the number

# l=[1,2,3,4,5]
# sum=0
# for i in l:
#     sum+=i
# print(sum)


# 6. lsit ka average find karo 

# l=[1,2,4,4,5,6,4,43]
# total=0
# for i in l:
#     total+=i
# avg=total/len(l)
# print(avg)


# 7.reverse in list without reverse()

# l=[1,2,3,4,5,6,7]
# rev=[]
# for  i in range(len(l)-1,-1,-1):
#     rev.append(l[i])
# print(rev)


# with reverse 

# l=[1,2,3,4,5,6,7]
# l.reverse()
# print(l)


# 8. present number

# l=[1,2,3,4,555]
# n=555
# if n in l:
#     print("presnt")
# else:
#     ("not present")

# 9. second largest number

# l = [1, 2, 3, 4, 5, 6]
# largest = max(l)
# l.remove(largest)

# print(max(l))



