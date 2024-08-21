from django.contrib import admin
from tweetapp.models import Tweet
# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fields=['message' ,'username']


admin.site.register(Tweet,TweetAdmin)
