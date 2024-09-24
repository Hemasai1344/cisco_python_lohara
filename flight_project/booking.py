from models import Booking
from crud_operations import get_flights, book_ticket, get_bookings

def book_ticket_for_flight(booking_id, flight_number, seat_type, seat_position):
    flights = get_flights()
    for flight in flights:
        if flight.flight_number == flight_number:
            if flight.seats[seat_type][seat_position] > 0:
                flight.seats[seat_type][seat_position] -= 1
                booking = Booking(booking_id, flight_number, seat_type, seat_position)
                book_ticket(booking)
                print('Ticket booked successfully')
                print_remaining_seats(flight_number)
            else:
                print(f'No {seat_position} {seat_type} seats available')
            return
    print(f'No such flight number {flight_number}')

def print_remaining_seats(flight_number):
    flights = get_flights()
    for flight in flights:
        if flight.flight_number == flight_number:
            print(f'Remaining seats for flight {flight_number}: {flight.seats}')
            return
