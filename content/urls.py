from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/page/<int:page>/', views.ReviewsList.as_view(),
         name='browse'),
    path('review/<slug:slug>/', views.review_detail, name='review_detail'),
]
