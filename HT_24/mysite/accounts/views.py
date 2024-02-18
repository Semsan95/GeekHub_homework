from django.http import HttpResponseRedirect
from django.urls import reverse


def profile(request):
    return HttpResponseRedirect(reverse('admin:index' if request.user.is_superuser else 'products:search'))