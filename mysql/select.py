from conn import myCursor

myCursor.execute("SELECT * FROM customers")

records = myCursor.fetchall()

for record in records:
    print(record)

print("123")