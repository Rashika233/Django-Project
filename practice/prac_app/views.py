from django.shortcuts import render 
from .forms import GeeksForm 

def home_view(request): 
	context ={} 

	# create object of form 
	form = GeeksForm(request.POST or None, request.FILES or None) 
	
	# check if form data is valid 
	if form.is_valid(): 
		# save the form data to model 
		form.save() 
		form = GeeksForm()
	context['form']= form 
	return render(request, "home.html", context) 

