# generate_wordlist.py

import itertools

# Define capital letters (A-Z) and years range (1950 to 2024)
capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
years_range = range(1950, 2025)  # from 1950 to 2024 (inclusive)

# Open a file to write the wordlist
with open('wordlist.txt', 'w') as file:
    # Generate combinations of 4 capital letters followed by 4 digits
    for letters in itertools.product(capital_letters, repeat=4):
        for year in years_range:
            # Format as first 4 letters (capital) + 4 digits of the year
            word = ''.join(letters) + str(year)
            file.write(word + '\n')
