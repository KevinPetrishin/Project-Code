print("Hello, and welcome to whatever this project is")
name = input("Please enter your name: ")

age = int(input("Hello {}. Please state your age: ".format(name)))
if age < 18:
    print("I am very sorry {}, but you have to be 18 or older to use this useless project".format(name))
else:
    print("Are you really {}? (yes or no)".format(age))
    real_age = input()
    if real_age == 'yes':
        print("Ok, I believe you")
    elif real_age == 'no':
        print("How dare you lie to me?")
    else:
        print("That's not an answer. Please enter either: yes or no.")
