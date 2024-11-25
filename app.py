from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get input values from the form
        sistolik = int(request.form['sistolik'])
        diastolik = int(request.form['diastolik'])
        age = int(request.form['age'])
        gender = request.form['gender']
        lifestyle = request.form['lifestyle']
        diet = request.form['diet']
        physical_activity = request.form['physical_activity']
        family_history = request.form['family_history']

        # Blood pressure classification logic
        if sistolik < 120 and diastolik < 80:
            hasil = "Normal"
            solusi = (
                "Your blood pressure is within the normal range. Keep up with a healthy lifestyle to maintain your blood pressure. "
                "Ensure a balanced diet, regular physical activity, and regular monitoring of your blood pressure."
            )
        elif 120 <= sistolik <= 129 and diastolik < 80:
            hasil = "Elevated"
            solusi = (
                "Your blood pressure is elevated. This is an early warning sign of potential hypertension. "
                "Consider reducing stress, improving your diet (reduce salt and fat intake), and increasing your physical activity."
            )
        elif 130 <= sistolik <= 139 or 80 <= diastolik <= 89:
            hasil = "Hypertension Stage 1"
            solusi = (
                "You may have Stage 1 hypertension. It's important to monitor your blood pressure regularly. "
                "If lifestyle changes aren't sufficient, you might need medication. "
                "Consult with your doctor for advice tailored to your situation."
            )
        elif 140 <= sistolik <= 180 or 90 <= diastolik <= 120:
            hasil = "Hypertension Stage 2"
            solusi = (
                "You have Stage 2 hypertension. This stage may require medications and lifestyle modifications. "
                "It's essential to consult your doctor for appropriate treatment and blood pressure management strategies."
            )
        elif sistolik > 180 or diastolik > 120:
            hasil = "Hypertensive Crisis"
            solusi = (
                "You are in a hypertensive crisis. Seek emergency medical attention immediately. "
                "A hypertensive crisis can lead to severe complications, such as a heart attack or stroke."
            )
        else:
            hasil = "Unknown"
            solusi = "There was an issue with the input. Please double-check your values and try again."

        # Personalized advice based on age, gender, and lifestyle
        if age > 60:
            solusi += " Since you are over 60, it's crucial to monitor your blood pressure closely. Regular check-ups are highly recommended."
        if gender == "female" and age > 50:
            solusi += " As a woman over 50, hormonal changes due to menopause can impact blood pressure. It's vital to maintain a healthy lifestyle and consult with your healthcare provider."
        if lifestyle == "poor":
            solusi += " A poor lifestyle can contribute to high blood pressure. Consider adopting healthier habits such as exercising, reducing salt intake, and managing stress."
        if diet == "poor":
            solusi += " Poor dietary habits (such as high salt, fat, or sugar intake) can worsen blood pressure. Try to eat a balanced diet rich in vegetables, fruits, and lean proteins."
        if physical_activity == "low":
            solusi += " Low physical activity can negatively impact your blood pressure. Incorporate regular exercise into your routine, such as walking, swimming, or biking."
        if family_history == "yes":
            solusi += " A family history of hypertension increases your risk. It's even more important to keep your blood pressure under control and get regular check-ups."

        return render_template('index.html', hasil=hasil, solusi=solusi)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
