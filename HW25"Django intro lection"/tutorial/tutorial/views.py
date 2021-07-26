from django.http import HttpResponse
import random


def status(request):
	return HttpResponse("OK")


def random_color(request):
	color = "%06x" % random.randint(0, 0xFFFFFF)
	return HttpResponse("Random color is" + color)

