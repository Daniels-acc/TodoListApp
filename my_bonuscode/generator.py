import datetime

date_today = str(datetime.date.today())
mood_input = int(input("How was your day today from 1-10?: "))
journal = input("Enter your thoughts: \n")

with open(f"journal/{date_today}.txt", 'w') as file:
    file.writelines(f"Your day was: {mood_input} on a scale 1-10.\n")
    file.write(f"Your bookmarks: {journal}.")

