from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import ClientProfile
from  django.contrib import messages



def Home(request):
    return render(request, "home.html")


def login(request):
    return render(request, "client_page.html")


def client_login(request):
    return render(request, "client_login_page.html")


def client_registration(request):
    return render(request, "client_reg.html")


def save_client(request):
    if request.method == "POST":
        client_name = request.POST.get("t1")
        company_name = request.POST.get("t2")
        address = request.POST.get("t3")
        business_pro = request.POST.get("t4")
        password = request.POST.get("t7")
        Email = request.POST.get("t5")
        contact = request.POST.get("t6")
        ClientProfile(client_name=client_name, company_name=company_name, password=password, address=address,
                      business_profile=business_pro, email=Email, contact=contact).save()
        return render(request, "client_reg.html", {"msg": "Client Saved..."})


def client_login_check(request):
    email = request.POST.get("l1")
    password = request.POST.get("l2")
    c = ClientProfile.objects.filter(email=email, password=password)
    for x in c:
        id=x.id
    if c:
        request.session["client_id"]=id
        return render(request, "client_home.html")

    else:
        return render(request, "client_login_page.html", {"msg":"Invalid Details"})


def client_profile(request):
    try:
        id = request.session["client_id"]
    except:
        return HttpResponse("session expired")
    else:
        data=ClientProfile.objects.get(id=id)
        return render(request,"client_home.html",{"profile":data})


def client_update(request):
        idno=request.GET.get("id")
        data1=ClientProfile.objects.get(id=idno)
        return render(request, "client_update.html", {"profile": data1})


def logout(request):
    try:
        del request.session["client_id"]
    except:
        return redirect("client_login")
    else:
        return redirect("client_login")


def save_client_update(request):
    id=request.POST.get("u0")
    client_name = request.POST.get("u1")
    company_name = request.POST.get("u2")
    address = request.POST.get("u3")
    business_pro = request.POST.get("u7")
    Email = request.POST.get("u5")
    contact = request.POST.get("u4")
    password = request.POST.get("u6")

    cp=ClientProfile.objects.filter(id=id)
    cp.update(client_name=client_name, company_name=company_name, password=password, address=address,
                      business_profile=business_pro, email=Email, contact=contact)
    return redirect("client_profile")