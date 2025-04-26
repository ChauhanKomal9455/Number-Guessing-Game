from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)

app.secret_key = 'CodeClause2025Rocks!'

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'number_to_guess' not in session:
        session['number_to_guess'] = random.randint(1, 100)
        session['tries'] = 0

    message = session.get('message', '')

    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            session['tries'] += 1

            if guess < session['number_to_guess']:
                message = "Too low! Try again."
            elif guess > session['number_to_guess']:
                message = "Too high! Try again."
            else:
                message = f"BINGO! It took you {session['tries']} attempts."

            session['message'] = message
            return redirect(url_for('home'))

        except ValueError:
            message = "Please enter a valid number."
            session['message'] = message
            return redirect(url_for('home'))

    return render_template('index.html', message=message, tries=session.get('tries', 0))

@app.route('/restart')
def restart_game():
    session.pop('number_to_guess', None)
    session.pop('tries', None)
    session.pop('message', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
