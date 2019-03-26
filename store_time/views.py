from django.shortcuts import render
from store_time.models import Family

# Create your views here.
def index(request):
    store = 'Dembe'
    num = 9
    families = Family.objects.all().order_by('name')
    # how to filter
    kim = Family.objects.filter(name__contains='Kim')
    return render(request,'index.html', {"store":store ,'num':num,
                                         'families':families,'kim':kim})

def results(request):
    stations = request.args.get('num')
    time = stations * 30
    print(time)
    return render(request,'results.html', {"time":time ,}) 