from django.db import models
from django.utils.translation import ugettext_lazy as _


class Member(models.Model):
	first_name = models.CharField(max_length=1024, verbose_name=_("first name"))
	last_name = models.CharField(max_length=1024, verbose_name=_("last name"))
	member_since = models.DateField(verbose_name=_("member since"), auto_now_add=True)
