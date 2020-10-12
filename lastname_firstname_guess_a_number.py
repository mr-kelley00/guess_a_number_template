# <PROGRAM NAME>, <AUTHOR>, <DATE> <TIME>, <VERSION>
import ? # What library will allow you to generate random numbers?

num_guess # Initialize this variable to 0.

print("Let's play Guess the Number!\n")
player_name # Use input() to assign this variable a value.

# Use print() to print a STRING containing player_name.

rand_num = random.randint(1, 20) 
# random.randint(x, y) returns a random integer between (and including) x and y.

# Use print() to print a STRING containing player_name that explains the program will pick a random number from 1 to 20.

for num_guess in range(z): # Replace z with the number of guess attempts you want the player to have.
    # This a FOR loop.  It repeats the code below until z guesses OR the player guesses correctly.
    # FOR loops are best used when you know how many times the loop should execute. 
    player_guess # Use input() to let the player guess a number.  Make sure to convert it using int()!.

    if VARIABLE1 ? VARIABLE2: # Check if the player_guess is too low. 
        # Use print to indicate the guess is too low.

    if VARIABLE1 ? VARIABLE2: # Check if the player_guess is too high.  
        # Use print to indicate the guess is too high.

    if VARIABLE1 ? VARIABLE2: # Check if player_guess is equal to the random number.  
        break # This will exit the for loop on a correct guess. 

if VARIABLE1 ? VARIABLE2: # Did the player guess the number correctly?
    num_guess ? 1 # INCREMENT the number of guesses by 1.
    print(f"...") # Use an f-string to print a "win" message and the number of guesses.
# If they did not get the number correct, what goes here?
    print(f"...") # Use an f-string to print a "loss" message and the number to be guessed.
    
