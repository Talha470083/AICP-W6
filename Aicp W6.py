import datetime

# Constants for ticket prices and attractions
ONE_ADULT_ONE_DAY_TICKET_PRICE = 20
ONE_ADULT_TWO_DAY_TICKET_PRICE = 30
ONE_CHILD_ONE_DAY_TICKET_PRICE = 12
ONE_CHILD_TWO_DAY_TICKET_PRICE = 18
ONE_SENIOR_ONE_DAY_TICKET_PRICE = 16
ONE_SENIOR_TWO_DAY_TICKET_PRICE = 24
FAMILY_TICKET_FOR_ONE_DAY = 60
FAMILY_TICKET_FOR_TWO_DAY = 90
GROUP_PRICE_PER_PERSON_FOR_ONE_DAY = 15
GROUP_PRICE_PER_PERSON_FOR_TWO_DAY = 22.50
EXTRA_ATTRACTIONS = {
    'Lion feeding': 2.5,
    'Penguin Feeding': 2.0,
    'Evening barbecue (two-day tickets only)': 5.0
}

# Function to display ticket options and attractions
def display_options():
    print("Ticket Options:")
    print("1. One-Day Ticket - $20 (Adult)")
    print("2. Two-Day Ticket - $30 (Adult)")
    print("3. One-Day Ticket - $12 (Child)")
    print("4. Two-Day Ticket - $18 (Child)")
    print("5. One-Day Ticket - $16 (Senior)")
    print("6. Two-Day Ticket - $24 (Senior)")
    print("7. Family Ticket for One Day - $60")
    print("8. Family Ticket for Two Days - $90")
    print("9. Group Price per Person for One Day - $15")
    print("10. Group Price per Person for Two Days - $22.50")

    print("\nExtra Attractions:")
    for attraction, price in EXTRA_ATTRACTIONS.items():
        print(f"{attraction} - ${price}")

# Function to validate and get booking details
def get_booking_details():
    while True:
        try:
            ticket_type = int(input("Enter ticket type (1-10): "))
            if ticket_type not in range(1, 11):
                raise ValueError("Invalid ticket type. Please enter a number from 1 to 10.")
            break
        except ValueError as e:
            print(e)

    days_available = [str(datetime.date.today() + datetime.timedelta(days=i)) for i in range(7)]
    print("Days Available for Booking:")
    print("\n".join(days_available))

    selected_day = input("Enter the day for the booking (YYYY-MM-DD format): ")

    attractions = []
    while True:
        add_attraction = input("Do you want to add an attraction? (y/n): ").lower()
        if add_attraction == 'n':
            break
        elif add_attraction == 'y':
            print("Available Attractions:")
            print("\n".join(EXTRA_ATTRACTIONS.keys()))
            attraction = input("Enter the attraction you want to add: ")
            if attraction in EXTRA_ATTRACTIONS:
                attractions.append(attraction)
            else:
                print("Invalid attraction. Please choose from the available options.")

    return ticket_type, selected_day, attractions

# Function to calculate total cost
def calculate_total_cost(ticket_type, attractions):
    if ticket_type == 1:
        return ONE_ADULT_ONE_DAY_TICKET_PRICE + sum(EXTRA_ATTRACTIONS[attraction] for attraction in attractions)
    elif ticket_type == 2:
        return ONE_ADULT_TWO_DAY_TICKET_PRICE + sum(EXTRA_ATTRACTIONS[attraction] for attraction in attractions)
    elif ticket_type == 3:
        return ONE_CHILD_ONE_DAY_TICKET_PRICE + sum(EXTRA_ATTRACTIONS[attraction] for attraction in attractions)
    elif ticket_type == 4:
        return ONE_CHILD_TWO_DAY_TICKET_PRICE + sum(EXTRA_ATTRACTIONS[attraction] for attraction in attractions)
    elif ticket_type == 5:
        return ONE_SENIOR_ONE_DAY_TICKET_PRICE + sum(EXTRA_ATTRACTIONS[attraction] for attraction in attractions)
    elif ticket_type == 6:
        return ONE_SENIOR_TWO_DAY_TICKET_PRICE + sum(EXTRA_ATTRACTIONS[attraction] for attraction in attractions)
    elif ticket_type == 7:
        return FAMILY_TICKET_FOR_ONE_DAY
    elif ticket_type == 8:
        return FAMILY_TICKET_FOR_TWO_DAY
    elif ticket_type == 9:
        return GROUP_PRICE_PER_PERSON_FOR_ONE_DAY
    elif ticket_type == 10:
        return GROUP_PRICE_PER_PERSON_FOR_TWO_DAY

# Function to process a booking
def process_booking():
    print("Welcome to the Wildlife Park Ticket Booking System!")

    while True:
        display_options()
        ticket_type, selected_day, attractions = get_booking_details()
        total_cost = calculate_total_cost(ticket_type, attractions)

        print("\nBooking Details:")
        if ticket_type in [1, 2, 3, 4, 5, 6]:
            print(f"Ticket Type: {'One-Day' if ticket_type % 2 != 0 else 'Two-Day'}")
        elif ticket_type == 7:
            print("Ticket Type: Family Ticket for One Day")
        elif ticket_type == 8:
            print("Ticket Type: Family Ticket for Two Days")
        elif ticket_type == 9:
            print("Ticket Type: Group Price per Person for One Day")
        elif ticket_type == 10:
            print("Ticket Type: Group Price per Person for Two Days")

        print(f"Selected Day: {selected_day}")
        if attractions:
            print("Selected Attractions:")
            for attraction in attractions:
                print(attraction)
        print(f"Total Cost: ${total_cost}")

        confirm_booking = input("\nConfirm booking? (y/n): ").lower()
        if confirm_booking == 'y':
            booking_number = hash((ticket_type, selected_day, tuple(attractions)))
            print(f"\nBooking confirmed! Your unique booking number is: {abs(booking_number)}\n")
        else:
            print("Booking canceled.\n")

        another_booking = input("Do you want to make another booking? (y/n): ").lower()
        if another_booking != 'y':
            print("Thank you for using the Wildlife Park Ticket Booking System. Goodbye!")
            break

# Main program
if __name__ == "__main__":
    process_booking()
