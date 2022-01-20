from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

def Home(request):
    return render(request, 'plantilla/index.html')

class LoginFormViews(LoginView):
  template_name = 'plantilla/login.html'

  def dispatch(self, request, *args, **kwargs):
      print('request.user :',request.user)
      if request.user.is_authenticated:
        return redirect('home')
      return super().dispatch(request, *args, **kwargs)

  def get_context_data(self,**kwargs):
      context = super().get_context_data(**kwargs)
      context['title'] = 'Iniciar sesion'
      return context