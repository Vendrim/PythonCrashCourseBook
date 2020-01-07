current_users = ["john", "sally", "victor", "eric", "kolya", "rodney"]
new_users = ["John", "Rodney", "Wallace", "Randal", "Larry"]
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
if new_users: 
    name_not_available = True
    for user in new_users:
        name_not_available = user.lower() in current_users_lower

if name_not_available :
    print(f'New Username please!:')
else:
    print(f'Current Username is available.')