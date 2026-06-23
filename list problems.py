num=[12,13,14,78,80]
print('sum of the list:\n')
sum=0

for i in num:
    sum=sum+i
print(sum)

print('max of the list:\n')

print(max(num))

# max=lst[i]
#for i in num:
#     if i>max:
#         max=i
#print(max)

print('min of the list:\n')
print(min(num))

# min=lst[i]
#for i in num:
#     if i<min:
#         min=i
#print(max)

print('count the elements:')
count=0
for i in num:
    if i%2 ==0:
        count+=1
print(count)

no=list(filter(lambda a: a%2==0,num))
print(num,no)

print('average of list:')
for i in num:
    sum=sum+i
avg=sum/len(num)
print(avg)
print('fact of a num:')
noe=int(input('enter the no:'))
fact=1
for i in range(1,noe+1):
    fact=fact*i
print(fact)

print('prime no:/n')
n=int(input('enter the no'))
if n<=1:
    print('not prime')
else:
    for i in range(2,n):
        if n%i==0:
            print('not prime')
            break
        else:
            print('prime')
s=input('enter the string:')
rev=" "
for i in s:
    rev=i+rev
print(rev)

si=input('enter the string')
rev= ""
for i in si:
    rev=i+rev

if si==rev:
    print('it is a palindrome')
else:
    print('not a palindrome')

ni=[1,2,3,3,4,1,2,4,5]
new=[]
for i in ni:
    if i not in new:
        new.append(i)
print(new)

ne=[11,12,13,14,15]
first=ne[0]
second=ne[0]
for i in ne:
    if i>first:
        first=i
    elif i>second and i!=first:
        second=i
            
print(first)
print(second)

s1=input('enter the no:')
s2=input('enter the no:')
if sorted(s1)==sorted(s2):
    print('it is sorted')
else:
    print('NOT SOTRED')

n=input('enter the string:')
count=0
for i in n.lower():
    if i in 'aeiou':
        count+=1
print(count)

lst = [10, 15, 20, 25, 30, 35]
odd = []

for i in lst:
    if i % 2 != 0:
        odd.append(i)

print("Original List:", lst)
print("Odd Numbers:", odd)

lst = [1, 2, 3, 4, 5]
rev = []

for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])

print("Original List:", lst)
print("Reversed List:", rev)

lst = [1, 2, 3]
num = ""

for i in lst:
    num += str(i)

print("Single Integer =", int(num))

no=int(input('enter the no:'))
binary=""
while no>0:
    rev=no%2
    binary=str(rev)+binary
    no=no//2
print(binary)

n=[1,2,3,4,5]
a=[4,5,6,7,8]
new=[]
for i in n:
    if i in a:
        new.append(i)
print(new)

n=['banana','apple','strawberry','mango']

for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]>n[j]:
            n[i],n[j]=n[j],n[i]
        
print(n)

rev=""
n=input('enter the no:')

for i in n:
    if i!=" ":
        rev=rev+i
print(rev)
        



    





  
        
         


    


