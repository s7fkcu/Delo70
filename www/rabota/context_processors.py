# -*- coding: utf-8 -*-

from rabota.forms import SearchMinForm
from geo.models import CustomLocation

##################################################################################################	
##################################################################################################

def custom_proc(request):	
	return {
		'search': SearchMinForm(),
		'city': CustomLocation.objects.get(slug=u'tomsk')
	}
	
##################################################################################################	
##################################################################################################