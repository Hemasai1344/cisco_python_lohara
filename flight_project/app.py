from flask import Flask, jsonify, request
from crud_operations import create_tables, add_airplane, get_airplanes, add_flight, get_flights, book_ticket, get_bookings
from models import Airplane, Flight, Booking

create_tables()
app = Flask(__name__)

@app.route('/airplanes', methods=['POST'])
def airplanes_create():
    body = request.get_json()
    new_airplane = Airplane(model=body['model'], capacity=body['capacity'], status=body['status'])
    add_airplane(new_airplane)
    return jsonify({'message': 'Airplane created successfully'})

@app.route('/airplanes', methods=['GET'])
def airplanes_read_all():
    airplanes = get_airplanes()
    return jsonify([{'id': a.id, 'model': a.model, 'capacity': a.capacity, 'status': a.status} for a in airplanes])

@app.route('/flights', methods=['POST'])
def flights_create():
    body = request.get_json()
    new_flight = Flight(flight_number=body['flight_number'], flight_name=body['flight_name'], capacity=body['capacity'], airplane_id=body['airplane_id'])
    add_flight(new_flight)
    return jsonify({'message': 'Flight created successfully'})

@app.route('/flights', methods=['GET'])
def flights_read_all():
    flights = get_flights()
    return jsonify([{'flight_number': f.flight_number, 'flight_name': f.flight_name, 'capacity': f.capacity, 'airplane_id': f.airplane_id} for f in flights])

@app.route('/bookings', methods=['POST'])
def bookings_create():
    body = request.get_json()
    new_booking = Booking(booking_id=body['booking_id'], flight_number=body['flight_number'], seat_type=body['seat_type'], seat_position=body['seat_position'])
    book_ticket(new_booking)
    return jsonify({'message': 'Booking created successfully'})

@app.route('/bookings', methods=['GET'])
def bookings_read_all():
    bookings = get_bookings()
    return jsonify([{'booking_id': b.booking_id, 'flight_number': b.flight_number, 'seat_type': b.seat_type, 'seat_position': b.seat_position} for b in bookings])

if __name__ == '__main__':
    app.run(debug=True)
