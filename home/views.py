from django.shortcuts import render, redirect
from .models import Book, Shoes, Laptop, Electronics, MobilePhone, Clothes
# Create your views here.


def get_home(request):
    books = Book.objects.filter()
    shoess = Shoes.objects.filter()
    laptops = Laptop.objects.filter()
    clothess = Clothes.objects.filter()
    phones = MobilePhone.objects.filter()
    electronics = Electronics.objects.filter()
    return render(request, 'index.html', {'books': books, 'shoess': shoess, 'phones': phones,
                                          'laptops': laptops, 'clothess': clothess, 'electronics': electronics})


def get_home_admin(request):
    books = Book.objects.filter()
    shoess = Shoes.objects.filter()
    laptops = Laptop.objects.filter()
    clothess = Clothes.objects.filter()
    phones = MobilePhone.objects.filter()
    electronics = Electronics.objects.filter()
    return render(request, 'home.html', {'books': books, 'shoess': shoess, 'phones': phones,
                                         'laptops': laptops, 'clothess': clothess, 'electronics': electronics})


def add_book_form(request):
    return render(request, 'add_book.html')


def add_book(request):
    if request.method == 'POST':
        name = request.POST['name']
        img = request.FILES['img']
        desc = request.POST['desc']
        price = request.POST['price']
        amount = request.POST['amount']
        author = request.POST['author']
        publishingCompany = request.POST['publishingCompany']

        book = Book.objects.create(name=name,
                                   img=img,
                                   desc=desc,
                                   price=price,
                                   amount=amount,
                                   author=author,
                                   publishingCompany=publishingCompany
                                   )
        book.save()
    return redirect('http://127.0.0.1:8888/homeadmin/#Book')


def edit_book_form(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'edit_book.html', {'book': book})


def edit_book(request):
    if request.method == 'POST':
        id = request.POST['id']
        book = Book.objects.get(id=id)
        book.name = request.POST['name']
        book.img = request.FILES['img']
        book.desc = request.POST['desc']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.amount = request.POST['amount']
        book.publishingCompany = request.POST['publishingCompany']
        book.save()
    return redirect('http://127.0.0.1:8888/homeadmin/#Book')


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('http://127.0.0.1:8888/homeadmin/#Book')


def add_shoes_form(request):
    return render(request, 'add_shoes.html')


def add_shoes(request):
    if request.method == 'POST':
        name = request.POST['name']
        img = request.FILES['img']
        desc = request.POST['desc']
        price = request.POST['price']
        amount = request.POST['amount']
        size = request.POST['size']
        manufacturer = request.POST['manufacturer']

        shoes = Shoes.objects.create(name=name,
                                     img=img,
                                     desc=desc,
                                     price=price,
                                     amount=amount,
                                     size=size,
                                     manufacturer=manufacturer
                                     )
        shoes.save()
    return redirect('http://127.0.0.1:8888/homeadmin/#Shoes')


def edit_shoes_form(request, id):
    shoes = Shoes.objects.get(id=id)
    return render(request, 'edit_shoes.html', {'shoes': shoes})


def edit_shoes(request):
    if request.method == 'POST':
        id = request.POST['id']
        shoes = Shoes.objects.get(id=id)
        shoes.name = request.POST['name']
        shoes.img = request.FILES['img']
        shoes.desc = request.POST['desc']
        shoes.size = request.POST['size']
        shoes.price = request.POST['price']
        shoes.amount = request.POST['amount']
        shoes.manufacturer = request.POST['manufacturer']
        shoes.save()
    return redirect('http://127.0.0.1:8888/homeadmin/#shoes')


def delete_shoes(request, id):
    shoes = Shoes.objects.get(id=id)
    shoes.delete()
    return redirect('http://127.0.0.1:8888/homeadmin/#shoes')


def add_laptop_form(request):
    return render(request, 'add_laptop.html')


def add_laptop(request):
    if request.method == 'POST':
        name = request.POST['name']
        img = request.FILES['img']
        desc = request.POST['desc']
        price = request.POST['price']
        amount = request.POST['amount']
        hardware = request.POST['hardware']
        insurance = request.POST['insurance']
        manufacturer = request.POST['manufacturer']

        laptop = Laptop.objects.create(name=name,
                                     img=img,
                                     desc=desc,
                                     price=price,
                                     amount=amount,
                                     hardware=hardware,
                                     insurance = insurance,
                                     manufacturer=manufacturer
                                     )
        laptop.save()
    return redirect('http://127.0.0.1:8888/homeadmin/#Laptop')


