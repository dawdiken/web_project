from django.views.generic import View
from django.conf import settings
from django.shortcuts import redirect
import pymysql
import json
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect



def about(request, *args, **kwargs):
    return render(request, 'about.html')


def success(request, *args, **kwargs):
    return render(request, 'success.html')


class saveCust(View):
    print("did you fucking work2222")
    def get(self, request, *args, **kwargs):
        # if not request.user.is_authenticated:
        #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        # if not request.user.email.endswith('@gmail.com'):
        #     return redirect('/permissionredirect')
        print("did you fucking work")
        return redirect('success')



