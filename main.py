from flask import Flask, render_template, url_for
import random
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("coupon.html")


if __name__ == '__main__':
    app.run(
    	host='0.0.0.0',
    	port=random.randint(2000, 9000),
    	debug=True)