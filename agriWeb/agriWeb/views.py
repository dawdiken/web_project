from django.views.generic import View
from django.conf import settings
from django.shortcuts import redirect
import pymysql
import json
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect



def addCustomer(request, *args, **kwargs):
    return render(request, 'addCust.html')


def success(request, *args, **kwargs):
    return render(request, 'success.html')


class saveCust(View):
    print("did you fucking work2222")
    def get(self, request, *args, **kwargs):
        # if not request.user.is_authenticated:
        #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        # if not request.user.email.endswith('@gmail.com'):
        #     return redirect('/permissionredirect')

        cnx = pymysql.connect(host="35.185.61.102",  # your host, usually localhost
                              user="remote",  # your username
                              passwd="safe_passworD123!",  # your password
                              db="agri_data")  # name of the data base
        cursor = cnx.cursor()
        #query = ("SELECT * FROM customer")
        sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
        val = ("John", "Highway 21")


        cursor.execute(sql, val)


        # results = cursor.fetchall()
        # print(results)


        print(request)
        print("did you fucking work")
        return redirect('success')



