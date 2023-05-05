from flask import Flask, request, render_template
import pickle

import numpy as np

app = Flask(__name__, template_folder='./templates', static_folder='./static')

Pkl_Filename = "new.pkl" 
with open(Pkl_Filename, 'rb') as file:  
    model = pickle.load(file)
@app.route('/')

def hello_world():
    return render_template('home.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    
    # features = [float(x) for x in request.form.values()]
    #  print(request.form.values , "and 12324565656" , request.form.keys, "her\n\n\n")
     if request.method == 'POST':
        age = int(request.form['age'])
        
        sex = request.form['Gender']
        if (sex == 'male'):
            sex_male = 1
            sex_female = 0
        else:
            sex_male = 0
            sex_female = 1

        smoker = request.form['smoker']
        if (smoker == 'yes'):
            smoker_yes = 1
            smoker_no = 0
        else:
            smoker_yes = 0
            smoker_no = 1

        bmi = int(request.form['bmi'])
        children = int(request.form['children'])

        region = request.form['region']
        if (region == 'NW'):
            region = 1
        elif (region == 'SE'):
            region = 2
        elif (region == 'SW'):
            region = 3
        else:
            region = 4
        
        
        # values = np.array([age,sex_male,smoker_yes,bmi,children,region])
        # features = [int(x) for x in values]
        # values = [int(x) for x in values].reshape((1,6))
        # print(values)

        # pred = model.predict(values)
        # print(request.form.values)

    # print(features)
        # final = np.array(features).reshape((1,6))
        # print(final)
        pred = model.predict( np.array([age,sex_male,smoker_yes,bmi,children,region]).reshape(1,6))[0][0]
        pred *= age*10 + bmi
        # print(pred)

    
        if pred < 0:

               return render_template('op.html', pred='Expected amount is {0}'.format(pred))
        else:
               return render_template('op.html', pred='Expected amount is {0}'.format(pred))

if __name__ == '__main__':
    app.run(debug=True)