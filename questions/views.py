from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginate(objects_list, request, per_page=5):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page', 1)
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page

QUESTION_LIST = [
    {
        'id': i,
        'title': f'Вопрос {i}: Как начать работать с Django?',
        'text': f'Только начал изучать Django, подскажите, с чего начать и какие материалы лучше? Вопрос номер {i}.',
    }
    for i in range(1, 30)
]

def index(request):
    page = paginate(QUESTION_LIST, request)
    return render(request, 'questions/index.html', {'page_obj': page, 'questions': page.object_list})

def hot(request):
    page = paginate(QUESTION_LIST[::-1], request)
    return render(request, 'questions/hot.html', {'page_obj': page, 'questions': page.object_list})

def tag(request, tag_name):
    page = paginate(QUESTION_LIST, request)
    return render(request, 'questions/tag.html', {'page_obj': page, 'questions': page.object_list, 'tag': tag_name})

def question(request, question_id):
    answers = [{'id': i, 'text': f'Ответ номер {i}. Это тестовый ответ.'} for i in range(1, 15)]
    page = paginate(answers, request)
    return render(request, 'questions/question.html', {'page_obj': page, 'answers': page.object_list, 'question_id': question_id})

def ask(request):
    return render(request, 'questions/ask.html')
