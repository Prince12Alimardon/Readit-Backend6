from django.urls import path
from .views import home_page, blog_page, blog_single


urlpatterns = [
    path('', home_page, name='home'),
    path('blog/', blog_page, name='blog'),
    path('detail/<int:pk>/', blog_single, name='detail')
]

