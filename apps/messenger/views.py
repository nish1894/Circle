from allauth.core.internal.httpkit import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from apps.messenger.forms import ChatMessageCreateForm
from apps.messenger.models import *


# Create your views here.

@login_required
def chat_view(request):
    chat_group= get_object_or_404(ChatGroup, group_name = "public-chat")
    chat_messages = chat_group.group_message.all()[:30]
    form = ChatMessageCreateForm()

    if request.htmx:
        form = ChatMessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit = False) # not saved in database
            message.author = request.user
            message.group = chat_group
            message.save()
            context = {
                'message' : message,
                'user' : request.user
            }
            return render(request,'messenger/partials/chat_message_part.html',context )
    context = {
                'chat_messages': chat_messages,
                'form' : form
    }

    return render(request,'messenger/chat.html',  context)
