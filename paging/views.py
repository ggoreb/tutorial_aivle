from django.shortcuts import render
from secondapp.models import ArmyShop
from django.core.paginator import Paginator
def army_shop(request):
    now_page = request.GET.get('page', 1)
    #   LIMIT 시작번호, 개수

    datas = ArmyShop.objects.order_by('-id')
    p = Paginator(datas, 10)
    
    info = p.page(now_page)

    context = {
        'info' : info
    }
    return render(request, 'paging/army_shop.html', context)