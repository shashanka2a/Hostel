from django.urls import path

from .views import acceptProposals,declineProposals,showProposals,checkstatus,outing_request,home_page,AboutPageView

urlpatterns = [
    path('', home_page, name='home'),
    path('request/',outing_request,name='outing request'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('checkstatus/',checkstatus,name='checkstatus'),
    path('proposals/',showProposals,name='proposals'),
    path('proposals/accept',acceptProposals,name='Accept proposal'),
    path('proposals/reject',declineProposals,name='Reject proposal')
]
