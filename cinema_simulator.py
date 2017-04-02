films = {
    "Finding Dory": [3, 5],
    "Bourne": [19, 5],
    "Tarzan": [15, 5],
    "Ghostbusters": [12, 5]
}

choice = ""

while choice != "Exit":
    choice = input("What film do you want to watch ? ").strip().title()

    if choice in films:
        age = int(input("What's your age ? ").strip())
        if age >= films[choice][0]:
            num_seats = films[choice][1]
            if num_seats > 0:
                films[choice][1] = num_seats - 1
                print("Enjoy the film!")
            else:
                print("Sorry, no seats available for {}".format(choice))
        else:
            print("You're too young to see that film!")
    else:
        print("We don't have that film yet!")
