
with open("Input/Letters/starting_letter.txt", "r") as main_file:
    main_list = main_file.read()
with open("Input/Names/invited_names.txt", "r") as names_file:
    names_list = names_file.readlines()
    for names in names_list:
        stripped_names = names.strip()
        new_list = main_list.replace("[name]", stripped_names)
        with open(f"Output/ReadyToSend/letter_for_{stripped_names}.txt", "w") as file:
            y = file.write(f"{new_list}")