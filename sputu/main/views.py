from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Announcement, Contest, Program
from .forms import ContactForm
from django.contrib import messages


def index(request):
    news = News.objects.order_by('-date_published')[:3]
    announcements = Announcement.objects.order_by('-date_published')[:3]
    contests = Contest.objects.order_by('-deadline')[:3]
    return render(request, 'main/index.html', {
        'news': news, 'announcements': announcements, 'contests': contests
    })

def news_list(request):
    news = News.objects.order_by('-date_published')
    return render(request, 'main/news_list.html', {'news': news})

def news_detail(request, pk):
    article = get_object_or_404(News, pk=pk)
    return render(request, 'main/news_detail.html', {'article': article})

def announcements(request):
    items = Announcement.objects.order_by('-date_published')
    return render(request, 'main/announcements.html', {'items': items})

def contests(request):
    items = Contest.objects.order_by('-deadline')
    return render(request, 'main/contests.html', {'items': items})

def programs(request):
    programs = Program.objects.all()
    return render(request, 'main/programs.html', {'programs': programs})

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            messages.success(request, 'Ваше сообщение отправлено!')
            return redirect('contacts')
    else:
        form = ContactForm()
    return render(request, 'main/contacts.html', {'form': form})