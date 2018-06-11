from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse


def login(request):
    return render(request, 'chat/index.html')


def main(request, user=None):
    context = {
        'user': user
    }

    if not user:
        return HttpResponseRedirect(reverse('blog:login'))

    return render(request, 'chat/main.html', context)


def login_submit(request):
    return HttpResponseRedirect(reverse('blog:main',
                                        kwargs={'user': request.POST['username']}))