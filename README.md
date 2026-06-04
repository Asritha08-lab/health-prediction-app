# Health Prediction Application

## Overview

The Health Prediction Application is a Flask-based web application that allows users to manage patient health records and predict potential health risks using blood test results.

The application provides complete CRUD functionality (Create, Read, Update, Delete), data validation, persistent storage using SQLite, and automated health prediction based on patient medical parameters.

## Demo Video

A complete walkthrough of the application demonstrating CRUD operations, data validation, database integration, and health prediction functionality is available below:

[Watch Demo Video](https://drive.google.com/file/d/1CfLTvD5Y0_yT7f9NdJPdjAJSQZWrS7w9/view)

## Features

- Add new patient records
- View all patient records
- Update patient information
- Delete patient records
- Automatic health risk prediction
- Email validation
- Future Date of Birth validation
- SQLite database integration
- Responsive Bootstrap user interface

## Technologies Used

### Backend
- Python
- Flask
- Flask-SQLAlchemy

### Frontend
- HTML5
- Bootstrap 5

### Database
- SQLite

## Patient Information Stored

The application stores the following patient details:

- Full Name
- Date of Birth
- Email Address
- Glucose Level
- Haemoglobin Level
- Cholesterol Level
- Health Prediction Remarks

## Health Prediction Logic

The application automatically generates health predictions based on blood test values.

### High Diabetes Risk
**Condition:** Glucose > 180

### High Cholesterol Risk
**Condition:** Cholesterol > 240

### Possible Anaemia
**Condition:** Haemoglobin < 10

### Healthy
**Condition:** All values are within normal ranges.

## Validation

The application validates:

- Proper email address format
- Date of Birth cannot be a future date
- Numeric blood test values

## CRUD Operations

### Create
Add new patient records.

### Read
Display all patient records in a table.

### Update
Modify existing patient information.

### Delete
Remove patient records from the database.

## Installation

### Clone the Repository

```bash
git clone https://github.com/Asritha08-lab/health-prediction-app.git
```

### Navigate to the Project Directory

```bash
cd health-prediction-app
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

### Open in Browser

```text
http://127.0.0.1:5000
```

## Project Structure

```text
health-prediction-app/
│
├── app.py
├── models.py
├── patients.db
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── add_patient.html
│   └── edit_patient.html
```

## Future Enhancements

- External AI/ML API integration
- Advanced disease prediction models
- User authentication and authorization
- Dashboard analytics
- Report generation

## Author

**Asritha Nalubala**
