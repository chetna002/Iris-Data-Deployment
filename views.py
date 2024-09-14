from django.shortcuts import render
from django.http import HttpResponse
import joblib


# Create your views here.
model= joblib.load(r"C:\Users\uzuma\Desktop\django\sunrise\iris\Final_project_model")
def home(request):
    if request.method=="POST":
        Sepal_length=request.POST['Sepal_length']
        Sepal_width=request.POST['Sepal_width']
        Petal_width=request.POST['Petal_width']
        Petal_length=request.POST['Petal_length']
        y_predict=model.predict([[Sepal_length,Sepal_width,Petal_width,Petal_length]])

        if y_predict==0:
            y_predict="Setosa"
        elif y_predict==1:
            y_predict="Versicolor"
        else:
            y_predict="Viginica"
        return render(request,"iris/home.html",{"Result":y_predict}) 
           
    return render(request,"iris/home.html")