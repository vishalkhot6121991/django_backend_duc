


from django.urls import path
from . views import *
from . form import mychangepasswordform,mypasswordresetform
from django.contrib.auth.views import LogoutView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView


urlpatterns = [
    
    path('',home, name='home'),
    
    path('signup/',singup.as_view(), name='signup'),
    #path('signup/',signup,name='signup'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    
    path('login/',mylogin.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='/login/'),name='logout'),
    path('change-password/',PasswordChangeView.as_view(template_name='core/change-password.html',form_class= mychangepasswordform),name='change-password'),

    path("password_change_done/",PasswordChangeDoneView.as_view(template_name='core/change-password-done.html'),name='password_change_done'),
    path("reset-password/",PasswordResetView.as_view(template_name='core/reset-password.html',form_class=mypasswordresetform),name='reset-password'),
    path('reset-password-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='core/reset-password-confirm.html',form_class =mysetpasswordconfirm),name='password_reset_confirm'),
    path('password-reset-done/',PasswordResetDoneView.as_view(template_name='core/reset-password-done.html'),name='password_reset_done')
   
   
    #path('login/',login,name='login'),
]