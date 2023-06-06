@app.route('/payment', methods=['GET','POST'])
def payment():
    payment_methods = ['credit/debit cards', 'PayPal', 'Stripe']
    if request.method == 'POST':
        selected_payment_method = request.form.get('payment_method')
        if selected_payment_method not in payment_methods:
            return redirect(url_for('error'))
        else:
            return redirect(url_for('secure_payment_page'))
    return render_template('payment.html', payment_methods=payment_methods)

@app.route('/secure_payment_page', methods=['GET','POST'])
def secure_payment_page():
    if request.method == 'POST':
        payment_data = request.form
        payment_status = process_payment(payment_data)
        if payment_status:
            return redirect(url_for('payment_success'))
        else:
            return redirect(url_for('payment_failed'))
    return render_template('secure_payment_page.html')

@app.route('/payment_success')
def payment_success():
    return render_template('payment_success.html')

@app.route('/payment_failed')
def payment_failed():
    return render_template('payment_failed.html')

@app.route('/error')
def error():
    return render_template('error.html')