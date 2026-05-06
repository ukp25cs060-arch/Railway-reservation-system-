# Railway Reservation System

# Total seats
TOTAL_SEATS = 50
available_seats = TOTAL_SEATS

# Store bookings
bookings = {}   # booking_id : {name, age, seat}

# Booking ID generator
booking_counter = 1


# Function: Check Availability
def check_availability():
    print(f"\nAvailable Seats: {available_seats}")


# Function: Book Ticket
def book_ticket():
    global available_seats, booking_counter

    if available_seats <= 0:
        print("\nNo seats available!")
        return

    name = input("Enter Name: ")
    age = input("Enter Age: ")

    seat_number = TOTAL_SEATS - available_seats + 1
    booking_id = f"B{booking_counter}"

    bookings[booking_id] = {
        "name": name,
        "age": age,
        "seat": seat_number
    }

    available_seats -= 1
    booking_counter += 1

    print("\nTicket Booked Successfully!")
    print(f"Booking ID: {booking_id}")
    print(f"Seat Number: {seat_number}")


# Function: View Ticket
def view_ticket():
    booking_id = input("Enter Booking ID: ")

    if booking_id in bookings:
        b = bookings[booking_id]
        print("\n--- Ticket Details ---")
        print(f"Name: {b['name']}")
        print(f"Age: {b['age']}")
        print(f"Seat: {b['seat']}")
    else:
        print("\nInvalid Booking ID!")


# Function: Cancel Ticket
def cancel_ticket():
    global available_seats

    booking_id = input("Enter Booking ID to cancel: ")

    if booking_id in bookings:
        del bookings[booking_id]
        available_seats += 1
        print("\nTicket Cancelled Successfully!")
    else:
        print("\nInvalid Booking ID!")


# Main Menu
def main():
    while True:
        print("\n===== Railway Reservation System =====")
        print("1. Check Availability")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            check_availability()
        elif choice == '2':
            book_ticket()
        elif choice == '3':
            view_ticket()
        elif choice == '4':
            cancel_ticket()
        elif choice == '5':
            print("\nThank you!")
            break
        else:
            print("\nInvalid choice! Try again.")


# Run program
main()
