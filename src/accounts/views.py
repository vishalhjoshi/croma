from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import (
		authenticate,
		get_user_model,
		login,
		logout,
	)
from .forms import UserLoginForm, UserRegisterForm, CompanyRegistrationForm
from .models import Registration, YearEnding
import datetime


def login_view(request):
	User = get_user_model()
	user_qs = User.objects.all()
	register_qs = Registration.objects.all()

	if user_qs.count() == 0:
		messages.warning(request, 'You have to first register yourself')
		return HttpResponseRedirect("/account/register")
	
	if register_qs.count() == 0:
		return HttpResponseRedirect("/account/company/register")
	
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		session = form.cleaned_data.get("session")
		request.session['session'] = session.id
		user = authenticate(username = username, password = password)
		login(request, user)
		if register_qs.count() == 0:
			return HttpResponseRedirect("/account/company/register")
		return redirect("/")
	return render(request, "accounts/account_form.html", {
		"form" : form,
		"title" : "User Login",
		"btn_txt": "Login"
	})


def register_view(request):
	User = get_user_model()
	user_qs = User.objects.all()
	if user_qs.count() > 0:
		messages.warning(request, 'User has already registred')
		return HttpResponseRedirect("/account/login")

	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save()
		password = form.cleaned_data.get("password")	
		user.set_password(password)
		user.save()
		new_user = authenticate(username = user.username, password = password)
		login(request, new_user)
		return redirect("/account/company/register")
	return render(request, "accounts/account_form.html", {
		"title" : "User Register",
		"form" : form,
		"btn_txt": "Register"
	})


def logout_view(request):
	logout(request)
	try:
	  del request.session['session']
	except:
		pass
	return HttpResponseRedirect("/")


def companyRegistrationView(request):
	reg_qs = Registration.objects.all()
	if reg_qs.count() > 0:
		messages.warning(request, 'Only one Company can register.')
		return HttpResponseRedirect("/account/login")

	User = get_user_model()
	user_qs = User.objects.all()
	if user_qs.count() == 0:
		messages.warning(request, 'Register the user first')
		return HttpResponseRedirect("/account/register")

	messages.warning(request, 'Register Your Company Now.')
	form = CompanyRegistrationForm(request.POST or None)
	if form.is_valid():
		company_instance = form.save()
		today_date = datetime.date.today()
		end_date = today_date + datetime.timedelta(days=365)
		YearEnding.objects.create(code = "DB1",
							year_pur_id=0, year_sale_id=0,
                            from_dt=today_date, to_dt=end_date, 
							registration_id=company_instance)
		
		messages.warning(request, 'Login')
		return redirect("/account/login")
	return render(request, "accounts/account_form.html", {
		"form" : form,
		"title" : "Company Registration",
		"btn_txt": "Register"
	})
