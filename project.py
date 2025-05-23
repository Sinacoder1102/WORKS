from delay_write import delay

namelist = []

while True:
    question = input('Please enter the names. (if the names are enough,press enter) : ')
    namelist.append(question)
    if question == '':
        namelist.pop()
        yes_no = input('Do you want to see the list? (y/n) : ').lower()
        if yes_no in ['y']:
            # delay(str(namelist))
            delay("Names:\n" + "\n".join(f"- {name}" for name in namelist))
            x = input('Do you want to continue ? (y/n) : ').lower()
            if x in ['y']:
                continue
            else:
                break
        else:
            break