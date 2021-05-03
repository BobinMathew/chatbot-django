from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .chatbot import activate
import json


# Create your views here.
ans_list = []
def home(request):
    if request.method == 'POST':
        # print(request.GET.get('que'))
        ques = request.POST.get('que')  # ['que']
        # ans_list.append(f'You : {ques}')
        # print("ques =", ques)
        ans = activate(ques)
        ques = f'You : {ques}'
        # print(ans)
        # ans_list.append(ans)
        # context = {'ans': ans_list}
        # return render(request, 'home.html', context)
        # return HttpResponse(
        #     json.dumps({
        #         'ques': ques,
        #         'ans': ans
        #     }),
        #     content_type="application/json"
        # )
        return JsonResponse({
                'ques': ques,
                'ans': ans
            })
    return render(request, 'home.html')

