from django.conf.urls import url
from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
#from django.contrib.auth.views import PasswordChangeView as pwd_change, PasswordChangeDoneView as pwd_change_done, PasswordResetView as reset, PasswordResetDoneView as reset_done, PasswordResetConfirmView as reset_confirm, PasswordResetCompleteView as reset_complete
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'portfolio'
urlpatterns = [

    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),

    url(r'^register/$', views.register, name='register'),

    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('portfolio:password_change_done')), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('portfolio:password_reset_done')), {'email_template_name': 'registration/password_reset_email.html'}, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('portfolio:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('stock_list', views.stock_list, name='stock_list'),
    path('stock/create/', views.stock_new, name='stock_new'),
    path('stock/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),
    path('investment_list', views.investment_list, name='investment_list'),
    path('investment/create/', views.investment_new, name='investment_new'),
    path('investment/<int:pk>/edit/', views.investment_edit, name='investment_edit'),
    path('investment/<int:pk>/delete/', views.investment_delete, name='investment_delete'),
    path('customer/<int:pk>/portfolio/', views.portfolio, name='portfolio'),
    url(r'^customers_json/', views.CustomerList.as_view()),
    path('customer/<int:pk>/portfolio/pdf/', views.customer_portfolio_pdf, name='customer_portfolio_pdf'),
    path('customer/<int:pk>/portfolio/email_pdf/', views.customer_portfolio_email_pdf, name='customer_portfolio_email_pdf'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
