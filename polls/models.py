from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text+" "+self.pub_data

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    #Question fk관계 을 같게되며 Chicedml 는 question id 라는 이름으로
    #Question주인 이고 Choice노예? 라는 관계를 나타내며
    #on_delete 옵션으로 Question 이삭제 하면 Choice 도 삭재된다 외래키!
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# test 방법
#python manage.py shell
# from polls.models import Question, Choice
#Question.objects.all()
#from django.utils import timezone
#Question.objects.create(question_text='A',pub_date=timezine.now())
#
# q= Question(question_text='점심은',pub_date=timezone.now())
# q.save()
# c=Choice(choice_text='짜장',votes=1, question=q)
# c.save()
#q.datate

# q = Question.objects.get(question_text='좋은 언어는?')
# q.choice_set.all()

#insert
#Question.objects.create(question_text='A',pub_date=timezine.now())
#q= Question(question_text='점심은',pub_date=timezone.now())
#q.save()