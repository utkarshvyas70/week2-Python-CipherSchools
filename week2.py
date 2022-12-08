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