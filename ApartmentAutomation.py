from flask import *
from Controlsa import *

bl = Bedroom()
cl = Chandelier()

app = Flask(__name__)
app.secret_key = "my secret"
@app.route('/')
def Apartment():
    #return 'hello'
    return render_template('mobile.html', title='')
#turn on/off bedroom lamps based on string value of "light"
@app.route('/bedroomlight/<string:light>',methods=['POST'])
def led(light):
    bl.Lights(light)
    return('',204)

@app.route('/chandelier')
def Chandelier():
    return render_template('chandelier.html', title='')
#control the living room chandelier based on the string value of "ctrl"
@app.route('/chandelier/<string:ctrl>',methods=['POST'])
def chandelier(ctrl):
    cl.ChandelierControl(ctrl)
    return ('',204)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3232, debug=True)
