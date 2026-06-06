import random
import string

def generate_random_text(length=100, include_digits=False, include_punctuation=False):
    """
    Generates a random text string of specified length.

    Args:
        length (int): The length of the text to generate. Defaults to 100.
        include_digits (bool): Whether to include digits in the text. Defaults to False.
        include_punctuation (bool): Whether to include punctuation in the text. Defaults to False.

    Returns:
        str: A random text string of the specified length.
    """

    # Define the base character set (lowercase and uppercase letters)
    chars = string.ascii_letters

    # Add digits to the character set if required
    if include_digits:
        chars += string.digits

    # Add punctuation to the character set if required
    if include_punctuation:
        chars += string.punctuation

    # Generate the random text by choosing characters randomly from the character set
    random_text = ''.join(random.choice(chars) for _ in range(length))

    return random_text

def main():
    """
    Main function to generate and print random text.
    """
    try:
        # Get user input for text length
        length = int(input("Enter the length of the text to generate (default is 100): ") or 100)
        
        # Get user input for including digits
        include_digits = input("Include digits? (y/n, default is n): ").strip().lower() == 'y'
        
        # Get user input for including punctuation
        include_punctuation = input("Include punctuation? (y/n, default is n): ").strip().lower() == 'y'
        
        # Generate and print the random text
        random_text = generate_random_text(length, include_digits, include_punctuation)
        print("\nGenerated Random Text:")
        print(random_text)
    
    except ValueError:
        print("Invalid input. Please enter a valid number for text length.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()