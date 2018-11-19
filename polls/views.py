from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from polls.models import *
def save(request, question_id):
    q=request.POST['q']
    question = Question.objects.get(id=question_id)
    question.question_text = q
    question.save()
    return HttpResponse('수정완료')

def edit(request,question_id):
    q = Question.objects.get(id=question_id)
    return render(
        request,'polls/edit.html',{'q':q}
    )

def index(request):
    q=Question.objects.all()
    return render(request,'polls/index.html',{'question':q})
    # q = Question.objects.all()[0]
    # choices = q.choice_set.all()
    #
    # print(q.question_text)
    # print(choices[0].choice_text)
    # print(choices[1].choice_text)
    # print(choices[2].choice_text)
    # return HttpResponse('polls index')

def vote(request,question_id):
    q = Question.objects.get(id=question_id)
    try:
        select = request.POST['select']
        c = q.choice_set.get(id=select)
        c.votes +=1
        c.save()
        print(select)
    except:
        pass
    # return HttpResponse('OK!')
    return render(request,'polls/result.html',{'q':q})

def detail(request, question_id):
    q=Question.objects.get(id=question_id)
    c=q.choice_set.all()
    choice=''
    for a in c:
        choice +=" "+a.choice_text
    #     request 템플릿 컨덱스트(데이터/모델)
    return render(
        request,
        'polls/detail.html',
        {
            'question':q.question_text,
            'num':q.id,
            'choice':c
        }
    )
    # return HttpResponse(q.question_text+'<br>'+choice)

def detail2(request, num1,num2):
    return HttpResponse(num1+num2)




