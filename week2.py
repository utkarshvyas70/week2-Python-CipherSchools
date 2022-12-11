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