# Unit 3 - Q9: Movie Collection System (CSV + Regular Expressions)
# Reads movies.csv with the csv module inside a with statement.

import csv
import re


def load_movies(filename):
    with open(filename, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def display_movies(movies):
    if not movies:
        print("No matching movies found.")
        return
    for m in movies:
        print(f"ID: {m['movie_id']} | Name: {m['movie_name']} | "
              f"Rating: {m['rating']} | Ticket Price: ₹{m['ticket_price']}")


def main():
    movies = load_movies("movies.csv")

    print("\n--- All Movie Information ---")
    display_movies(movies)

    movie_id = input("\nEnter Movie ID to search: ").strip()
    print("\n--- Search by Movie ID ---")
    display_movies([m for m in movies if m["movie_id"].upper() == movie_id.upper()])

    keyword = input("\nEnter a keyword to search movie titles (regex allowed): ").strip()
    print("\n--- Search by Title (Regex) ---")
    try:
        pattern = re.compile(keyword, re.IGNORECASE)
        display_movies([m for m in movies if pattern.search(m["movie_name"])])
    except re.error as e:
        print(f"Invalid pattern: {e}")


if __name__ == "__main__":
    main()
