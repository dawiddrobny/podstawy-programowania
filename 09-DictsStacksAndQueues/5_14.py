import queue
import time

customer_queue = queue.Queue()
ticket_number = 1

while True:
    print("\n1. New Customer")
    print("2. Serve Customer")
    print("0. Exit")
    choice = input("Select option: ")
    
    if choice == '1':
        print(f"Customer added with Ticket #{ticket_number}")
        customer_queue.put(ticket_number)
        ticket_number += 1
    elif choice == '2':
        if not customer_queue.empty():
            served_ticket = customer_queue.get()
            print(f"Serving customer with Ticket #{served_ticket}...")
            time.sleep(1) # simulate service
            print("Customer served.")
        else:
            print("No customers in queue.")
    elif choice == '0':
        break
