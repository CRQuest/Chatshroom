from django.shortcuts import render


# Create your views here.


def main(request):
    context = {
        'title': 'it worked'
    }

    return render(request, 'Landing Page/index.html', context)



#