import datetime

# Sample data structure to store books read
books_read = [
    {"title": "Book 1", "date_finished": datetime.date(2024, 8, 7)},
    {"title": "Book 2", "date_finished": datetime.date(2024, 8, 9)},
    {"title": "Book 3", "date_finished": datetime.date(2024, 8, 10)},
    {"title": "Book 4", "date_finished": datetime.date(2024, 8, 11)},
]

def books_read_this_week(books):
    today = datetime.date.today()
    print(today)
    start_of_week = today - datetime.timedelta(days=today.weekday())
    books_this_week = [book for book in books if book["date_finished"] >= start_of_week]
    return books_this_week

def main():
    books_this_week = books_read_this_week(books_read)
    print(f"You've read {len(books_this_week)} books this week:")
    for book in books_this_week:
        print(f"- {book['title']} on {book['date_finished']}")
        
if __name__ == "__main__":
    main()
