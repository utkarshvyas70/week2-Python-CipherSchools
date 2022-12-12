#video 63
total=0
for i in range(1,21):
    total+=i
print(total)

n=int(input())
total=0
for i in range(1,n+1):
    total+=i
print(i)

#video 64
total=0
num=input("enter a number: ")
for i in range(0,len(num)):
    total+=int(num[i])
print(total)

#video 65
name=input()
temp=''
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp+=name[i]

#video 66
for i in range(1,11):
    if i==5:
        break
    print(i)

for i in range(1,11):
    if i ==5:
        continue
    print(i)

#video 67 excercise
winning_num=43
guess=1
number=int(input("guess 1 to 100: "))
game_over=False
while not game_over:
    if number==winning_num:
        print(f"win in {guess} times")
        game_over=True
    else:
        if number<winning_num:
            print('too low')
            guess+=1
            number=int(input("again:"))
        else:
            print('too high')
            guess+=1
            number=int(input("again: "))

#video 69
import random
winning_num=random.randint(1,100)
guess=1
number=int(input("guess 1 to 100: "))
game_over=False
while not game_over:
    if number==winning_num:
        print(f"win in {guess} times")
        game_over=True
    else:
        if number<winning_num:
            print('too low')
            guess+=1
            number=int(input("again:"))
        else:
            print('too high')
            guess+=1
            number=int(input("again: "))

#video 70
for i in range(1,-11,-1):
    print(i)

#video 71
name2='harshit'
for i in range(len(name2)):
    print(name[i])

name2='harshit'
for i in 'mohit':
    print(i)

num=input('enter: ')
total=0
for i in num:
    total+=int(i)
print(total)

#video 73
def add_two(num1,num2):
    return num1+num2
first_name=input('type first name')
last_name=input('type last name')
print(add_two(first_name,last_name))

#video 74
def add_three(a,b,c):
    return a+b+c
add_three(5,5,5)

#video 75
def last_char(name):
    return name[-1]
print(last_char("Utkarsh vyas"))
last_char(9)

def odd_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"

#video 76
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"calling {number}"

class Smartphone(Phone):
    def __init__(self,brand,model_name, price, ram, internal_memory, rear_camera):
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.internal_memory = internal_memory
        self.rear_camera=rear_camera
#video 77
def greater(a,b):
    if a > b:
        return a
    else:
        return b
num1=int(input("Enter first number "))
num2=int(input("Enter second number "))
bigger = greater(num1,num2)

print(f"{bigger} is greater")

#video 78 and video 79
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(greatest(100,40,30))

def new_greates(a,b,c):
    bigger=greater(a,b)
    return greater(bigger,c)
print(new_greates(1000,200,30))

# video 81 excercise
def is_palindrom(word):
    return word == word[::-1]
print(is_palindrom("naman"))
print(is_palindrom("horse"))

#video 82
def fibonacci_seq(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a, b)
    else:
        print(a,b,end=" ")
        for i in range(n-2):
            c= a+b
            a=b
            b=c
            print(b,end=" ")
fibonacci_seq(20)

#video 83
def user_info(first_name = 'unknown' , last_name='unknown', age=None):
    print(f"Your first name is {first_name}")
    print(f"Your last name is {last_name}")
    print(f"Your age is {age}")
user_info()

#video 84
x=5
def func():
    global x
    x=7
    return x

print(x)
print(func())
print(x)

#video 85
numbers=[1,2,3,4]
print(numbers[1])

word=["word1", "word2", "word3"]
print(word[:2])

mixed=[1,2,3,4,"five","six",2.3,None]
print(mixed[-1])

mixed[1:]=["three","four"]
print(mixed)

#video 86
fruits=[]
fruits.append("mango")
fruits.append("grapes")
print(fruits)

#video 87
fruits1=['mango','orange']
fruits2=['grapes','apple']
fruits=fruits1+fruits2
fruits1.extend(fruits2)
fruits1.append(fruits2)
print(fruits1)
print(fruits2)

#video 88
fruits=['orange', 'apple', 'pear','banana','apple','kiwi']
fruits.remove('apple')
print(fruits)

#video 89
fruits=['orange','apple','pear','banana','kiwi']
if 'mango' in fruits:
    print("mango is present")
else:
    print("not present")

#video 90
fruits=['orange','apple','pear','banana','kiwi','apple']
numbers=[3,5,1]
numbers_copy = numbers.copy()
print(num)

#video 91
fruits1=['orange','apple','pear']
fruits3=['orange','apple','pear']
fruits2=['banana','kiwi','apple','banana']
print(fruits1==fruits3)
print(fruits1 is fruits3)

#video 92
user_info=['harshit','24']
print(','.join(user_info))

#video 94
s='string'
l=['word1','word2','word3']
l.append('word3')
print(l)

#video 95
fruits=['orange','apple','pear','banana']
for fruit in fruits:
    print(fruit)

i=0
while i < len(fruits):
    print(fruits[i])
    i+=1

#video 96
matrix=[[1,2,3],[4,5,6],[7,8,9]]
for sublist in matrix:
    for i in sublist:
        print(i)

s='string'
print(type(s))
print(type(matrix))

#video 97
numbers= [1,2,3,4,5,6,7,8,9,10]
def negative_list(1):
    negative=[]
    for i in l:
        negative.append()

#video 99
def square_list(1):
    square=[]
    for i in l:
        square.append(i**2)
    return square

numbers=list(range(1,11))
print(square_list(numbers))

#video 101
def reverse_list(1):
    r_list=[]
    for i in range(1,len(1)+1):
        popped_item=l.pop()

numbers=[1,2,3,4]
print(reverse_list(numbers))

#video 103
def reverse_elements(1):
    elements=[]
    for i in l:
        elements.append(i[::-1])
    return elements

words=['abc','tuv','xyz']
print(reverse_elements(words))

#video 105
def filter_odd_even(1):
    odd_nums=[]
    even_nums=[]
    for i in l:
        if i%2==0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    output=[odd_nums,even_nums]
    return output
num=[1,2,3,4,5,6,7]
filter_odd_even(num)

#video 107
def common_finder(l1,l2):
    output=[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output

common_finder([1,2,5,8],[1,2,7,6])

#video 108
numbers=[6,60,2]
print(min(numbers))
print(max(numbers))

def greatest_duff(1):
    return max(1)-min(1)
print(greatest_duff(numbers))

#video 110
def sublist_counter(1):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count

mixed=[1,2,3,[1,2]]
print(sublist_counter(mixed))

#video 112
ex=('one','two','three')
ex[0]=1
print(ex)

#video 113
fav=('southern magnolia',['tokyo ghoul theme','landscape'])
fav[1].pop()
fav[1].append('we made it')
print()

#video 114
def func(int1,int2):
    add=int1+int2
    multiply=int1*int2
    return add,multiply
add,multiply=func(2,3)
print(add)
print(multiply)

#video 115
num=str((1,2,3,4,5,6,7,8,9,10))
num_list=str([1,2,3,4,5,6,7,8,9,10])
print(num_list)
print(type(num_list))

