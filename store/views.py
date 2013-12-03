#encoding:utf-8
from django.shortcuts import redirect, render
import json
from django.contrib.auth.decorators import login_required
from store.models import Good, GoodType, GoodTypeGoods
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

    raise Http404
    
@login_required
def good_type_list(request):
    if request.method == 'GET':
        good_types = GoodType.objects.all()
        for good_type in good_types:
            good_type.main_num = Good.objects.filter(belong_type=good_type.name).count()
            good_type.subsidiary_num = good_type.goods.count()
  
        return render(request, 'manage/store/good_type_list.html', {'good_types':good_types})

    raise Http404

def good_of_goodtypes(request, goodtype_id):
    if request.method == 'GET':
        goodtype = GoodType.objects.get(id=goodtype_id)
        m_goods = Good.objects.filter(belong_type=goodtype.name)#主要分类中的商品

        s_goods = goodtype.goods.all()#次要分类中的商品
        
        return render(request, 'manage/store/goods_list_ms.html', {'m_goods':m_goods, 's_goods':s_goods})

    raise Http404

def ajax_add_good_to_type(request, good_id, good_type_id):
    if not request.is_ajax():             
         raise Http404


@login_required
def good_detail(request, good_type, good_id):
    if request.method == 'GET':
        pass

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
        raise Http404

def add_good_type(request):
    '''
    add good types
    '''
    if request.method == 'POST':
        name = request.POST['name']
        num = request.POST['num']
     
        # add session info and so on 

        return redirect('home')

    else:
        raise Http404


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
