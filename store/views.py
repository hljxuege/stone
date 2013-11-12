#encoding:utf-8
import json
from store.models import PaperStock, InkStock
from django.http import HttpResponse
def home(request):
    return HttpResponse('store home')

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
