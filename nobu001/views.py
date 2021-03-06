from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend, Message
# from .forms import HelloForm
from .forms import FriendForm, MessageForm
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import FindForm
from django.db.models import Count,Sum,Avg,Min,Max
from .forms import CheckForm
from django.core.paginator import Paginator



def index(request, num=1):
    data = Friend.objects.all()
    page = Paginator(data, 3)
    params = {
        'title': 'Hello',
        'message': '',
        'data': page.get_page(num),
    }
    return render(request, 'nobu001/index.html', params)

# create model
def create(request):
    params = {
        'title': 'Hello',
        'form': FriendForm()
    }
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/nobu001')
    params = {
        'title': 'Hello',
        'form': FriendForm()
    }
    return render(request, 'nobu001/create.html', params)

def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/nobu001')
    params = {
        'title': 'Hello',
        'id': num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'nobu001/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/nobu001')
    params = {
        'title': 'Hello',
        'id': num,
        'obj': friend,
    }
    return render(request, 'nobu001/delete.html', params)

class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend


def find(request):
    if (request.method == 'POST'):
        msg = request.POST['find']
        form = FindForm(request.POST)
        sql = 'select * from nobu001_friend'
        if (msg != ''):
            sql += ' where ' + msg
        data = Friend.objects.raw(sql)
        msg = sql
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'nobu001/find.html', params)

def check(request):
    params = {
        'title': 'Hello',
        'message': 'check validation.',
        'form': FriendForm(),
    }
    if (request.method == 'POST'):
        obj = Friend()
        form = FriendForm(request.POST, instance=obj)
        params['form'] = form
        if (form.is_valid()):
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good.'
    return render(request, 'nobu001/check.html', params)

def message(request, page=1):
    if (request.method == 'POST'):
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 3)
    params = {
        'title': 'Message',
        'form': MessageForm(),
        'data': paginator.get_page(page),
    }
    return render(request, 'nobu001/message.html', params)










    
    

        

    





