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
        
        return render(request, 'weather_app/result.html', {'result': result})
    return render(request, 'weather_app/predict.html')
