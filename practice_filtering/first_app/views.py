from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    dummydata = {'name' : 'muzammel', 'age' : 25, 'city' : 'rajshahi', 'lerning' : 'i am lerning django framework', 'date' : datetime.datetime.now()}
    return render(request, 'home.html', dummydata)