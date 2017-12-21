#  Guessing Game - Topic 3.5

debug=False                                     # Debug Flag

smallest=1                                      # Lower Limit
largest=100                                     # Upper Limit
guess_number=0                                  # Lopp counter of the number of times through
found_it=False;                                 # Set to true when the number is found
print("Think of a number between 1 and 100")
while not(found_it):
    guess = (smallest + largest) / 2            # We'll guess in the middle.
    if smallest > largest:                      # If the Lower limit is ever greater than the upper limit, then error
        print("You're fibbing!!")
        break                                   # We're outta here
    guess_number = guess_number+1               # bump the loop counter and prompt the user for an answer
    answer=raw_input("Is your number 'more' or 'less' or 'equal' to " + str(guess) +"? ")
    if answer == "more":                        # If we're low then make the new lower limit equal to one more
                                                # than the previous
        smallest = guess + 1
    elif answer == "less":                      # If we're high then make the new upper limit equal to one less
                                                # than the previous
        largest = guess - 1
    elif answer == "equal":                     # We're there - set the exit flag to true
        found_it=True
        print("Found it in " + str(guess_number) + " tries.")           # Tell them how many times through and
                                                                        # leave the loop.
        break
    if debug:
        print(smallest, largest)
pass
