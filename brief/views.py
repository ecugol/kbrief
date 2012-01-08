from django.contrib.formtools.wizard import FormWizard
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from brief.forms import BriefForm1

def index(request):
    form = BriefForm1(request.POST or None)
    if request.POST and form.is_valid():
        pass

    return TemplateResponse(request, "index.html", {'form': form})


class BriefWizard(FormWizard):
    def done(self, request, form_list):
        return render_to_response('done.html', {
            'form_data': [form.cleaned_data for form in form_list],
            })
