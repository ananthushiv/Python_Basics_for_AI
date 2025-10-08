age = 20
if age >= 18:
    print("Eligible to vote.")

if age > 18: print("Eligible to Vote.")

age = 11

if age > 18:
    print("Eligible to Vote.")
else:
    print("Not Eligible to Vote.")


marks = 85
if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'
print("Grade:", grade)

res = "Pass" if marks >= 40 else "Fail"
print(res)
print(f"Grade: {grade}, Result: {res}")


num = 2

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other number")
# --- IGNORE ---
