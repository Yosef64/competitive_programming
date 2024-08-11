from datetime import datetime, timedelta

# Sample data: List of dates when books were read
books_read_dates = [
    "2024-08-05", "2024-08-06", "2024-08-08",  # Books read this week
    "2024-07-31", "2024-07-29",                # Books read last week
]

# Convert string dates to datetime objects
books_read_dates = [datetime.strptime(date, "%Y-%m-%d") for date in books_read_dates]

# Get the current date and the start of the current week (Monday)
current_date = datetime.now()

start_of_week = current_date - timedelta(days=current_date.weekday())
print(start_of_week)
# Count the number of books read this week
books_read_this_week = sum(1 for date in books_read_dates if date >= start_of_week)

print(books_read_this_week)
