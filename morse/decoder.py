from morse.mapping import MORSE
REVERSE_MORSE = {v: k for k, v in MORSE.items()}

def decode_word(word):
    letters = word.split()
    decoded = []

    for letter in letters:
        if letter in REVERSE_MORSE:
            decoded.append(REVERSE_MORSE[letter])

    return "".join(decoded)

def decode(text):
    words = text.split("|")
    decoded_words = []

    for word in words:
        decoded_words.append(decode_word(word))

    return " ".join(decoded_words)

if __name__ == "__main__":
    # Example usage for one word
    EXAMPLE_MORSE = ".... .."
    DECODED_TEXT = decode_word(EXAMPLE_MORSE)
    print(f"Decoded '{EXAMPLE_MORSE}' to text: '{DECODED_TEXT}'")

    # Example usage for one sentence
    EXAMPLE_MORSE = ".... ..|--. ..- -.-- ..."
    DECODED_TEXT = decode(EXAMPLE_MORSE)
    print(f"Decoded '{EXAMPLE_MORSE}' to text '{DECODED_TEXT}'")
