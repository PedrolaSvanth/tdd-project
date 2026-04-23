from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'items': items})

def new_list(request):
    my_list = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=my_list)
    return redirect('/lists/the-only-list-in-the-world/')