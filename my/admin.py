from django.contrib import admin

from my.models import userbio,userpost

class userbioAdmin(admin.ModelAdmin):
    list_display=["name","username"]

admin.site.register(userbio,userbioAdmin)
class userpostAdmin(admin.ModelAdmin):
    list_display=['username',"age"]

admin.site.register(userpost,userpostAdmin)
