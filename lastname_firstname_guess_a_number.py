# <PROGRAM NAME>, <AUTHOR>, <DATE> <TIME>, <VERSION>
import ? # What library will allow you to generate random numbers?

num_guess # Initialize this variable to 0.

# Use print() to display a STRING introducing the game.

player_name # Use input() to assign this variable a value.

# Use print() to print a STRING containing player_name.

rand_num = random.randint(x, y) # Replace x and y with integers.  X must be less than Y, and Y must be less than 101. 
# random.randint(x, y) returns a random integer between (and including) x and y.

# Use print() to print a STRING with player_name, explain the program will pick a random number from x to y and number of guesses. 

for num_guess in range(z):
    # Replace z with the number of guess attempts you want the player to have.  If Y is a high number, provide more guess attempts. 
    # This a FOR loop.  It repeats the code below until z guesses OR the player guesses correctly.
    # FOR loops are best used when you know how many times the loop should execute.
    # range() basically counts from 1 to z.
    
    player_guess # Use input() to let the player guess a number.  Make sure to convert it using int()!.

    # You will create an if/elif/else statement on the next lines to check the number.  
    # Check if the player_guess is too low. 
        # Use print() to indicate the guess is too low.
    # Check if the player_guess is too high.  
        # Use print() to indicate the guess is too high.
    # If it's not too high and it's not too low, it must be a match.  What goes here? 
        break # This will exit the for loop on a correct guess.

# After z times through the loop, the loop exits and the code continues to exectute the next statements.  

# Did the player guess the number correctly?
    # INCREMENT num_guess by 1.
    # Use an f-string to print a "win" message and the number of guesses.
# If they did not get the number correct, what goes here?
    # Use an f-string to print a "loss" message and the number to be guessed.
    
# Version 0.1 should have the correct import statement.
# Version 0.2 should correctly initialize num_guess and print() the introduction.
# Version 0.3 should correctly get the player_name from the player.
# Version 0.4 should have X and Y defined for rand_num = random.randint(x, y)
# Version 0.5 should print() the STRING with player_name, explain the range of numbers, and the number of guesses allowed.
# Version 0.6 should replace z in range(z) with the number of guess attempts.
# Version 0.7 should use input() to allow the player to guess a number.
# Version 0.8 should complete the if/elif/else statements to check if guess is too high, too low, or a match.
# Version 0.9 should complete the if/elif/else to print a "win" or "loss" message based on the guess.
# Version 1.0 should be the completed program, free of syntax and logic errors.  
