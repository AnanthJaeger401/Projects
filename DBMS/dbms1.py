import tkinter as tk
from tkinter import ttk
from MySQLdb import connect
import mysql.connector

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def display_tables():
    # Establish a database connection
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sql2203",
    database="flightreservation1")
    cur=conn.cursor()

    # Fetch data from the Passenger table
    cur.execute("SELECT * FROM Passenger")
    passengers = cur.fetchall()

    # Fetch data from the Flight table
    cur.execute("SELECT * FROM Flight")
    flights = cur.fetchall()

    # Fetch data from the Booking table
    cur.execute("SELECT * FROM Booking")
    bookings = cur.fetchall()

    # Fetch data from the Airport table
    cur.execute("SELECT * FROM Airport")
    airports = cur.fetchall()

    # Fetch data from the Payment table
    cur.execute("SELECT * FROM Payment")
    payments = cur.fetchall()    
    # Close the database connection
    conn.close()

    return render_template('display_tables.html', passengers=passengers, flights=flights, bookings=bookings, airports=airports, payments=payments)
@app.route('/DaytimeTravellers')
def DaytimeTravellers():
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sql2203",
    database="flightreservation1")
    cur=conn.cursor()
    cur.execute("select * from daytimepassengers;")
    daytimepassengers = cur.fetchall()
    return render_template('daytimepass.html', daytimepassengers=daytimepassengers)

@app.route('/NightTimeTravellers')
def NightTimeTravellers():
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sql2203",
    database="flightreservation1")
    cur=conn.cursor()
    cur.execute("select * from nighttimepassengers;")
    nighttimepassengers = cur.fetchall()
    return render_template('nighttimepass.html', nighttimepassengers=nighttimepassengers)
if __name__ == '__main__':
    app.run(debug=True)
