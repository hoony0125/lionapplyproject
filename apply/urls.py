from django.urls import path
from apply.views import *

urlpatterns = [
    path('new',new, name="urlnamenew"),                #urls.py에서 가운데는 함수명
    path('readall',readall, name='urlnamereadall'),
    path('detail<str:each_id>',detail, name='urlnamedetail'),   #views.py에 가서 get object or 404 작성
    path('update<str:each_id>',update, name = 'urlnameupdate'),
    path('delete<str:each_id>',delete, name ='urlnamedelete'),
    
]   
