from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import *
from users.views import *

# Create your views here.

def index(request):
    return render(request, 'index.html', {'check' : True})

@login_required
def after_login(request):
    user = request.user
    context = {
                'client':user,
                'check' : False
            }
    try:
        acc_type = AccType.objects.get(user=user)
        if acc_type.type == 'serviceprovider':
            try:
                status = ProfileStatus.objects.get(user=user)
            except:
                return redirect('users:profile')
        else:
            return render(request, 'index.html', context=context)
        return render(request, 'index.html', context=context)
    except:
        pass

