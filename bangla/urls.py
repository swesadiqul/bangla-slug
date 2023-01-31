from django.urls import path
from .views import *


#create path
urlpatterns = [
    path('', homepage, name = 'homepage'),
    path('post/<slug>/', post, name = 'post'),
    path('about/', about,name = 'about' ),
    path('postlist/<slug>/', postlist, name = 'postlist'),
    path('posts/', allposts, name = 'allposts'),
    path('search/', search, name = 'search'),

]
