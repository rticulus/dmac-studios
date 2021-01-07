from django.shortcuts import render

news = [
    {
        'author': 'Remzi CI',
        'title': 'First Article',
        'content': 'New newsletter to the masses, hope you like it. <br>Dance is important to the wellbeing and general happiness of all human beings, <br>providing the sport and socialisation that is required for a balanced living',
        'date_posted': 'December 16, 2020'
    },
    {
        'author': 'Tomiaz CI',
        'title': '2nd Article',
        'content': 'New newsletter to the masses, hope you like it. <br>Dance is important to the wellbeing and general happiness of all human beings, <br>providing the sport and socialisation that is required for a balanced living',
        'date_posted': 'December 18, 2020'
    },
    {
        'author': 'Jendi CI',
        'title': '3rd Article',
        'content': 'New newsletter to the masses, hope you like it. <br>Dance is important to the wellbeing and general happiness of all human beings, <br>providing the sport and socialisation that is required for a balanced living',
        'date_posted': 'December 20, 2020'
    },
    {
        'author': 'Fausa CI',
        'title': 'Fourth Article',
        'content': 'New newsletter to the masses, hope you like it. <br>Dance is important to the wellbeing and general happiness of all human beings, <br>providing the sport and socialisation that is required for a balanced living',
        'date_posted': 'December 22, 2020'
    },
    {
        'author': 'Grego CI',
        'title': 'Fifth Article',
        'content': 'New newsletter to the masses, hope you like it. <br>Dance is important to the wellbeing and general happiness of all human beings, <br>providing the sport and socialisation that is required for a balanced living',
        'date_posted': 'December 24, 2020'
    },
]


def home(request):
    context = {
        'news': news
    }
    return render(request, 'newsletter/home.html', context)


def director(request):
        return render(request, 'newsletter/director.html', {'title': 'About'})
