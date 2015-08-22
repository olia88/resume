from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display=['__unicode__', 'timestamp', 'first_name']
    class Meta:
        model=Member

admin.site.register(Member, MemberAdmin)

