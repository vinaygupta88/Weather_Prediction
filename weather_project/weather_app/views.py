import os
import pickle
import numpy as np
from django.shortcuts import render

model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'rfp.pkl')
model = pickle.load(open(model_path, 'rb'))

def index(request):
    return render(request, 'weather_app/index.html')

def about(request):
    return render(request, 'weather_app/about.html')

def predict(request):
    return render(request, 'weather_app/predict.html')

def submit(request):
    if request.method == "POST":
        precipitation = float(request.POST.get('precipitation'))
        maxTemp = float(request.POST.get('maxTemp'))
        minTemp = float(request.POST.get('min-Temp'))
        wind_speed = float(request.POST.get('wind_speed'))

        input_data = np.array([[precipitation, maxTemp, minTemp, wind_speed]])
        result = model.predict(input_data)[0]  # <- Here, result is defined

        return render(request, 'weather_app/submit.html', {'result': result})
    return render(request, 'weather_app/predict.html')