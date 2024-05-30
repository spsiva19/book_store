# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import get_user
from django.contrib.auth import authenticate
from django.template import loader
from .models import book_details, user_reg, book_cart
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def book_entry(request):
    return render(request, 'book_entry.html')


def book_post(request):
    if request.method == 'POST':
        new = book_details()

        new.cover = request.POST.get('cover')
        new.bname = request.POST.get('name')
        new.author = request.POST.get('author')
        new.pub_year = request.POST.get('year')
        new.description = request.POST.get('descrip')
        new.save()
        return render(request, 'book_entry.html')
    else:
        template = loader.get_template('book_entry.html')
        message = 'Enter Valid data'
        context = {'message': message}
        return HttpResponse(template.render(context, request))


# Create your views here.
def user_view(request):
    return render(request, 'user_entry.html')


def user_entry(request):
    if request.method == 'POST':
        newuser = user_reg()

        newuser.name = request.POST.get('name')
        newuser.username = request.POST.get('uname')
        newuser.password = request.POST.get('pass')
        newuser.email_id = request.POST.get('email')
        newuser.place = request.POST.get('uplace')
        newuser.save()

        posts = book_details.objects.all().order_by('id')
        p = Paginator(posts, 8)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
        template = loader.get_template('home.html')
        message = 'Registration successful'
        context = {'message': message,'page_obj': page_obj}
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('user_entry.html')
        message = 'Enter Valid data'
        context = {'message': message}
        return HttpResponse(template.render(context, request))


def user_login(request):
    return render(request, 'login.html')


def user_check(request,current_user):
    if request.method=='POST':
        user = request.POST.get('uname')
        passw = request.POST.get('pswd')
        mydata = user_reg.objects.filter(username=user, password=passw).values()
        if mydata:
            mydata = user_reg.objects.filter(username=user, password=passw).all()[0]
            quant =  book_cart.objects.filter(uc_id=mydata.id).count()
            # x = []
            # for i in mydata:
            #    x.append(i['name'])
            

            posts = book_details.objects.all().order_by('id')
            p = Paginator(posts, 8)
            page_number = request.GET.get('page')
            try:
                page_obj = p.get_page(page_number)
            except PageNotAnInteger:
                page_obj = p.page(1)
            except EmptyPage:
                page_obj = p.page(p.num_pages)
            template = loader.get_template('loggedin.html')
            context = {'myuser': mydata.name, 'page_obj': page_obj,'current_user':mydata.id,'quant':quant}
            return HttpResponse(template.render(context, request))
        else:
            template=loader.get_template('login.html')
            message='Check Login Credentials'
            context={'message':message}
            return HttpResponse(template.render(context,request))
    elif request.method=='GET':
        mydata = user_reg.objects.filter(id=current_user).all()[0]
        quant = book_cart.objects.filter(uc_id=mydata.id).count()
        # x = []
        # for i in mydata:
        #    x.append(i['name'])

        posts = book_details.objects.all().order_by('id')
        p = Paginator(posts, 8)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
        template = loader.get_template('loggedin.html')
        context = {'myuser': mydata.name, 'page_obj': page_obj, 'current_user': mydata.id, 'quant': quant}
        return HttpResponse(template.render(context, request))

def book_retrieve(request):
    #bookdata = book_details.objects.all()
    posts = book_details.objects.all().order_by('id')
    p = Paginator(posts, 8)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))


def add_cart(request,bookid,current_user):
    if current_user!=0:
        s=book_cart()
        currentuser=user_reg.objects.filter(id=current_user).all()[0]
        current_book=book_details.objects.filter(id=bookid).all()[0]
        # quant+=1
        s.quantity+=1
        s=book_cart(bc_id=current_book.id,uc_id=currentuser.id,cover=current_book.cover,bname=current_book.bname,
                    author=current_book.author,username=currentuser.username,quantity=s.quantity)
        s.save()
        quant = book_cart.objects.filter(uc_id=current_user).count()
        mydata = user_reg.objects.filter(id=current_user).all()[0]
        # x = []
        # for i in mydata:
        #    x.append(i['name'])

        posts = book_details.objects.all().order_by('id')
        p = Paginator(posts, 8)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
        template = loader.get_template('loggedin.html')
        context = {'myuser': mydata.name, 'page_obj': page_obj, 'current_user': mydata.id,'quant':quant}
        return HttpResponse(template.render(context, request))
    else:
        posts = book_details.objects.all().order_by('id')
        p = Paginator(posts, 8)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
        message = 'Please login to ADD'
        template = loader.get_template('home.html')
        context = {'page_obj': page_obj,'message':message}
        return HttpResponse(template.render(context, request))
def view_cart(request,current_user):
    posts = book_cart.objects.filter(uc_id=current_user).all().order_by('id')
    p = Paginator(posts, 8)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    quant = book_cart.objects.filter(uc_id=current_user).count()
    mydata = user_reg.objects.filter(id=current_user).all()[0]
    template = loader.get_template('cart.html')
    context = {'myuser': mydata.name, 'page_obj': page_obj, 'current_user': mydata.id, 'quant': quant}
    return HttpResponse(template.render(context, request))
def delete_from_cart(request,bookid,current_user):
    try:

        b = book_cart.objects.filter(bc_id=bookid,uc_id=current_user).all()[0]
        b.delete()
    except IndexError:
        message = 'No Book to delete'
        posts = book_cart.objects.filter(uc_id=current_user).all().order_by('id')
        p = Paginator(posts, 8)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
        quant = book_cart.objects.filter(uc_id=current_user).count()
        mydata = user_reg.objects.filter(id=current_user).all()[0]
        template = loader.get_template('cart.html')
        context = {'myuser': mydata.name, 'page_obj': page_obj, 'current_user': mydata.id, 'quant': quant,'message':message}
        return HttpResponse(template.render(context, request))
    posts = book_cart.objects.filter(uc_id=current_user).all().order_by('id')
    p = Paginator(posts, 8)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    quant = book_cart.objects.filter(uc_id=current_user).count()
    mydata = user_reg.objects.filter(id=current_user).all()[0]
    template = loader.get_template('cart.html')
    context = {'myuser': mydata.name, 'page_obj': page_obj, 'current_user': mydata.id, 'quant': quant}
    return HttpResponse(template.render(context, request))
def home(request,current_user):
    quant = book_cart.objects.filter(uc_id=current_user).count()
    mydata = user_reg.objects.filter(id=current_user).all()[0]
    # x = []
    # for i in mydata:
    #    x.append(i['name'])

    posts = book_details.objects.all().order_by('id')
    p = Paginator(posts, 8)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    template = loader.get_template('loggedin.html')
    context = {'myuser': mydata.name, 'page_obj': page_obj, 'current_user': mydata.id, 'quant': quant}
    return HttpResponse(template.render(context, request))

# Create your views here.
