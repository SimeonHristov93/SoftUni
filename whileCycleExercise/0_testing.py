import time

for attempt in range(5):
    print(f"Current attempt: {attempt}")
    time.sleep(1)
    print("Trying to connect to database...")
    time.sleep(1)
    if attempt == 1:
        print("Success")
        break
