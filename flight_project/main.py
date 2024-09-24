from models import Flight, Booking, Airplane
from crud_operations import add_airplane, get_airplanes, add_flight, get_flights, book_ticket, get_bookings

def main_menu():
    while True:
        choice = int(input('''1-Add airplane
2-Display all airplanes
3-Add flight
4-Display all flights
5-Book ticket
6-Display all bookings
7-Exit
Your choice: '''))
        
        if choice == 1:
            model = input('Enter airplane model: ')
            capacity = int(input('Enter airplane capacity: '))
            status = input('Enter airplane status: ')
            airplane = Airplane(model=model, capacity=capacity, status=status)
            add_airplane(airplane)
        elif choice == 2:
            airplanes = get_airplanes()
            for airplane in airplanes:
                print(airplane)
        elif choice == 3:
            flight_number = input('Enter flight number: ')
            flight_name = input('Enter flight name: ')
            capacity = int(input('Enter flight capacity: '))
            airplane_id = int(input('Enter airplane ID: '))
            flight = Flight(flight_number=flight_number, flight_name=flight_name, capacity=capacity, airplane_id=airplane_id)
            add_flight(flight)
        elif choice == 4:
            flights = get_flights()
            for flight in flights:
                print(flight)
        elif choice == 5:
            booking_id = int(input('Enter booking ID: '))
            flight_number = input('Enter flight number: ')
            seat_type = input('Enter seat type (premium/business/regular): ')
            seat_position = input('Enter seat position (window/middle/aisle): ')
            booking = Booking(booking_id=booking_id, flight_number=flight_number, seat_type=seat_type, seat_position=seat_position)
            book_ticket(booking)
        elif choice == 6:
            bookings = get_bookings()
            for booking in bookings:
                print(booking)
        elif choice == 7:
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main_menu()
