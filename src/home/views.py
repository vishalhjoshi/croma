from django.shortcuts import render, redirect, Http404, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import Registration, YearEnding

@login_required(login_url='/account/login/')
def HomePage(request):
	if not request.user.is_authenticated():
		raise Http404
	try:
		current_session_id = request.session['session']
	except:
		currentSession = YearEnding.objects.order_by("-id").first()
		request.session['session'] = currentSession.id
		current_session_id = currentSession.id

	current_session = get_object_or_404(YearEnding, id = current_session_id)
	return render(request, 'home/index.html', {"current_session":current_session})

