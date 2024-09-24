import sqlite3
from models import Flight, Booking, Airplane

def connect():
    con = sqlite3.connect('flight_management_system.db')
    return con

def create_tables():
    con = connect()
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS airplanes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT NOT NULL,
        capacity INTEGER NOT NULL,
        status TEXT NOT NULL
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS flights(
        flight_number TEXT PRIMARY KEY,
        flight_name TEXT NOT NULL,
        capacity INTEGER NOT NULL,
        airplane_id INTEGER,
        FOREIGN KEY (airplane_id) REFERENCES airplanes (id)
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS bookings(
        booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
        flight_number TEXT,
        seat_type TEXT,
        seat_position TEXT,
        FOREIGN KEY (flight_number) REFERENCES flights (flight_number)
    )""")
    con.commit()
    con.close()

def add_airplane(airplane):
    con = connect()
    cur = con.cursor()
    cur.execute("INSERT INTO airplanes (model, capacity, status) VALUES (?, ?, ?)", (airplane.model, airplane.capacity, airplane.status))
    con.commit()
    con.close()

def get_airplanes():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM airplanes")
    airplanes = cur.fetchall()
    con.close()
    return [Airplane(id=row[0], model=row[1], capacity=row[2], status=row[3]) for row in airplanes]

def add_flight(flight):
    con = connect()
    cur = con.cursor()
    cur.execute("INSERT INTO flights (flight_number, flight_name, capacity, airplane_id) VALUES (?, ?, ?, ?)", (flight.flight_number, flight.flight_name, flight.capacity, flight.airplane_id))
    con.commit()
    con.close()

def get_flights():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM flights")
    flights = cur.fetchall()
    con.close()
    return [Flight(flight_number=row[0], flight_name=row[1], capacity=row[2], airplane_id=row[3]) for row in flights]

def book_ticket(booking):
    con = connect()
    cur = con.cursor()
    cur.execute("INSERT INTO bookings (flight_number, seat_type, seat_position) VALUES (?, ?, ?)", (booking.flight_number, booking.seat_type, booking.seat_position))
    con.commit()
    con.close()

def get_bookings():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM bookings")
    bookings = cur.fetchall()
    con.close()
    return [Booking(booking_id=row[0], flight_number=row[1], seat_type=row[2], seat_position=row[3]) for row in bookings]
