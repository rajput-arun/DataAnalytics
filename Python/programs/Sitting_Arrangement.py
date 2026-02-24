"""
Seating Arrangement


We're organizing a conference and arranging seats for participants in a hall. The hall consists of rows and seats per row. Our task is to print a seating plan, marking the numbers of rows and seats in each row.

Create a function seating_arrangement that:

Takes the number of rows and the number of seats_per_row.
Uses nested loops to print the numbers of rows and seats, where:
Outer loop iterates through the rows.
Inner loop iterates through the seats in each row.
In the final result, the row number for each row should come first, and the seat numbers in that row — second. Here's an example output for a hall with 3 rows and 4 seats per row:

seating_arrangement(3, 4) == [
    "Row 1: Seat 1, Seat 2, Seat 3, Seat 4",
    "Row 2: Seat 1, Seat 2, Seat 3, Seat 4",
    "Row 3: Seat 1, Seat 2, Seat 3, Seat 4"
]

"""
def seating_arrangement(rows: int, seats_per_row: int) -> list[str]:
    lst = []
    arrangement=""
    for i in range(rows):
        arrangement="Row "+str(i+1)+": "
        for j in range(seats_per_row):
            arrangement+="Seat "+str(j+1)+", "
        arrangement+="\n"
        lst.append(arrangement)
    print(lst)
    return lst

seating_arrangement(5, 7)




