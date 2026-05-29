from config import Config
from flask import Flask, render_template, request, redirect, url_for
from models import contact_add
from flask_mail import Mail, Message
import os
import resend


app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)
resend.api_key = "re_RDyB76gw_PWKSr5SAFXnugud9rVho3xZv"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':

        try:
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']

            contact_add(name, email, message)

            msg = Message(
                subject='New Portfolio Contact',
                sender=app.config['MAIL_USERNAME'],
                recipients=['bharathr1130@gmail.com']
            )

            msg.body = f"""
New Contact Message

Name: {name}
Email: {email}

Message:
{message}
"""

            resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": ["nagaveni.bharath1981@gmail.com"],
                "subject": "New Portfolio Contact",
                "html": f"""
                <h3>New Contact Message</h3>

                <p><b>Name:</b> {name}</p>
                <p><b>Email:</b> {email}</p>
                <p><b>Message:</b> {message}</p>
                """
            })

            return redirect(url_for('index'))

        except Exception as e:
            return f"ERROR: {str(e)}"

    return render_template('contact.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)