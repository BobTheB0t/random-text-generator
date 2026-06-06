import random
import string
from typing import List, Optional

class RandomTextGenerator:
    """
    Generates random text based on specified parameters.
    Supports customizable length, character sets, and word separation.
    """

    def __init__(self, 
                 min_length: int = 10, 
                 max_length: int = 50,
                 use_uppercase: bool = True,
                 use_lowercase: bool = True,
                 use_digits: bool = True,
                 use_punctuation: bool = False,
                 word_separated: bool = False):
        """
        Initializes the random text generator with specified parameters.

        Args:
            min_length: Minimum length of generated text
            max_length: Maximum length of generated text
            use_uppercase: Include uppercase letters
            use_lowercase: Include lowercase letters
            use_digits: Include digits
            use_punctuation: Include punctuation
            word_separated: Generate word-separated text
        """
        self.min_length = min_length
        self.max_length = max_length
        self.use_uppercase = use_uppercase
        self.use_lowercase = use_lowercase
        self.use_digits = use_digits
        self.use_punctuation = use_punctuation
        self.word_separated = word_separated

        self._validate_parameters()
        self._build_character_set()

    def _validate_parameters(self) -> None:
        """Validates that the initialization parameters are valid."""
        if self.min_length > self.max_length:
            raise ValueError("min_length cannot be greater than max_length")
        if not any([self.use_uppercase, self.use_lowercase, 
                   self.use_digits, self.use_punctuation]):
            raise ValueError("At least one character set must be enabled")

    def _build_character_set(self) -> None:
        """Builds the character set based on enabled options."""
        self.character_set = []
        if self.use_uppercase:
            self.character_set.extend(string.ascii_uppercase)
        if self.use_lowercase:
            self.character_set.extend(string.ascii_lowercase)
        if self.use_digits:
            self.character_set.extend(string.digits)
        if self.use_punctuation:
            self.character_set.extend(string.punctuation)

    def generate(self, num_texts: int = 1) -> List[str]:
        """
        Generates random text(s) based on the configured parameters.

        Args:
            num_texts: Number of texts to generate

        Returns:
            List of generated random texts
        """
        texts = []
        for _ in range(num_texts):
            if self.word_separated:
                text = self._generate_word_separated_text()
            else:
                text = self._generate_continuous_text()
            texts.append(text)
        return texts

    def _generate_continuous_text(self) -> str:
        """Generates a single continuous random text string."""
        length = random.randint(self.min_length, self.max_length)
        return ''.join(random.choice(self.character_set) for _ in range(length))

    def _generate_word_separated_text(self) -> str:
        """Generates word-separated random text."""
        num_words = random.randint(2, 10)  # Reasonable range for word count
        words = []
        for _ in range(num_words):
            word_length = random.randint(3, 15)  # Typical word lengths
            word = ''.join(random.choice(self.character_set) 
                          for _ in range(word_length))
            words.append(word)
        return ' '.join(words)

# Example usage
if __name__ == "__main__":
    try:
        generator = RandomTextGenerator(
            min_length=10,
            max_length=50,
            use_uppercase=True,
            use_lowercase=True,
            use_digits=True,
            use_punctuation=False,
            word_separated=True
        )

        texts = generator.generate(num_texts=5)
        for i, text in enumerate(texts):
            print(f"Generated text {i+1}: {text}")

    except Exception as e:
        print(f"An error occurred: {e}")