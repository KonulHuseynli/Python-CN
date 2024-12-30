from django.contrib import messages #istifadəçiyə müvəqqəti mesajlar göstərmək üçün istifadə olunur.
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect,
)

from django.http import HttpResponse

from watches.models import Watches

from watches.forms import WatchForm



def all_watches(request):
    watches = Watches.objects.all() #SELECT*FROM wacthes_watch(bu hissede melumati aliriq)
    # return HttpResponse(watches)

    context={
        'watches':watches
    }
    return render(request,'watches/all_watches.html',context)

@login_required
def create_watch(request):
    if request.method == 'POST':
        form = WatchForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            form.save()
            new_form.save()
            return redirect('all_watches')
        else:
            #user-ə xətaları messages ile gosteririk
             messages.error(request,'You entered incorrect information.')
             messages.error(request,form.errors)
             messages.error(request,"MM/DD/YYYY HH:MM")
             return redirect('create_watch')
    else: #Get methodu olsa bu blok ise dusur
        form = {
            "watch_form" : WatchForm()
        }
        return render(request, 'watches/create_watch.html', form)


@login_required
def detail_watch(request, pk):
    watch = get_object_or_404(Watches, id = pk)
    context = {
        'watch':watch
    }
    return render(request, 'watches/detail_watch.html', context)
  
  
@login_required  
def update_watch(request, pk):
    wacthes = Watches.objects.filter(author = request.user)
    watch = get_object_or_404(wacthes, id = pk)
    
    if request.method == 'POST':
        form = WatchForm(request.POST, request.FILES, instance = watch)#instance yeni bir obyekt yaratmir sadece movcud olan obyekti yenilmek ucundur
        if form.is_valid():   
            form.save()
            return redirect('detail_watch', watch.id)
    else:
        form = WatchForm(instance = watch) #burdaki instancede melumati dolu sekilde getirir
        #instance--melumatlari bir basa ozu elave edir ve ici dolu gonderir.
        context = {
            'form':form
        }
        return render(request, 'watches/update_watch.html', context)


@login_required  
def delete_watch(request, pk):
    wacthes = Watches.objects.filter(author = request.user)
    watch = get_object_or_404(wacthes, id = pk)    
    watch.delete()
    messages.success(request, "Delete operation completed successfully.")
    return redirect('all_watches')