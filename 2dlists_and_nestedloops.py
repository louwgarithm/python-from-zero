books = [
    [
        1, 2, 3
    ],
    [
        4, 5, 6
    ],
    [
     7, 8, 9
    ]
]

print(books)
print(books[1])
print(books[2][1])

for book in books:
    for num in book:
        print(num)
