from django.shortcuts import render, redirect
from Book.models import Book
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    all_books = Book.active_objects.all()
    # print(all_books)
    return render(request,template_name='home.html',context={"books":all_books})

def save_book(request):
    #print("in save book")
    #print(request.POST)
    book_obj = Book.objects.get(id=request.POST.get("id"))
    b_name = request.POST.get("name")
    b_author = request.POST.get("auth")
    b_qty = request.POST.get("qty")
    b_price = request.POST.get("price")
    b_pub = request.POST.get("pub")
    #print(b_name,b_author,b_qty,b_price,b_pub)
    if b_pub == "on":
        flag = True
    else:
        flag = False
    if request.POST.get("id"):
        book_obj.name = b_name
        book_obj.author = b_author
        book_obj.qty = b_qty
        book_obj.price = b_price
        book_obj.is_published = flag
        book_obj.save()
        return redirect('welcome')
    else:
        b =Book(name=b_name,author=b_author,qty=b_qty,price=b_price,is_published=flag)
        b.save()
        return redirect('welcome')

def edit_book(request, id):
    try:
        book_obj = Book.objects.get(id=id)
    except Exception:
        msg = f"Book Not Found For ID: {id}"
        return HttpResponse(msg)

    all_books = Book.active_objects.all()
    return render(request,template_name='home.html',context={"book":book_obj,"books":all_books})

def delete_book(request, pk):   #primary key
    book_obj = Book.objects.get(id=pk)
    #book_obj.delete()
    book_obj.is_deleted = "Y"
    book_obj.save()
    return redirect('welcome')

def hard_delete_book(request, pk):   #primary key
    book_obj = Book.objects.get(id=pk)
    book_obj.delete()
    return redirect('welcome')

def show_deleted_data(request):
    all_deleted_books = Book.inactive_objects.all()
    return render(request,template_name='home.html',context={"books":all_deleted_books})

def restore_data(request, id):
    book_obj = Book.objects.get(id=id)
    book_obj.is_deleted = "N"
    book_obj.save()
    return redirect('welcome')

def restore_all_data(request):
    book_obj = Book.inactive_objects.all().update(is_deleted="N")
    return redirect('welcome')

def soft_delete_all(request):
    book_obj = Book.active_objects.all().update(is_deleted="Y")
    return redirect('welcome')
    