from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete_review/<int:review_id>/',
         views.delete_review, name='delete_review'),
]
