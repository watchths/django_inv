# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404

from django.db.models import Count 
from stock.models import Division,Category,Item,Employee,Inventory,V_Item,V_Item_Imp,V_Schedule, V_Imp_Hdd, V_Imp_Ssd
 
# def views_category(request):
#     category_list = Category.objects.all().order_by('id')
#     return render_to_response('index.html', {'category_data': category_list})

def views_item(request):
    list_item = V_Item.objects.values('name','division','item','serial_number').order_by('name')
    return render_to_response('show_item.html', {'items': list_item})

def views_item_imp(request):
    list_item = V_Item_Imp.objects.values('name','division','item','serial_number').order_by('name')
    return render_to_response('show_item_imp.html', {'items': list_item})

def views_schedule(request):
    list_item = V_Schedule.objects.values('name','item','project','destination','taken_date','receipt_date').order_by('project')
    return render_to_response('show_schedule.html', {'items': list_item})

def filter_person_by_storage (target, filters):
    return list( filter(lambda x: x not in filters, target) )

def filter_arr_by_name (arr, names):
    return list( filter(lambda x: x['name'] in names, arr) )

def get_person_by_storage_type (type):
    hdd = V_Imp_Hdd.objects.values('name', 'division', 'item', 'serial_number').order_by('name')
    ssd = V_Imp_Ssd.objects.values('name', 'division', 'item', 'serial_number').order_by('name')

    person_hdd = [ x['name'] for x in hdd ]
    person_ssd = [ x['name'] for x in ssd ]
    
    if type == 'ssd':
        person_ssd_after_filter = filter_person_by_storage(person_ssd, person_hdd)
        return filter_arr_by_name(ssd, person_ssd_after_filter)
    elif type == 'hdd':
        person_hdd_after_filter = filter_person_by_storage(person_hdd, person_ssd)
        return filter_arr_by_name(hdd, person_hdd_after_filter)

def render_ssd_person (request):
    return render_to_response('show_imp_only_ssd.html', {'people': get_person_by_storage_type('ssd')})

def render_hdd_person (request):
    return render_to_response('show_imp_only_hdd.html', {'people': get_person_by_storage_type('hdd')})

def render_contoh (request):
    # process hasil request
    return render_to_response('contoh.html', {'request': request.GET.get('personName')})