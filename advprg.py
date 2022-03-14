import random
i = 0
num_list = []
while i <6:
    number = int(input("Enter number: "))
    num_list.append(number)
    i += 1

even_number = []
for num in num_list:
    if num%2 == 0:
        even_number.append(num)

print("Even numbers: ", end = '\t')
print(*even_number, sep=', ')

i = 0
print("Numbers generated: ")
num_0 = []
num_1 = []
num_2 = []
num_3 = []
num_4 = []
num_5 = []
num_6 = []
num_7 = []
num_8 = []
num_9 = []
while i <20:
    ran_number = random.randint(0,9)
    if ran_number == 0:
        num_0.append(ran_number)
    elif ran_number == 1:
        num_1.append(ran_number)
    elif ran_number == 2:
        num_2.append(ran_number)
    elif ran_number == 3:
        num_3.append(ran_number)
    elif ran_number == 4:
        num_4.append(ran_number)
    elif ran_number == 5:
        num_5.append(ran_number)
    elif ran_number == 6:
        num_6.append(ran_number)
    elif ran_number == 7:
        num_7.append(ran_number)
    elif ran_number == 8:
        num_8.append(ran_number)
    elif ran_number == 9:
        num_9.append(ran_number)

    print(ran_number)
    i += 1

print("Number of 0's: ",len(num_0))
print("Number of 1's: ",len(num_1))
print("Number of 2's: ",len(num_2))
print("Number of 3's: ",len(num_3))
print("Number of 4's: ",len(num_4))
print("Number of 5's: ",len(num_5))
print("Number of 6's: ",len(num_6))
print("Number of 7's: ",\
      len(num_7))
print("Number of 8's: ",len(num_8))
print("Number of 9's: ",len(num_9))
