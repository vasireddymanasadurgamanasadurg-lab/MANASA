'''
#NESTED IF

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
else:
    if marks >= 75:
        print("Grade B")
    else:
        if marks >= 60:
            print("Grade C")
        else:
            print("Fail")
'''
'MATCH CASE'

choice = int(input("Enter a number (1-7): "))

match choice:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid choice")

