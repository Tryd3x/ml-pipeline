import sys, os

from flask import Flask, render_template, request, jsonify
from src.pipeline.prediction_pipeline import PredictionPipeline, CustomClass

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def prediction_data():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomClass(
            age= int(request.form.get('age')),
            workclass= request.form.get('workclass'),
            education_num= int(request.form.get('education_num')),
            marital_status= int(request.form.get('marital_status')),
            occupation= int(request.form.get('occupation')),
            relationship= int(request.form.get('relationship')),
            race= int(request.form.get('race')),
            sex= int(request.form.get('sex')),
            capital_gain= int(request.form.get('capital_gain')),
            capital_loss= int(request.form.get('capital_loss')),
            hours_per_week= int(request.form.get('hours_per_week')),
        )

    final_data = data.get_data_DataFrame()
    pipeline_prediction = PredictionPipeline()
    pred = int(pipeline_prediction.predict(final_data))

    if pred == 0:
        return render_template("results.html", final_result=f"Income is less than and equal to 50k: {pred}")
    elif pred == 1:
        return render_template("results.html", final_result=f"Income is more than and equal to 50k: {pred}")
    
if __name__ == '__main__':
    app.run(debug=True)
