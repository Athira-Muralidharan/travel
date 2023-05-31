from django.shortcuts import render
from . models import Place
from . models import Team

# Create your views here.
from django .http import HttpResponse
def demo(request):
    obj=Place.objects.all()
    objs=Team.objects.all()
    return render(request,"index.html",{'result':obj,'results':objs})




#def another(request):
#    return render(request,"another.html")

#def inner(request):
#    return HttpResponse("Nothing to show more")

#def addition(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    res1=x+y
#    res2=x-y
#    res3=x*y
#    res4=x/y

#    return render(request,"result.html",{'result1':res1,'result2':res2,'result3':res3,'result4':res4})
















































