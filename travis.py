known_users = ["Alice", "Bob", "Claire", "Emma", "Robert"]

print(len(known_users))

name = ""

while name != "Exit":
    print("Hi, My name is Travis, type Exit to quit")
    name = input("What's your name ? ").strip().capitalize()
    if name in known_users:
        print("Hello, {}!".format(name))
        remove = input("Would you like to be removed from system (y/n)? ").strip().lower()
        if remove == 'y':
            known_users.remove(name)
    else:
        add = input("Would you like to be added to system (y/n)? ").string().lower()
        if add == 'y':
            known_users.append(name)