from django.http import HttpResponse
from django.shortcuts import render
from .chatbot import activate


# Create your views here.
def home(request):
    if request.method == 'POST':
        # print(request.GET.get('que'))
        ques = request.POST.get('que')  # ['que']
        # print("ques =", ques)
        ans = activate(ques)
        # print(ans)
        context = {'ans': ans}
        return render(request, 'home.html', context)
    return render(request, 'home.html')
