from flask import (Flask, render_template)


app = Flask(__name__)

@app.route('/OurMission')
def OurMission():
    return render_template("mission.html")


@app.route('/fundraising')
def fundraising():
    return render_template('fundraising.html')

@app.route('/Broadcast')
def broadcast():
    return render_template('broadcast.html')

@app.route('/sponsorships')
def sponsor():
    return render_template('sponsorships.html')

@app.route('/')
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(port='3000', host='127.0.0.1')

