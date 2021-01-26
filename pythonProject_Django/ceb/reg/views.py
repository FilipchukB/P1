from django.shortcuts import render
from django.views.generic.base import View
from .models import Table2, Table1
# from allauth
class Login(View):
    def get(self, request):
        return render(request, 'reg/login.html')
# Create your views here.
class TebleVive(View):
    def get(self, request):
            # if user.is_autheticated:
                tabL = Table2.objects.all()
                tabR = Table1.objects.all()
                context = {
                    'tab_list': tabL, 'tab_L': tabR
                }
                return render(request, "reg/index.html", context)


