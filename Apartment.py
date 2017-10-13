from flask import *
from flask import request
from Controls import *

bl = Bedroom_Light()

app = Flask(__name__)
app.secret_key = "my secret"
@app.route('/')
def Apartment():
        return render_template('apt.html', title='')
@app.route('/alarm')
def ApartmentAlarm():
        return render_template('alarm.html',title='')
@app.route('/chandelier')
def LivingRoomChandelier():
        return render_template('chandelier.html',title='')
@app.route('/bedroomlighta')
def BedroomLights():
        return render_template('bedroomlighta.html',title='')
@app.route('/bedroomlight/<string:light>',methods=['POST'])
def BedroomLight(light):
        bl.Lights(light)
        return('',204)
@app.route('/alarmclock')
def BedroomAlarmclock():
        return render_template('alarmclock.html',title='')
        if request.method == 'POST':
                if request.form['LightSwitch'] == "switch":
                        bl.Lights()
                        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3232, debug=True)
