#encoding:utf-8
from django.shortcuts import redirect, render
import json
from django.contrib.auth.decorators import login_required
from store.models import Good
from django.http import HttpResponse
def home(request):
    '''
    random 15 goods
    随机展示15个商品
    '''
    if request.method == 'GET':
        goods = Good.objects.order_by('?')[:5]
    
        return render(request, 'manage/store/random_goods.html', {'goods':goods})
    

    return  HttpResponse('store home')

@login_required
def goods_list(request):
    if request.method == 'GET':
        goods = Good.objects.filter(belong_to=request.user)
    
        return render(request, 'manage/store/goods_list.html', {'goods':goods})


def add_goods(request):
    '''
    add good
    '''
    if request.method == 'POST':
        name = request.POST['name']
        num = request.POST['num']
        good_type = request.POST['good_type']

        # add session info and so on 

        return redirect('home')

    else:
        pass

def add_good_type(request):
    '''
    add good types
    '''
    pass


def get_paper_stock(request, page):
    if request.method == 'GET':
        

        return render(request, )
    else:
        return HttpResponse('wrong request')

def paper_stock(request, page):
    """  Return json with new captcha for ajax refresh request """
    # if not request.is_ajax():
    #     raise Http404
    to_json_response = {}

    

    return HttpResponse(json.dumps(to_json_response), content_type='application/json')  
