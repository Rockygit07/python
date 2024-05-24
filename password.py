import itertools
from tqdm import tqdm

def generate_wordlist(output_file, characters, word_length):
    total_words = len(characters) ** word_length
    with open(output_file, 'w') as file:
        with tqdm(total=total_words) as pbar:
            for word in itertools.product(characters, repeat=word_length):
                file.write(''.join(word) + '\n')
                pbar.update(1)
    print("Wordlist generated successfully!")


def main():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$&!"  # All characters
    word_length = 8  # Length of each word
    
    output_file = "wordlist.txt"
    generate_wordlist(output_file, characters, word_length)


if __name__ == "__main__":
    main()
