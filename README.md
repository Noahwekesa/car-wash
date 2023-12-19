# In-House Carwash System 
Dashboard
![alt text](https://github.com/Noahwekesa/car-wash/blob/main/screenshot/home.png)
## Overview
This Django-based In-House Carwash System is designed to streamline the carwash management process for in-house use. It includes features such as customer management, service tracking, user authentication, and booking management.
## Features
Customer Management:

Capture customer details including name, email, phone, vehicle type, gender, and location.
Services:

Define various carwash services that can be offered.
User Authentication:

User registration and authentication are handled using Django's built-in User model.
Booking Management:

Schedule carwash services with date, payment status, amount, and description.
As
## Installation
A step-by-step guide on how to install and set up your project. 
Step 1: Clone the repository
```bash
git clone https://github.com/noahwekesa/car-wash.git 
```
Step 2: Navigate to the project directory
```bash
cd car-wash
```
step 3: Install virtural enviroment
```bash
virtualenv .
```
Step 4: Install dependencies

```bash
pip install -r requirements.txt 
```
step 5: Navigate to src
```bash
cd src
```
Step 5: Apply database migrations
```bash
python manage.py migrate 
```
Step 5: Run the development server

```bash
python manage.py runserver
```
Access the application in your web browser at http://localhost:8000/.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.sociate bookings with customers and selected services.
