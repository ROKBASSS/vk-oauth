from web_project.settings import SOCIAL_AUTH_VKONTAKTE_EXTRA_DATA
from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404, render_to_response
import vk
# Create your views here.
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader, RequestContext
from django.contrib.auth import logout

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))


# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'vk_oauth/detail.html', {'question': question})


def logout_view(request):
    logout(request)
    return render(request, 'vk_oauth/index.html')


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'vk_oauth/index.html', context)
    return render(request, 'vk_oauth/index.html')


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def friends(request):
    user = request.user
    social = user.social_auth.get(provider='vk-oauth2')
    session = vk.Session(access_token=social.extra_data['access_token'])
    vk_api = vk.API(session)
    friends = vk_api.friends.get(order="random", count=5, fields='photo_200', v="5.124")
    return render(request, 'vk_oauth/friends.html', {"friends": friends['items']})


def get_token(request):
    user = request.user
    social = user.social_auth.get(provider='vk-oauth2')
    return JsonResponse({"access_token": social.extra_data['access_token']})


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
