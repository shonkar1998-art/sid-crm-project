from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm

def home(request):
    q = request.GET.get('q', '')
    if q:
        customers = Customer.objects.filter(name__icontains=q) | Customer.objects.filter(email__icontains=q)
    else:
        customers = Customer.objects.all().order_by('-created_at')
    return render(request, 'crmapp/home.html', {'customers': customers, 'q': q})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm()
    return render(request, 'crmapp/add_customer.html', {'form': form})

def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'crmapp/edit_customer.html', {'form': form, 'customer': customer})

def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('home')
    return render(request, 'crmapp/delete_customer.html', {'customer': customer})
