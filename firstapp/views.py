from django.shortcuts import render
from django.http import Http404

from firstapp.models import Item

def index(request): 
    # show title of all items in stock - this a query set 
    items=Item.objects.all()
    return render(request, 'inventory/index.html', {
        'items': items,
        })

def item_detail(request, id): 
    #takes id that we will use to query an item using .get method
    #if id not found, then use try except block
    try: 
        item=Item.objects.get(id=id)
    except Item.DoesNotExist: 
            raise Http404('This item does not exist')
    return render(request, 'inventory/item_detail.html', {
'item': item,
})

def projectone(request): 

    tabledata = [ 
      { "first_name" : 'These ',
        "last_name"  : 'People',
        "home"  : 'are' },
      { "first_name" : 'not',
        "last_name"  : 'from',
         "home"      : 'the'},
      { "first_name" : 'data',
        "last_name"  : 'base',
        "home"     : 'they'},
      { "first_name" : 'come',
        "last_name"  : "from",
        "home"      : 'views.py'},
      { "first_name" : 'Romana',
        "last_name"  : "null",
        "home"      : 'Gallifrey'},
      { "first_name": 'Clara',
        "last_name"  : 'Oswald',
        "home"      : 'Earth'},
      { "first_name" : 'Adric',
        "last_name"  : "null",
        "home"      : 'Alzarius'},
      { "first_name" : 'Susan',
        "last_name"  : 'Foreman',
        "home"      : "Gallifrey"} ]

    return render(request, 'inventory/projectone.html', {
        'items': tabledata,
        })
