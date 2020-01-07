username_list = ["John", "Victor", "Kolya", "Sarah", "admin"]
input = input("Username: ")
if (input in username_list):
    if(input == "admin"):
        print(f' Welcome Back {input}. Would you like to see a usage report?')
    else:
        print(f'Welcome Back {input}.')
else:
    print(f'User was not found.')

