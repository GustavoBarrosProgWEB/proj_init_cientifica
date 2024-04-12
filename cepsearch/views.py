from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from cepsearch.models import Users

def home(request):
    return render(request,'home/index.html')
        
def users(request):
    if (request.method == 'GET'):
        users = Users.objects.all()
        return render(request,'user/users.html', {'users':users})
    if (request.method == 'POST'):
        user = Users()
        user.name = request.POST.get('name')
        user.surname = request.POST.get('surname')
        user.cep = request.POST.get('cep')
        user.rua = request.POST.get('rua')
        user.bairro = request.POST.get('bairro')
        user.cidade = request.POST.get('cidade')
        user.uf = request.POST.get('uf')
        user.save()
        return redirect('users')
    
def usersNew(request):
    return render(request,'user/userNew.html')

def usersNewSave(request):
    user = Users()
    user.name = request.POST.get('name')
    user.surname = request.POST.get('surname')
    user.cep = request.POST.get('cep')
    user.rua = request.POST.get('rua')
    user.bairro = request.POST.get('bairro')
    user.cidade = request.POST.get('cidade')
    user.uf = request.POST.get('uf')
    user.save()
    return redirect('users')

def user(request, id):
    user = Users.objects.get(id=id)
    return render(request,'user/user.html', {'user':user})

def usersEdit(request, id):
    if (request.method == 'POST'):
        user = Users.objects.get(id=id)
        user.name = request.POST.get('name')
        user.surname = request.POST.get('surname')
        user.cep = request.POST.get('cep')
        user.rua = request.POST.get('rua')
        user.bairro = request.POST.get('bairro')
        user.cidade = request.POST.get('cidade')
        user.uf = request.POST.get('uf')
        user.save()
        return redirect('users')
    if (request.method == 'GET'):
        user = Users.objects.get(id=id)
        user.delete()
        return redirect('users')
    
def view_404(request, exception=None):
    return render(request,'error/404.html')
    
def view_500(request):
    return render(request,'error/500.html')