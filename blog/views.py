from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Address
from .forms import AddressForm
from django.contrib.auth.decorators import login_required


def addr_list(request):
    addrs = Address.objects.filter(open_addr=0)
    no_addrs = Address.objects.filter(open_addr=1)
    return render(request, 'blog/addr_list.html', {'addrs':addrs, 'no_addrs':no_addrs})


def addr_detail(request, pk):
    addr = get_object_or_404(Address, pk=pk)
    return render(request, 'blog/addr_detail.html', {'addr': addr})


@login_required
def addr_new(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            addr = form.save(commit=False)
            addr.author = request.user
            addr.created_date = timezone.now()
            addr.save()
            return redirect('blog:addr_detail', pk=addr.pk)
    else:
        form = AddressForm()
    return render(request, 'blog/addr_edit.html', {'form':form})


@login_required
def addr_edit(request, pk):
    addr = get_object_or_404(Address, pk=pk)
    if request.method == "POST":
        form = AddressForm(request.POST, instance=addr)
        if form.is_valid():
            addr = form.save(commit=False)
            addr.author = request.user
            addr.created_date = timezone.now()
            addr.save()
            return redirect('blog:addr_detail', pk=addr.pk)
    else:
        form = AddressForm(instance=addr)
    return render(request, 'blog/addr_edit.html', {'form':form})


@login_required
def addr_remove(request, pk):
    addr = get_object_or_404(Address, pk=pk)
    addr.delete()
    return redirect('blog:addr_list')


@login_required
def addr_openaddr(request, pk):
    addr = get_object_or_404(Address, pk=pk)
    addr.openaddr()
    return redirect('blog:addr_list')


@login_required
def addr_noopenaddr(request, pk):
    addr = get_object_or_404(Address, pk=pk)
    addr.noopenaddr()
    return redirect('blog:addr_list')