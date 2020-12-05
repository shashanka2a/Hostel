from django.urls import path

from .views import acceptProposals,declineProposals,showProposals,checkstatus,outing_request,home_page,AboutPageView

urlpatterns = [
    path('', home_page, name='home'),
    path('request/',outing_request,name='outing request'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('checkstatus/',checkstatus,name='checkstatus'),
    path('proposals/',showProposals,name='proposals'),
    path('accept/<str:pk>',acceptProposals,name='accept_req'),
    path('reject/<str:pk>',declineProposals,name='reject_req')
]
