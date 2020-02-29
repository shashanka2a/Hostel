from django.views.generic import TemplateView
from django.shortcuts import render
from users.models import CustomUser,Request,Partners
from users.forms import UserOutingForm
from django.contrib.auth.decorators import login_required

#
# class HomePageView(TemplateView):
#     template_name = 'pages/home.html'


@login_required
def home_page(req):
    if req.user.is_superuser:
        return render(req,'pages/admindash.html')
    return render(req,'pages/home.html')

def showProposals(req):
    proposal_list = Request.objects.all()
    context = {'proposals': proposal_list}
    return render(req, 'pages/proposals.html', context)

def outing_request(req):
    form = UserOutingForm(req.POST or None)
    if form.is_valid():
        form.save()
    content = {
        'username' : req.user,
        'form' : form
    }
    return  render(req,'pages/form_template.html',content)

def acceptProposals(req):
    """  proposals = Request.objects.filter(from_user = req.user)

    for proposal in proposals.all():
        newpartner.user = proposal.get(user=proposal.user)
        newpartner.when = proposal.when
        newpartner.return_date = proposal.return_date
        newpartner.place = proposal.place
        newpartner.purpose = proposal.purpose
    newpartner.save()
    proposal.delete()"""
    proposal = Request.objects.filter(from_user=req.user)
    proposal.assigned_to = 'accepted'
    content = {'status': proposal.assigned_to}
    proposal.delete()
    return render(req,'pages/proposals.html',content)

def checkstatus(req):
    #request_list = Request.objects.filter(from_user = req.user)
    proposal = Request.objects.filter(from_user=req.user)
    content = {'request': proposal}
    return render(req,'pages/checkstatus.html',content)



def declineProposals(req):
    proposal = Request.objects.filter(from_user = req.user)
    proposal.delete()
    return render(req,'pages/proposals.html')

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


