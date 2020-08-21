from django.shortcuts import render
from .models import Message
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

"""@login_required
def user_detail(request, username):
    user = get_object_or_404(User,
                             username=username,
                             is_active=True)
    received_messages = Message.objects.filter(receiver=user.profile)
    sent_messages = Message.objects.filter(sender=user.profile)
    messages = received_messages.union(sent_messages).order_by('time')
    return render(request, 'private_messages/private_message.html', {'messages': messages})
"""
