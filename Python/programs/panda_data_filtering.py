"""
In this task:


Find books priced at 200 or below and with copies sold greater than or equal to 100. Separately, find the count of such books.

Find all books written by John Doe and Jane Smith.

Select all books whose title contains the word "Python".

Add headings in text blocks to each section.



"""
import pandas as pd

# Creating a DataFrame with book sales data
book_data = {
    "book_id": [201, 202, 203, 204, 205],
    "title": ["Python for Beginners", "Data Science with Python", "Advanced Python Programming", "Learning SQL", "Python for Data Analysis"],
    "author": ["John Doe", "Jane Smith", "John Doe", "Alice Johnson", "Jane Smith"],
    "price": [250, 300, 150, 180, 280],
    "copies_sold": [150, 200, 100, 90, 300]
}

books_df = pd.DataFrame(book_data)
print(books_df)


#Use filtering to find all books priced above 200.

books_abv200 = books_df[books_df["price"] > 200]
print(books_abv200)

#Find books priced at 200 or below and with copies sold greater than or equal to 100. Separately, find the count of such books.

books_priced_sold = books_df[(books_df["price"]<=200) & (books_df["copies_sold"]>100)]
print(books_priced_sold)

books_below200 = books_df[books_df["price"]<= 200]
print(books_below200)

books_sold = books_df[books_df["copies_sold"]>100]
print(books_sold)

#Find all books written by John Doe and Jane Smith.
books_by_author = books_df[books_df["author"].isin(["John Doe", "Jane Smith"])]
print(books_by_author)

#Select all books whose title contains the word "Python".
books_by_title = books_df[books_df["title"].str.contains("Python")]
print(books_by_title)
