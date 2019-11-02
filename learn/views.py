from django.shortcuts import render

# Create your views here.

import cx_Oracle
from learn import NClass


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw);


def test(request):
    ndame='fdsasdf'
    mt = NClass.Metal()
    NClass.Metal.mcout=111

    tt=(1,2,3,4)
    kt={'dfd':'dfadfa','1123':'23232'};
    f1(*tt,**kt)
    #mt.mcout

    return render(request, 'test.html',{'name': mt.mcout.__str__()})





