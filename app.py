from flask import Flask, render_template, request, redirect, url_for
from models import db, Patient
import re
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


def predict_health(glucose, haemoglobin, cholesterol):

    if glucose > 180:
        return "High Diabetes Risk"

    elif cholesterol > 240:
        return "High Cholesterol Risk"

    elif haemoglobin < 10:
        return "Possible Anaemia"

    else:
        return "Healthy"


@app.route('/')
def home():
    patients = Patient.query.all()
    return render_template('index.html', patients=patients)


@app.route('/add', methods=['GET', 'POST'])
def add_patient():

    if request.method == 'POST':

        email = request.form['email']
        dob = request.form['dob']

        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(email_pattern, email):
            return "Invalid Email Address"

        if datetime.strptime(dob, "%Y-%m-%d").date() > datetime.today().date():
            return "Date of Birth cannot be in the future"

        patient = Patient(
            full_name=request.form['full_name'],
            dob=request.form['dob'],
            email=request.form['email'],
            glucose=float(request.form['glucose']),
            haemoglobin=float(request.form['haemoglobin']),
            cholesterol=float(request.form['cholesterol']),
            remarks=predict_health(
                float(request.form['glucose']),
                float(request.form['haemoglobin']),
                float(request.form['cholesterol'])
            )
        )

        db.session.add(patient)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('add_patient.html')


@app.route('/delete/<int:id>')
def delete_patient(id):

    patient = Patient.query.get_or_404(id)

    db.session.delete(patient)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):

    patient = Patient.query.get_or_404(id)

    if request.method == 'POST':

        email = request.form['email']
        dob = request.form['dob']

        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(email_pattern, email):
            return "Invalid Email Address"

        if datetime.strptime(dob, "%Y-%m-%d").date() > datetime.today().date():
            return "Date of Birth cannot be in the future"

        patient.full_name = request.form['full_name']
        patient.dob = request.form['dob']
        patient.email = request.form['email']
        patient.glucose = float(request.form['glucose'])
        patient.haemoglobin = float(request.form['haemoglobin'])
        patient.cholesterol = float(request.form['cholesterol'])

        patient.remarks = predict_health(
            patient.glucose,
            patient.haemoglobin,
            patient.cholesterol
        )

        db.session.commit()

        return redirect(url_for('home'))

    return render_template('edit_patient.html', patient=patient)


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)