username_list = ["John", "Victor", "Kolya", "Sarah", "admin"]
input = input("Username: ")
if (input in username_list):
    if(input == "admin"):
        printf(f’ Welcome Back{input}. Would you like to see a usage report?')
    else:
        printf(f'Welcome Back{input}.')
else:
printf(f'User wasn't found.')

