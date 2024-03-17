from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
     path('login/', views.login_view, name='login'),
     path('signup/', views.signup_view, name='signup'),
     path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
     path('my-profile/', views.my_profile, name='my_profile'),
     path('edit_review/<int:review_id>/',
          views.edit_review, name='edit_review'),
     path('delete_review/<int:review_id>/',
          views.delete_review, name='delete_review'),
     path('confirm_delete_review/<int:review_id>/',
          views.confirm_delete_review, name='confirm_delete_review'),
     path('edit_comment/<int:comment_id>/',
          views.edit_comment, name='edit_comment'),
     path('delete_comment/<int:comment_id>/',
          views.delete_comment, name='delete_comment'),
     path('confirm_delete_comment/<int:comment_id>/',
          views.confirm_delete_comment, name='confirm_delete_comment'),
]