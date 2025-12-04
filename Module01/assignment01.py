# Brandi Butler
# 12/04/2025
# Assignment 1.3 – Countdown Song Program
# This program asks the user for a number and prints the "Bottles of Beer on the Wall" song lyrics, counting down until no bottles remain.

def countdown(bottles):
    # Loop while there are more than 1 bottle
    while bottles > 1:
        # Print the current number of bottles
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles -= 1  # Subtract one bottle
        print(f"Take one down and pass it around, {bottles} bottle(s) of beer on the wall.\n")

    # When there's only one bottle left
    if bottles == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        bottles -= 1
        print("Take one down and pass it around, 0 bottle(s) of beer on the wall.\n")

    # End of the song message
    print("Time to buy more bottles of beer.\n")

def main():
    try:
        # Ask the user how many bottles to start with
        bottles = int(input("Enter number of bottles: "))
        if bottles < 0:
            print("Please enter a non-negative number.")
        else:
            countdown(bottles)
    except ValueError:
        # Handle if user enters something that's not a number
        print("Invalid input. Please enter an integer number.")

# Run the main function when script is executed
if __name__ == "__main__":
    main()