def edit_laptop_form(request, id):
    laptop = Laptop.objects.get(id=id)
    return render(request, 'edit_laptop.html', {'laptop': laptop})


def edit_laptop(request):
    if request.method == 'POST':
        id = request.POST['id']
        laptop = Laptop.objects.get(id=id)
        laptop.name = request.POST['name']
        laptop.img = request.FILES['img']
        laptop.desc = request.POST['desc']
        laptop.hardware = request.POST['hardware']
        laptop.price = request.POST['price']
        laptop.amount = request.POST['amount']
        laptop.insurance = request.POST['insurance']
        laptop.manufacturer = request.POST['manufacturer']
        laptop.save()
    return redirect('http://127.0.0.1:8888/homeadmin/#Laptop')


def delete_laptop(request, id):
    laptop = Laptop.objects.get(id=id)
    laptop.delete()
    return redirect('http://127.0.0.1:8888/homeadmin/#Laptop')


def add_phone_form(request):
    return render(request, 'add_phone.html')


def add_phone(request):
    if request.method == 'POST':
        name = request.POST['name']
        img = request.FILES['img']
        desc = request.POST['desc']
        price = request.POST['price']
        amount = request.POST['amount']
        insurance = request.POST['insurance']
        manufacturer = request.POST['manufacturer']

        phone = MobilePhone.objects.create(name=name,
                                     img=img,
                                     desc=desc,
                                     price=price,
                                     amount=amount,
                                     insurance = insurance,
                                     manufacturer=manufacturer
                                     )
        phone.save()
    return redirect('http://127.0.0.1:8888/homeadmin/#Phone')


def edit_phone_form(request, id):
    phone = MobilePhone.objects.get(id=id)
    return render(request, 'edit_phone.html', {'phone': phone})


def edit_phone(request):
    if request.method == 'POST':
        id = request.POST['id']
        phone = MobilePhone.objects.get(id=id)
        phone.name = request.POST['name']
        phone.img = request.FILES['img']
        phone.desc = request.POST['desc']
        phone.price = request.POST['price']
        phone.amount = request.POST['amount']
        phone.insurance = request.POST['insurance']
        phone.manufacturer = request.POST['manufacturer']
        phone.save()
    return redirect('http://127.0.0.1:8888/homeadmin/#Phone')


def delete_phone(request, id):
    phone = MobilePhone.objects.get(id=id)
    phone.delete()
    return redirect('http://127.0.0.1:8888/homeadmin/#Phone')


def add_clothes_form(request):
    return render(request, 'add_clothes.html')


def add_clothes(request):
    if request.method == 'POST':
        name = request.POST['name']
        img = request.FILES['img']
        desc = request.POST['desc']
        price = request.POST['price']
        amount = request.POST['amount']
        material = request.POST['material']
        size = request.POST['size']
        manufacturer = request.POST['manufacturer']

        clothes = Clothes.objects.create(name=name,
                                     img=img,
                                     desc=desc,
                                     price=price,
                                     amount=amount,
                                     material=material,
                                     size = size,
                                     manufacturer=manufacturer
                                     )
        clothes.save()
    return redirect('http://127.0.0.1:8888/homeadmin/#clothes')


def edit_clothes_form(request, id):
    clothes = Clothes.objects.get(id=id)
    return render(request, 'edit_clothes.html', {'clothes': clothes})


def edit_clothes(request):
    if request.method == 'POST':
        id = request.POST['id']
        clothes = Clothes.objects.get(id=id)
        clothes.name = request.POST['name']
        clothes.img = request.FILES['img']
        clothes.desc = request.POST['desc']
        clothes.material = request.POST['material']
        clothes.price = request.POST['price']
        clothes.amount = request.POST['amount']
        clothes.size = request.POST['size']
        clothes.manufacturer = request.POST['manufacturer']
        clothes.save()
    return redirect('http://127.0.0.1:8888/homeadmin/#Clothes')


def delete_clothes(request, id):
    clothes = Clothes.objects.get(id=id)
    clothes.delete()
    return redirect('http://127.0.0.1:8888/homeadmin/#Clothes')
