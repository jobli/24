breakfast_special = "Texas Omelet"
breakfast_notes = "Contains brisket"
lunch_special = "Greek patty melt"
lunch_notes = "Like the regular one, but with different sauce"
dinner_special = "Buffalo steak"
dinner_notes = "Top loin with hot sauce"

meal_time = raw_input("Which mealtime do you want? [breakfast, lunch, dinner] ")
meal_time = meal_time.strip()
meal_time = meal_time.lower()
print "Specials for {}:".format(meal_time)
if meal_time == "breakfast":
    print breakfast_special
    print breakfast_notes
elif meal_time == "lunch":
    print lunch_special
    print lunch_notes
elif meal_time == "dinner":
    print dinner_special
    print dinner_notes
else:
    print "Sorry, {} is not valid.".format(meal_time)
