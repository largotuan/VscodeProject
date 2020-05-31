from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Question
from .forms import RegistrationForm
def index(request):
    myname = "Ngoc Tuan"
    taisan1 = ["Dien thoai", "May Tinh", "May Bay", "Nhieu tien"]
    context = {"name": myname, "taisan": taisan1}
    return render(request, "polls/index.html", context)

def viewlist(request):
    #get_object_or_404(request)
    list_question = Question.objects.all()
    context = {"dsquest": list_question}
    return render(request, "polls/question_list.html", context)
def detailView(request, question_id):
    q = Question.objects.get(pk = question_id)
    return render(request, "polls/detail_question.html", {"qs" : q})
def vote(request, question_id):
    q = Question.objects.get(pk = question_id)
    try:
        dulieu = request.POST["choice"]
        c=q.choice_set.get(pk=dulieu)
    except:
        HttpResponse("Loi khong co choice")
        c.vote+=1
        c.save()
    return render(request, "polls/result.html", {"q" : q})#q de hien thi url, vd polls/5
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'polls/register.html', {'form': form})