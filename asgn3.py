print('Question 1\n')

input_string = input('Enter input string: ')
input_string = input_string.lower().strip()
words = {}

if ' ' in input_string:
    input_string = input_string.split()

for word in input_string:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

for k, v in words.items():
    print(f"{k}:{v} ")
    
    
    
##########################################################################################################################    



print('Question 2')

def leap_year(year: int):                                                                            
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
while True:
    date = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))
    #removing wrong input
    if (date < 1) or (date > 31) or (month < 1) or (month > 12) or (year < 1800) or (year > 2025):               
        print("Please use the given conditions for entering the current date\nC1 : 1<=month<=12\nC2 : 1<=day<=31\nC3 : 1800<=year<=2025")
        continue
    if month in (4,6,9,11) and date == 31:
        print("The given month has only 30 days\nPlease enter a valid date")
        continue
    elif month == 2 and date >= 29: #Condition for no. of days in February
        if leap_year(year) and date != 29:
            print("The given month has only 29 days\nPlease enter a valid date")
            continue
        elif not leap_year(year):
            print("The given month has only 28 days\nPlease enter a valid date")
            continue
    break

#fixing the total number of days in a month
if month == 2:
    if leap_year(year):
        max_days = 29
    else:
        max_days = 28
elif month in [4,6,9,11] :
    max_days = 30
else:
    max_days = 31
    
#incrementing the date
if date == max_days:
    date = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
else:
    date += 1
print(f"Next Date is: {date}/{month}/{year}")




##########################################################################################################################    



print('Qustion 3')

list = [3, 7, 9, 10]
output_list = []
for number in list:
    output_list.append((number, number**2))
print(output_list)



##########################################################################################################################    



print('Question 4')
grade_points = int(input('Enter Grade Points: '))
if 3 < grade_points < 11:
    # creating a nested dictionery of the given data
    dict = {
        4: {'Performance': 'Poor', 'Letter Grade': 'D'},
        5: {'Performance': 'Below Average', 'Letter Grade': 'C'},
        6: {'Performance': 'Average', 'Letter Grade': 'C+'},
        7: {'Performance': 'Good', 'Letter Grade': 'B'},
        8: {'Performance': 'Very Good', 'Letter Grade': 'B+'},
        9: {'Performance': 'Excellent', 'Letter Grade': 'A'},
        10: {'Performance': 'Outstanding', 'Letter Grade': 'A+'}
    }
    # getting the required data based on grade points
    sub_dict = dict[grade_points]
    print(
        f"Your Grade is {sub_dict['Letter Grade']} and {sub_dict['Performance']} performance ")
else:
    print('Error! (Grade Points must be between 4 and 10)')

    
  
##########################################################################################################################    
  
  
    
print('Question 5')

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
row = 1
space = ''
while row <= 6:
    for letters in alphabets:
        print(letters, end='')
    # To go to the next row.
    print('')
    # Slicing the list to remove last 2 alphabets.
    alphabets = alphabets[:-2]
    # Increasing the row counter for the while loop.
    row += 1
    # Print spaces on the left side of letters.
    space += ' '
    print(space, end='')

    
    
 ##########################################################################################################################    
    
    
    print('Question 6')

dictionery = {}
# setting a flag for the input prompt
flag = True
prompt = "y"
while flag:
    if prompt.lower() == "y":
        SID = int(input("Please Enter SID of Student: "))
        name = input("Please enter the name of the Student: ")
        dictionery[SID] = name
        prompt = input("If you want to enter more details press Y/N- ")
        flag = True

    else:
        flag = False

print("Part a")
for k, v in dictionery.items():
    print(f"SID {k} is of {v}\n")

print("Part b")
name_sort_dict = sorted(dictionery.values())
print(f"value sorted dictionary is {name_sort_dict}\n")

print("Part c")
sid_sort_dict = sorted(dictionery.keys())
print(f"Keys sorted dictionary is {sid_sort_dict}\n")

print("Part D")
int_sid = int(input("Please enter the student's SID whose detail you need- "))
if int_sid in dictionery.keys():
    print(f"Name of the required student is {dictionery[int_sid]}")
else:
    print("The SID is not present in the given Data")

    
    
##########################################################################################################################    
    
    
    
    print("Question 7")

a = 1
b = 1
sum = 0
input = int(input('Enter no. of terms: '))
print(f"The Fibonacci sequence upto {input} terms is: ")
print(a, end=",")
for i in range(1, input):
    sum += b
    print(b, end=",")
    c = a + b
    a = b
    b = c
print("\nThe average of the terms of Fibonacci sequence for %d terms is %0.2f" %
      (input, sum/input))




##########################################################################################################################    





print('Question 8')

set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}
print("(a)", set1 ^ set2, '\n')

print("(b)", set1 ^ set2 ^ set3, '\n')

print("(c)", (set1 | set2 | set3) - (set1 ^ set2 ^ set3) - (set1 & set2 & set3), '\n')

set4 = set()
for n in range(1, 11):
    if n not in set1:
        set4.add(n)
print("(d)", set4, '\n')

print("(e)", set(range(1, 11)) - (set1 | set2 | set3), '\n')

    
    
    
