from django.shortcuts import render, HttpResponse, redirect
from .models import comment, content
from django.utils import timezone

sourceUrl = ''


# Create your views here.
def index(request):
    shj = content.objects.all()
    message = comment.objects.all()
    global sourceUrl
    sourceUrl = request.path
    return render(request, 'index.html', {'shj': shj, 'message': message})


def submitComment(request):
    text = request.POST['text']
    if not text.strip():
        return HttpResponse('<a href="' + sourceUrl + '">留言内容不可为空</a>')
    timeNow = timezone.now().strftime('%Y-%m-%d %H:%M')
    submit = {'content': text, 'time': timeNow}
    print(submit)
    comment.objects.create(**submit)
    return HttpResponse('<a href="' + sourceUrl + '">留言成功</a>')
