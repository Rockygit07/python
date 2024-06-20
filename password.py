import random
import string
from tqdm import tqdm
import time

def generate_word(length=8):
    characters = string.ascii_letters + string.digits + "@#"
    word = ''.join(random.choice(characters) for _ in range(length))
    return word

def generate_word_list(n, length=8):
    word_list = []
    for _ in tqdm(range(n), desc="Generating words", ncols=100):
        word_list.append(generate_word(length))
    return word_list

# Record the start time
start_time = time.time()

# Generate a list of 100 words as an example
word_list = generate_word_list(100)

# Record the end time
end_time = time.time()

# Calculate the total time taken
total_time = end_time - start_time

# Print the total time taken
print(f"Total time taken: {total_time:.2f} seconds")

# Optionally, print the word list
# for word in word_list:
#     print(word)
