from django.shortcuts import render

from .models import Member


def member_list(request):
	template_data = dict(
		members=Member.objects.all(),
	)
	return render(request, "member_list.html", template_data)
