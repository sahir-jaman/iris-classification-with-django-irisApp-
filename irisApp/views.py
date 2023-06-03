from django.shortcuts import render
from joblib import load 

model = load('./savedModels/model.joblib')

# Create your views here.
def predictor(request):
    return render(request,'main.html' )

def formInfo(request):
    speal_lenth = request.GET['sepal_lenth']
    speal_width = request.GET['sepal_width']
    petal_lenth = request.GET['petal_lenth']
    petal_width = request.GET['petal_width']
    y_pred = model.predict([[speal_lenth, speal_width, petal_lenth, petal_width]])
    if y_pred[0] == 0:
        y_pred = 'Setosa'
    elif y_pred[0] == 1:
        y_pred = 'VersiColor'
    else:
        y_pred = 'Virginica'
    return render(request, 'result.html', {'result': y_pred})