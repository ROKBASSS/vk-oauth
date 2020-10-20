from vk_oauth.views import friends
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # logout
    path('logout/', views.logout_view, name='logout'),
    # friends
    path('friends', views.friends, name='friends'),
    # get token for js
    path('get_token', views.get_token, name='access_token')
]