from django.views.generic import TemplateView
from django.shortcuts import render
from users.models import CustomUser,Request
from users.forms import UserOutingForm
from django.contrib.auth.decorators import login_required

#
# class HomePageView(TemplateView):
#     template_name = 'pages/home.html'

@login_required
def home_page(req):
    """user_details = CustomUser.objects.get(username=req.user)
    data = {
        'username' : req.user,
        'phone' : user_details.phone
    }
    return render(req,template_name='pages/home.html',context=data)"""
    form = UserOutingForm(req.POST or None)
    if form.is_valid():
        form.save()

    content = {
        'username' : req.user,
        'form' : form
    }
    return render(req,'pages/home.html', content)

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


