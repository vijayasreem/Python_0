# Flask API for Email Notifications

from flask import Flask, request, jsonify
from flask_mail import Mail, Message

# Create Flask App
app = Flask(__name__)

# Setup Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'example@gmail.com'
app.config['MAIL_PASSWORD'] = 'example_password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# Create Welcome Email Route
@app.route('/email/welcome', methods=['POST'])
def send_welcome_email():
    data = request.get_json()
    user_name = data['user_name']
    user_email = data['user_email']
    msg = Message('Welcome to our Website', sender='example@gmail.com', recipients=[user_email])
    msg.body = f"""
    Dear {user_name},
    Welcome to our website. We hope you have an enjoyable experience using our services.
    Thank you.
    """
    mail.send(msg)
    return jsonify({"message": "Welcome email sent successfully"})

# Create Password Reset Email Route
@app.route('/email/reset_password', methods=['POST'])
def send_reset_password_email():
    data = request.get_json()
    user_name = data['user_name']
    user_email = data['user_email']
    reset_link = data['reset_link']
    msg = Message('Reset Password Request', sender='example@gmail.com', recipients=[user_email])
    msg.body = f"""
    Dear {user_name},
    We received a request to reset your password. Please click on the link below to reset your password.
    {reset_link}
    Thank you.
    """
    mail.send(msg)
    return jsonify({"message": "Password reset email sent successfully"})

# Create Order Confirmation Email Route
@app.route('/email/order_confirmation', methods=['POST'])
def send_order_confirmation_email():
    data = request.get_json()
    user_name = data['user_name']
    user_email = data['user_email']
    order_details = data['order_details']
    msg = Message('Order Confirmation', sender='example@gmail.com', recipients=[user_email])
    msg.body = f"""
    Dear {user_name},
    Your order has been confirmed. Below are the details of your order:
    {order_details}
    Thank you.
    """
    mail.send(msg)
    return jsonify({"message": "Order confirmation email sent successfully"})

# Create Account Activity Alert Email Route
@app.route('/email/account_activity_alert', methods=['POST'])
def send_account_activity_alert_email():
    data = request.get_json()
    user_name = data['user_name']
    user_email = data['user_email']
    alert_details = data['alert_details']
    msg = Message('Account Activity Alert', sender='example@gmail.com', recipients=[user_email])
    msg.body = f"""
    Dear {user_name},
    We have detected unusual activity in your account. Below are the details of the activity:
    {alert_details}
    Please take appropriate action to secure your account.
    Thank you.
    """
    mail.send(msg)
    return jsonify({"message": "Account activity alert email sent successfully"})