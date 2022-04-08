from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from home.models import Product, Orders
from math import ceil

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is home page")


def items(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'items.html', params)


def login(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(
            username=first_name, email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("items")
        else:
            messages.info(request, 'invalid credentials')
            return redirect("/login")

    else:
        return render(request, 'login.html')


def index_2(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        password1 = request.POST['password1']

        if User.objects.filter(email=email).exists():
            messages.info(request, 'email already taken')
            return redirect("index_2")
        else:
            user = User.objects.create_user(
                email=email, first_name=first_name, password=password1, username=first_name,)
            user.save()
            messages.info(
                request, 'user created now you can login from login page')
            return redirect("login")
    else:
        return render(request, 'index_2.html')


def about(request):
    return render(request, 'about.html')


def help(request):
    return render(request, 'help.html')


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + \
            " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email,
                       address=address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'checkout.html', {'thank': thank, 'id': id})
    return render(request, 'checkout.html')


def productView(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'prodView.html', {'product': product[0]})


def category(request):
    pass

    # username=kapil
    # password=kap@123il
