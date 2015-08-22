from django import template
from myapp.models import Member
from django.contrib.auth.models import User

register = template.Library()

@register.inclusion_tag('navbar.html', takes_context=True)
def auth_block(context):
    user = context['request'].user
    member = None
    if user.is_authenticated():
        try:
            member = Member.objects.get(user=user)
        except (Member.DoesNotExist, Member.MultipleObjectsReturned):
            pass
    return member
