from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from Courriers.models import Book
from Courriers.forms import BookForm
from braces.views import LoginRequiredMixin
from django.views.generic import ListView, View, TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.forms.models import model_to_dict
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.template.loader import render_to_string



from pandas import *


def indexView(request):
    return render(request,'index.html')

class registerView(FormView):
    template_name='registration/register.html'
    success_url=reverse_lazy('login')
    form_class=UserCreationForm
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

class passwordresetView(FormView):
    template_name="registration/passwordreset.html"
    success_url=reverse_lazy('login')
    form_class=PasswordResetForm

def setpasswordView(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            return redirect('login')

    else:
        form=PasswordChangeForm(request.user)
    return render(request,'registration/setpassword.html',{'form':form})

@permission_required(('auth.add_user','auth.change_user',
    'auth.delete_user','auth.view_user','auth.add_permission','auth.change_permission',
    'auth.delete_permission','auth.view_permission'),login_url='index')
def administrationView(request):
    return render(request,'registration/administration.html')

class administrationuser_createView(CreateView):
    model=User
    fields="__all__"
    template_name="registration/administrationuser_create.html"
    success_url=reverse_lazy('administrationuser_list')

class administrationuser_listView(ListView):
    model = User
    liste=User.objects.all()
    template_name="registration/administrationuser_list.html"

class administrationuser_updateView(UpdateView):
    template_name="registration/administrationuser_update.html"
    model = User
    success_url=reverse_lazy('administrationuser_list')
    fields="__all__"

class administrationuser_deleteView(DeleteView):
    template_name="registration/administrationuser_delete.html"
    model = User
    success_url=reverse_lazy('administrationuser_list')
    fields="__all__"

def book_list(request):
	books = Book.objects.all()
	context = {
	'books': books
	}
	return render(request, 'book_list.html',context)

def save_all(request,form,template_name):
	data = dict()
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			data['form_is_valid'] = True
			books = Book.objects.all()
			data['book_list'] = render_to_string('book_list_2.html',{'books':books})
		else:
			data['form_is_valid'] = False
	context = {
	'form':form
	}
	data['html_form'] = render_to_string(template_name,context,request=request)
	return JsonResponse(data)

def book_create(request):
	if request.method == 'POST':
		form = BookForm(request.POST)
	else:
		form = BookForm()
	return save_all(request,form,'book_create.html')

def book_update(request,id):
	book = get_object_or_404(Book,id=id)
	if request.method == 'POST':
		form = BookForm(request.POST,instance=book)
	else:
		form = BookForm(instance=book)
	return save_all(request,form,'book_update.html')

def book_delete(request,id):
	data = dict()
	book = get_object_or_404(Book,id=id)
	if request.method == "POST":
		book.delete()
		data['form_is_valid'] = True
		books = Book.objects.all()
		data['book_list'] = render_to_string('book_list_2.html',{'books':books})
	else:
		context = {'book':book}
		data['html_form'] = render_to_string('book_delete.html',context,request=request)

	return JsonResponse(data)

def searchView(request):
    query=request.POST.get('qu')
    liste=Book.objects.filter(Q(objet=query)|Q(n_courrier=query)).order_by('date_reception')
    count=liste.count()
    paginator=Paginator(liste,4)
    page=request.POST.get('page')
    courriers=paginator.get_page(page)
    return render(request,'search.html',{'liste':liste,'query':query,'count':count,'courriers':courriers})


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt





# Create your views here.
