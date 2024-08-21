from . import views
from django.urls import path

app_name='tweetapp'

urlpatterns = [
    path('', views.listweet, name="listtweet"),
    path('addtweet', views.addtweet,name='addtweet'),
    path('signup' ,views.SingUpView.as_view() , name='signup'),
    path('deleteTweet/<int:id>',views.deleteTweet,name="deleteTweet")
]