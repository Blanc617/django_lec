from django.shortcuts import get_object_or_404, render
from .models import MainContent

def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)

def detail(request, content_id):
    # 단일 콘텐츠 객체를 가져옵니다
    content = get_object_or_404(MainContent, pk=content_id)
    # 템플릿에 단일 콘텐츠 객체를 전달합니다
    context = {'content': content}
    return render(request, 'mysite/content_detail.html', context)
