from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from ..accounts.forms import UsuarioForm
from django.urls import reverse_lazy


# Create your views here
def user_login(request):
    template_name = 'login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(login(request, user))
            return redirect('core:index')
        else:
            return render(request, 'login.html')
    return render(request, template_name, {})


class CreateUser(CreateView):
    template_name = 'user_form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('accounts:user_login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Titulo'] = "Cadastrar novo usuario"
        context['botao'] = 'Cadastrar'
        return context
