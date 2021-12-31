from django.shortcuts import render


def index(request):
    room_name = "main"
    return render(request, 'chat/index.html', {'room_name': room_name})




