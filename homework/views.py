from django.shortcuts import render


def homework_view(request):
    return render(request, "homework/homework.html")
