#encoding:utf-8
# Create your views here.
from django.shortcuts import redirect, render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from users.models import UserPofile
from django.contrib.auth.decorators import login_required
import json
from captcha.models import CaptchaStore
from sequence.views import get_unique_code
from django.db.transaction import commit_on_success
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
            'user_type': user_profile.user_type,
            'profile_image_url_s':'img_%s_s'%user_profile.code
        }
    else:
        to_json_response = {}
    return HttpResponse(json.dumps(to_json_response), content_type='application/json')

def ajax_get_login_user_type(request):
    '''
    获取当前用户信息
    '''
    if not request.is_ajax():
         raise Http404

    user_profile = _get_user_profile(request)
    if user_profile:        
        to_json_response = {
            'user_type': user_profile.user_type,
            
        }
    else:
        to_json_response = {}
    return HttpResponse(json.dumps(to_json_response), content_type='application/json')
    

@login_required
@commit_on_success
def create_user(request):
    '''
    创建用户
    @desc 管理员权限的人分配添加账号
    '''    
    if request.method == 'POST':
        username = request.POST['username']
        user_type = request.POST['user_type']
        

        #default_pass
        default_pass = username   
        user = User.objects.create_user(username, '%s@wm.com'%username, username)

        user_profile = get_object_or_404(UserPofile, user=user)
        user_profile.user_type = user_type

        user_profile.code = get_unique_code(user_type)
        user_profile.belong_to_id = request.user.id
        
        user_profile.save()

        return redirect('list-users')
    else:

        return render(request, 'users/create_user.html')

@login_required
def list_users(request):
    '''
    show users
    '''
    if request.method == 'POST':
        #TODO
        pass

    else:
        order_by = request.GET.get('order_by', '')
        order_bys = ['-id']
        if order_by == 'user_type':
            order_bys.append('user_type')
        elif order_by == 'active':
            order_bys.append('user__is_active')
        else:
            pass

        #div privilege
        # admin see all
        # employee see his and his employee
        # employee and customer could see nothing

        cur_user = request.user
        if cur_user.is_superuser:
            user_profiles = UserPofile.objects.all().order_by(*order_bys)
        else:
            user_profiles = UserPofile.objects.filter(belong_to = cur_user).order_by(*order_bys)

        data = [dict(zip(('username', 'user_type', 'is_active', 'code'), 
            (u_p.user.username, u_p.user_type, u_p.user.is_active, u_p.code))) for u_p in user_profiles]
                
        # return render_to_response('users/userinfo.html', {'users':data})
        return render(request, 'users/userinfo.html', {'users':data})

def edit_user_info(request, user_id):
    '''
    edit user's info 
    '''        
    if request.method == 'POST':
        #TODO
        pass

    else:
        pass

def show_user_info(request, user_id=0):
    '''
    show user's info
    '''
    if request.method == 'POST':
        pass
    else:
        #TODO
        return render(request, 'users/userinfo.html')

def ajax_get_user_info_by_usercode(request):
    '''
    
    '''
    if not request.is_ajax():
         raise Http404

    code = request.GET['code']
    user_profile = get_object_or_404(UserPofile, code=code)
    to_json_response = {
            'username': user_profile.user.username,
            'user_type': user_profile.user_type,
            'is_active':'Y' if user_profile.user.is_active else 'N',
            'code':user_profile.code,
    }
    return HttpResponse(json.dumps(to_json_response), content_type='application/json')

def change_password(request, user_id):
    '''
    change user 's password
    '''
    if request.method == 'POST':
        pass
    else:
        pass

def reset_password(request, user_id):
    '''
    reset password 
    '''
    if request.method == 'POST':
        pass
    else:
        pass