#encoding:utf-8
# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from users.models import UserPofile
from django.contrib.auth.decorators import login_required
import json
from captcha.models import CaptchaStore

def sign_in(request):
    is_login = False
    message = {}
    if request.user.is_authenticated():     
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        captcha = request.POST['captcha']
        captcha_key = request.POST['captcha_key']
        
        #校验captcha
        captcha_obj = CaptchaStore.objects.get(hashkey=captcha_key)
        if captcha_obj.response != captcha.lower():
            message['warning'] = '验证码错误'
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    is_login = True
            else:
                message['warning'] = '用户名密码不匹配'

            
    if is_login:
        return render(request, 'index.html')
    else:
        captcha_key = CaptchaStore.generate_key()
        captcha_url = captcha_image_url(captcha_key)
        captcha_dict = {
        'captcha_key':captcha_key,
        'captcha_url':captcha_url,
        'message':message,
        }
        
        return render(request, 'users/signin.html', captcha_dict)
        

def sign_out(request):
    logout(request)
    return redirect('sign')


def _get_user_profile(request):
    user_profile = None
    if request.user.is_authenticated():
        user_profile = UserPofile.objects.get(user=request.user)
    return user_profile

@login_required
def get_user_profile(request):
    '''
    获取用户信息
    '''
    if request.method == 'GET':
        user_profile = _get_user_profile(request)
        active_page = 'profile'
        return render(request, 'users/profile.html', {'user_profile':user_profile, 'active_page':active_page})
        
    else:
        pass

def get_login_user(request):
    '''
    获取当前用户信息
    '''
    if not request.is_ajax():
         raise Http404

    user_profile = _get_user_profile(request)
    if user_profile:        
        to_json_response = {
            'username': user_profile.user.username,
            'usertype': user_profile.user_type,
            'profile_image_url_s':'img_%s_s'%user_profile.code
        }
    else:
        to_json_response = {}
    return HttpResponse(json.dumps(to_json_response), content_type='application/json')

def create_user(request):
    '''
    创建用户
    @desc 管理员权限的人分配添加账号
    '''    
    if request.method == 'POST':
        username = request.POST['username']
        code = request.POST['code']
        user_type = request.POST['user_type']
        belong_to_id = request.POST['belong_to_id']

        #default_pass
        default_pass = '11111111'

        #Todo
        pass

        return 
        