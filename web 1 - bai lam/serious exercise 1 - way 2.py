# without render_template
from flask import Flask       

app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:height>')

def bmi_calcu(weight,height):
    height_m = height/100
    sb_bmi = weight/((height_m)**2)
    # return 'Your BMI is: ' + str(sb_bmi)
    # return 'And your condition: '
    if sb_bmi < 16:
        return 'Your BMI is: ' + str(sb_bmi) + '. And you are severely Underweighttttt'
    elif 16 <= sb_bmi < 18.5:
        return 'Your BMI is: ' + str(sb_bmi) + '. And you are Underweight'
    elif 18.5 <= sb_bmi < 25:
        return 'Your BMI is: ' + str(sb_bmi) + '. And you are Normal'
    elif 25 <= sb_bmi < 30:
        return 'Your BMI is: ' + str(sb_bmi) + '. And you are Overweight'
    else:
        return 'Your BMI is: ' + str(sb_bmi) + '. And you are Obese'

if __name__ == '__main__':
    app.run(debug ='True')      