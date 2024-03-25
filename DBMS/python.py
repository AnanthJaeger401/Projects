import mysql.connector
# Connect to the MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sql2203",
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

cursor.execute("""CREATE DATABASE IF NOT EXISTS flightreservation1""")
cursor.execute("""use flightreservation1""")
# Create tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS passenger (
        passengerid INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone VARCHAR(20) NOT NULL,
        address VARCHAR(255) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS flight (
        flightid INT PRIMARY KEY AUTO_INCREMENT,
        airlines VARCHAR(255) NOT NULL,
        departuretime TIME NOT NULL,
        arrivaltime TIME NOT NULL,
        origin VARCHAR(3) NOT NULL,
        destination VARCHAR(3) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS booking (
        bookingid INT PRIMARY KEY AUTO_INCREMENT,
        passengerid INT,
        flightid INT,
        bookingdate DATE NOT NULL,
        seatno VARCHAR(10) NOT NULL,
        FOREIGN KEY (passengerid) REFERENCES passenger(passengerid) ON DELETE CASCADE,
        FOREIGN KEY (flightid) REFERENCES flight(flightid) ON DELETE CASCADE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS airport (
        airportcode VARCHAR(3) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        city VARCHAR(255) NOT NULL,
        country VARCHAR(255) NOT NULL,
        airlines VARCHAR(255) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS payment (
        paymentid INT PRIMARY KEY AUTO_INCREMENT,
        bookingid INT,
        amt DECIMAL(10, 2) NOT NULL,
        paymentdate DATETIME NOT NULL,
        paymentmethod VARCHAR(50) NOT NULL,
        FOREIGN KEY (bookingid) REFERENCES booking(bookingid) ON DELETE CASCADE
    )
""")
