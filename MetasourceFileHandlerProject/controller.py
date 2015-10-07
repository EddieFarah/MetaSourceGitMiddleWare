import json

__author__ = 'Edie'


from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

from django.core import serializers

from github import *
from django.views.decorators.csrf import csrf_exempt

class Object:
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

def UserInfo(request,user_name):
    gh = GitHub()

    return JsonResponse({'status':'success','result':gh.users(user_name).get()})

def RepoInfo(request,user_name):
    gh = GitHub()

    return JsonResponse({'status':'success','result':gh.users(user_name).repos.get()})

def RepoContent(request,user_name,repo_name):
    gh = GitHub()

    return JsonResponse({'status':'success','result':gh.repos(user_name)(repo_name).contents.get()})

@csrf_exempt
def CreateRepo(request):
    gh = GitHub(username="EdieFarahKuhcoon",password="Ed!ek251989")
    repo_name = request.POST['name']
    return JsonResponse({'status':'success','result':gh.user.repos.post(name=repo_name)})