from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def start(request):
    return render(request,"input.html",{})
def output(request):
    x = int(request.GET["t1"])
    y = int(request.GET["t2"])
    opr = request.GET["t3"]
    z = 0
    if opr == "ADD":
        z = x+y
    elif opr == "SUB":
        z = x-y
    elif opr == "MUL":
        z = x*y
    else:
        z = x/y
    res = HttpResponse("The result is "+str(z))
    return res

