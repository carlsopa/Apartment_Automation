#using the flask frame work and server, create a multipage webpage for to control my apartments various lights and sensors.
from flask import *
from Controlsa import *

bl = Bedroom()
cl = Chandelier()

#bl = BedroomLights()

app = Flask(__name__)
app.secret_key = "my secret"
#inital webpage viewed
@app.route('/')
def Apartment():
    #return 'hello'
    return render_template('mobile.html', title='')
#route to take when the bedroom light toggles are switched.  
@app.route('/bedroomlight/<string:light>',methods=['POST'])
def led(light):
    #print(light)
    bl.Lights(light)
    #if light == 0:
    #    bl.Lights('left')
    #elif light == 1:
    #    bl.Lights('right')
    return('',204)

@app.route('/chandelier')
def Chandelier():
    return render_template('chandelier.html', title='')
#route to take when a change is detected on the chandelier control page
@app.route('/chandelier/<string:ctrl>',methods=['POST'])
def chandelier(ctrl):
    #print('hello')
    cl.ChandelierControl(ctrl)
    return ('',204)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3232, debug=True)
