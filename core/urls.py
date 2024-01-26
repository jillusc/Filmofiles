from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path('review/edit/<int:review_id>/', views.edit_review,
         name='edit_review'),
    path('review/delete/<int:review_id>/', views.delete_review,
         name='delete_review'),
    path('comment/edit/<int:comment_id>/', views.edit_comment,
         name='edit_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment,
         name='delete_comment'),
    path('delete-account/', views.delete_account, name='delete_account'),
]
