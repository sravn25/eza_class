# age = int(input("Tell me your age: "))
# height = int(input("Tell me your height: "))
# oku = True

# 1. there is another smaller toilet for people below 15 years old
# 2. the smaller toilet is only 150cm tall
# 3. the toilet can only accept people below 30 years old
# 4. the bigger toilet is only 180cm tall
# 5. if someone is older than 30 years old, then ask him go home
# 6. if they are above 30 or OKU, then can go in bigger one

# if age < 15 and height < 150:
#     print("You are allowed to come into the smaller toilet")

# age = int(input("what is your age: "))
#
# if not age:
#     print("tell me your age")
# elif age < 15:
#     print("you are younger than 15")
#     if age > 10:
#         print("But you are big kid")
#     elif age > 5:
#         print("But you are small kid")
#     else:
#         print("You are baby kid")
# elif age > 15 and age < 50:
#     print("You are older than 15")
# elif age > 50 or age == 50:
#     print("you are old")
# else:
#     print("error")
toilet_people = [15, 20, 25, 5, 0, 40, 15, 20, 25, 5, 0, 40]
for age in box_people:
    print(age)

age = 0
while age == 0:
    age = int(input("How old are you"))
    if age == 0:
        print("Please tell me your real age")

# for age in toilet_people:
if age > 15:
    print("Welcome to the bigger toilet")
elif age < 15:
    print("Welcome to the smaller toilet")
else:
    print("You cannot come in")


