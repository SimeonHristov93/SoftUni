book_pages = int(input())
pages_read = int(input())
days = int(input())

hours = book_pages // pages_read
daily_reading = hours // days

print(f"Needed hours to read daily is {daily_reading} hours.")
