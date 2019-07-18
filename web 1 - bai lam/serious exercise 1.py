# with render_template
from flask import Flask, render_template       

app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:height>')

def bmi_calcu(weight,height):
    height_m = height/100
    sb_bmi = weight/((height_m)**2)
    return render_template('bmi.html',SB_BMI=sb_bmi)

if __name__ == '__main__':
    app.run(debug ='True')      