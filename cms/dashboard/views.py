from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from .forms import MyAuthentication
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
# Create your views here.

class Home(LoginRequiredMixin,View): 
    name = 'home'
    template_name ='dashboard/pages/home.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    def get(self, request):
        context = {

        'name':self.name,
  
        }
        return render(request,self.template_name,context)



class UserLogin(LoginView):
    form_class  =MyAuthentication
    template_name = 'dashboard/pages/login_test.html'
    login_url = 'login'
    def form_valid(self, form):
        """Security check complete. Log the user in."""
        user = authenticate(self.request,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
        if user is not None:
            if (user.is_active == True) or (user.is_active == True and user.is_admin == True) or (user.is_superuser==True):
                login(self.request,user)
                print('true')
                return redirect('home')
            else:
                
                return render(self.request,'dashboard/pages/login.html')
    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        print('invalid')
        return self.render_to_response(self.get_context_data(form=form))

