from django.http.response import HttpResponse
from django.shortcuts import render


class HasPerm:
    
    def has_perm(self, request, *args, **kwargs):
        qs = super().get_queryset().filter(pk=kwargs['pk'])

        if qs.count() == 1 and qs.first().user == request.user :
            return super().get(request,*args, **kwargs)
        else:
            return render(request, '404.html')