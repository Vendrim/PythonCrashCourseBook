username_list = []
username_list2 = ["John", "Victor", "Kolya", "Sarah", "admin"]
if username_list:
    print(f'We need to find some Users!')
    input = input("Username: ")
    if (input in username_list):
        if(input == "admin"):
            print(f' Welcome Back {input}. Would you like to see a usage report?')
        else:
            print(f'Welcome Back {input}. Enjoy your Session.')
    else:
        print(f'User was not found.')
else:
    print(f"There are no Users in our Database!")
