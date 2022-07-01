from django.shortcuts import render

import joblib
import numpy as np
import numpy as geek


def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):


    model = joblib.load('C:/Users/Dell/Desktop/PredictDiabetes_RandomForest/final_model.sav')

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])




    out_arr = geek.asarray([[val1, val2, val3, val4, val5, val6, val7, val8]])
    input_data = np.asarray(out_arr)


    pred = model.predict(input_data)

    result1 = ""
    if pred == [1]:
        result1 = "Bạn đã mắc bệnh tiểu đường"
    else:
        result1 = "Bạn không mắc bệnh tiểu đường"

    return render(request, 'predict.html', {"result2":result1})
