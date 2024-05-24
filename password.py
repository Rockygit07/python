import itertools

def generate_wordlist(output_file, characters, word_length):
    with open(output_file, 'w') as file:
        for word in itertools.product(characters, repeat=word_length):
            file.write(''.join(word) + '\n')
    print("Wordlist generated successfully!")


def main():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$&!"  # All characters
    word_length = 8  # Length of each word
    
    output_file = "wordlist.txt"
    generate_wordlist(output_file, characters, word_length)


if __name__ == "__main__":
    main()
