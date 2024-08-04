# ETHOS

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup](#setup)



## Project Overview

ETHOS is a startup company dedicated to teaching students about public speaking. Our mission is to empower individuals to become confident and compelling public speakers. The ETHOS web app serves as a medium for users to register for courses, provide feedback, and learn more about the company and its offerings.

## Features

- **Course Browsing:** Users can browse various public speaking courses offered by ETHOS.
- **Course Registration:** Users can register for courses that suit their needs.
- **Feedback Collection:** Users can provide feedback on courses and their overall experience.
- **Advertising Platform:** Information about ETHOS and its offerings to attract potential users.

## Tech Stack

- **Backend:** Django, Python
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** SQLite (development), PostgreSQL (production)

## Setup

### Prerequisites

- Python 3.x
- Django 3.x or later

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/TheViper008/ETHOS-Startup-Website.git
   cd ETHOS-Startup-Website/myproject
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Run the development server:
   ```sh
   python manage.py runserver
   ```

## Usage

To start the application, navigate to `http://127.0.0.1:8000` in your web browser. You can access the admin panel at `http://127.0.0.1:8000/admin` using the superuser credentials created during setup.
