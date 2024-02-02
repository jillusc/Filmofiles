from django.urls import path
from . import views
from .views import submit_comment


urlpatterns = [
    path('', views.home, name='home'),
    path('browse/page/<int:page>/', views.ReviewsList.as_view(),
         name='browse'),
    path('review/<slug:slug>/', views.review_detail, name='review_detail'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('submit_comment/<int:review_id>/', views.submit_comment, name='submit_comment'),

]
