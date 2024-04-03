from flask import Flask, render_template, request, redirect
from database import session, Response

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page_name(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:

            response = Response(email=request.form['email'], subject=request.form['subject'], message=request.form['message'])
            session.add(response)
            session.commit()
            session.close()

            return redirect('/thankyou.html')
        except:
            return 'Not saved to database'
    else:
        return 'Something went wrong, try again'

if __name__ == "__main__":
    app.run(debug=True, port=5000)


