from django.urls import path, include
from . import views

urlpatterns = [
    # boiler
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # finches
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finch/<int:pk>/update/',
         views.FinchUpdate.as_view(), name='finches_update'),
    path('finch/<int:pk>/delete/',
         views.FinchDelete.as_view(), name='finches_delete'),

    # feeding
    path('finches/<int:finch_id>/add_feeding/',
         views.add_feeding, name='add_feeding'),

    # toys
    path('finches/<int:finch_id>/assoc_toy/<int:toy_id>/',
         views.assoc_toy, name='assoc_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/',
         views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/',
         views.ToyDelete.as_view(), name='toys_delete'),

    # photos
    path('cats/<int:cat_id>/add_photo/', views.add_photo, name='add_photo'),

    # signup
    path('accounts/signup/', views.signup, name='signup'),

]
