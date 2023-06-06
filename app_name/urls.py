from django.urls import path

urlpatterns = [
    path('', indexing_view, name='indexing_view'),
]