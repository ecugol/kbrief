# -*- coding:utf-8 -*-
from django import forms
from brief.models import Brief

class BriefForm1(forms.Form):
    contact_name = forms.CharField(max_length=50)
    contact_phone = forms.CharField(max_length=20)
    contact_email = forms.EmailField()
    contact_city = forms.CharField(max_length=100, initial=u"Сургут")
    contact_address = forms.CharField(widget=forms.Textarea)


class BriefForm2(forms.Form):
    project_name = forms.CharField(max_length=150)
    sphere = forms.CharField(widget=forms.Textarea)

    contact_site = forms.URLField(required=False)
    contact_domain_name = forms.URLField(label=u"Планируемый адрес сайта", required=False)

    deadline_date = forms.DateField(required=False)

    deadline_info = forms.CharField(widget=forms.Textarea, required=False)

    marketing_events = forms.CharField(widget=forms.Textarea, required=False)
