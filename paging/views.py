from django.shortcuts import render
from secondapp.models import ArmyShop
from django.core.paginator import Paginator
def army_shop(request):
    now_page = request.GET.get('page', 1)
    #   LIMIT 시작번호, 개수

    datas = ArmyShop.objects.order_by('-id')
    p = Paginator(datas, 10)
    
    # 요청파라미터는 문자열, 문자열 -> 숫자
    now_page = int(now_page)

    info = p.page(now_page)

    start_page = (now_page - 1) // 10 * 10 + 1
    end_page = start_page + 9
    if end_page > p.num_pages:
        end_page = p.num_pages
    context = {
        'info' : info,
        'page_range' : range(start_page, end_page + 1)
    }
    return render(request, 'paging/army_shop.html', context)