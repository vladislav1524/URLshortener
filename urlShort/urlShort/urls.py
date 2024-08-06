from django.contrib import admin
from django.urls import path, include
from url import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/register/', views.RegistrationView.as_view(), name='register'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/success_logout.html'),
    #   name='logout'),
    # path('password_reset/',
    #       auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
    #                                             name='password_reset'),
    # path('password_reset/done/', 
    #      auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
    #      name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
    #      name='password_reset_confirm'),
    # path('reset/done/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    #       name='password_reset_complete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('url.urls', namespace='url')),
]
