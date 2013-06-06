from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from models import InputForm
from compute import compute

def index(request):
    s = None  # initial value of result
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            r = form.r
            s = compute(r)
    else:
        form = InputForm()

    return render_to_response('hw2.html',
            {'form': form,
             's': '%.5f' % s if isinstance(s, float) else ''
             }, context_instance=RequestContext(request))

