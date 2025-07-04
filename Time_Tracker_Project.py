# Welcome Msg #
user = input("Name: ")

# Input time spent on each activity (in hours) #
print(f"{user}! Time Tracker")
Study = float(input("Study: "))
Exercise = float(input("Exercise: "))
Gaming = float(input("Gaming: "))
Leisure = float(input("Leisure: "))

# Summary of the input #
print(f"\n{user}! Today's Time Spent")
print(f"Time Spent on Studying: {Study} Hours")
print(f"Time Spent in Gym: {Exercise} Hours")
print(f"Time Spent on Gaming: {Gaming} Hours")
print(f"Time Spent on Leisure: {Leisure} Hours")

# Total time tracked #
total = Study + Exercise + Gaming + Leisure
print(f"Total Time Tracked: {total} Hours")