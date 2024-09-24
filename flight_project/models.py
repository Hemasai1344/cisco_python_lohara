class Flight:
    def __init__(self, flight_number, flight_name, capacity, airplane_id):
        self.flight_number = flight_number
        self.flight_name = flight_name
        self.capacity = capacity
        self.airplane_id = airplane_id
        self.seats = {
            'premium': {
                'window': int(capacity * 0.05),
                'middle': int(capacity * 0.02),
                'aisle': int(capacity * 0.03)
            },
            'business': {
                'window': int(capacity * 0.10),
                'middle': int(capacity * 0.05),
                'aisle': int(capacity * 0.05)
            },
            'regular': {
                'window': int(capacity * 0.35),
                'middle': int(capacity * 0.20),
                'aisle': int(capacity * 0.15)
            }
        }
        self.bookings = []

    def __str__(self):
        return f'[Flight Number={self.flight_number}, Flight Name={self.flight_name}, Capacity={self.capacity}, Seats={self.seats}]'

    def __repr__(self):
        return self.__str__()

class Booking:
    def __init__(self, booking_id, flight_number, seat_type, seat_position):
        self.booking_id = booking_id
        self.flight_number = flight_number
        self.seat_type = seat_type
        self.seat_position = seat_position

    def __str__(self):
        return f'[Booking ID={self.booking_id}, Flight Number={self.flight_number}, Seat Type={self.seat_type}, Seat Position={self.seat_position}]'

    def __repr__(self):
        return self.__str__()

class Airplane:
    def __init__(self, id=None, model='', capacity=0, status=''):
        self.id = id
        self.model = model
        self.capacity = capacity
        self.status = status
