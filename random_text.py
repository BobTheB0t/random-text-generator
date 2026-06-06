import random
import string

def generate_random_text(length=10, use_digits=True, use_punctuation=True):
    """
    Generates a random text string of specified length.

    Args:
        length (int): The length of the text to generate. Defaults to 10.
        use_digits (bool): Whether to include digits in the text. Defaults to True.
        use_punctuation (bool): Whether to include punctuation in the text. Defaults to True.

    Returns:
        str: A random text string of the specified length.
    """
    # Define the character sets to use
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    # Ensure the character set is not empty
    if not characters:
        raise ValueError("At least one character set must be selected")

    # Generate the random text
    try:
        random_text = ''.join(random.choice(characters) for _ in range(length))
        return random_text
    except Exception as e:
        raise RuntimeError(f"Failed to generate random text: {str(e)}")

def main():
    """
    Main function to demonstrate the usage of the generate_random_text function.
    """
    try:
        # Example usage
        print(generate_random_text(length=20, use_digits=True, use_punctuation=True))
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()