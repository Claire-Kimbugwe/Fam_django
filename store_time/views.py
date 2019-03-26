from django.shortcuts import render

# Create your views here.
def index(request):
    store = 'Dembe'
    num = 9
    return render(request,'index.html',{"store":store ,'num':num})
def results(request):
    stations = request.args.get('num')
    time = stations * 30
    print(time)
    return render(request,'results.html', {"time":time ,}) 