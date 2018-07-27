from django.shortcuts import render

# Create your views here.
# Вывод начальной страницы
def index(request):
    return render(request, 'htmlpage/homepage.html')
