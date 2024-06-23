from datetime import datetime, timedelta

# Define start and end dates
start_date = datetime(1950, 1, 1)
end_date = datetime(2024, 12, 31)

# List to hold formatted dates
date_list = []

# Generate dates in a loop
current_date = start_date
while current_date <= end_date:
    # Format the date as 'ddmmyyyy'
    formatted_date = current_date.strftime('%d%m%Y')
    date_list.append(formatted_date)
    # Increment to the next day
    current_date += timedelta(days=1)

# Save the list of dates to a text file
with open('wordlist_years.txt', 'w') as file:
    file.write('\n'.join(date_list))

print("Wordlist created successfully!")
