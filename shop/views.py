from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'shop/index.html')

def store(request):
	return render(request,'shop/store.html')

def products(request):
	return render(request,'shop/products.html')

def about(request):
	return render(request,'shop/about.html')