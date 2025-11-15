correct_pin = "0805"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered_pin = input("Enter the PIN code: ")
    if entered_pin == correct_pin:
        print("PIN correct.")
        break
    else:
        print("Incorrect...\n")
        attempts += 1

if attempts == max_attempts:
    print("Sorry, your payment card has been blocked.")
