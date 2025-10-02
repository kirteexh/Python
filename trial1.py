n_english = int(input("Enter number ="))

# Read roll numbers and convert to a set
english_subs = set(map(int, input("Enter elements =").split()))

# Read the number of students who subscribed to the French newspaper
n_french = int(input("Enter number ="))

# Read roll numbers and convert to a set
french_subs = set(map(int, input("Enter elements =").split()))

# Use set difference to get students who subscribed only to the English newspaper
only_english = english_subs - french_subs  # Same as english_subs.difference(french_subs)

# Print the total number of students who subscribed only to the English newspaper
print(len(only_english))