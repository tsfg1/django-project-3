from django.shortcuts import render
import requests
import json

# Create your views here.

def home(request):
    api_request = requests.get('http://api.github.com/users?since=0')
    api = json.loads(api_request.content)
    return render(request, 'home.html', {"aaa":api}) #注意此处aaa和home.html中的aaa相对应


def user(request):
    if request.method == 'POST': #如果获取到该请求是POST方式
        user = request.POST.get('nnn') #此处与base.html中【①】相对应
        
        api_request = requests.get('http://api.github.com/users/'+user)
        userinfo = json.loads(api_request.content)   

        return render(request, 'user.html', {'userinfo':userinfo})
    else:#如果获取到该请求是GET方式
        nonTip = 'method is ' + request.method +', '+  '请输入name后点击搜索...'
        return render(request, 'user.html', {'nonTip':nonTip})


