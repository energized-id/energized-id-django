from django.contrib.auth import login
from .imports import *
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

AdminItems = [
    {"model":"BadgeTemplate", "title":"Badge Templates", "description":"Add or modify badge templates", "icon":"fas fa-id-badge", "url":"LibreBadge:BadgeTemplateList"},
    {"model":"AlertMessage", "title":"Alert Messages", "description":"Add or modify alert messages", "icon":"fas fa-exclamation-triangle", "url":"LibreBadge:AlertMessageList"}
]

@login_required
def applicationadmin(request):
    return render(request, 'LibreBadge/applicationadmin/home.html',
    context = {"AdminItems":AdminItems,})

def applicationAdminCRUDFunction(model, modelName, fields):
    def templateNameGenerator(suffix):
        return("LibreBadge/applicationadmin/" + modelName + "/" + modelName + suffix + ".html")
    viewsDictionary = {}
    viewsDictionary['CreateView'] = type(modelName + 'CreateView', (CreateView,), {'template_name': templateNameGenerator('Form'),'model': model, 'fields': fields})
    viewsDictionary['ListView'] = type(modelName + 'ListView', (ListView,), {'template_name': templateNameGenerator('List'),'model': model})
    viewsDictionary['UpdateView'] = type(modelName + 'UpdateView', (UpdateView,), {'template_name': templateNameGenerator('Form'),'model': model, 'fields': fields})
    viewsDictionary['DeleteView'] = type(modelName + 'DeleteView', (DeleteView,), {'template_name': templateNameGenerator('Delete'),'success_url': reverse_lazy('LibreBadge:' + modelName + 'List'),'model': model, 'fields':fields })
    return(viewsDictionary)

AlertMessageViews = applicationAdminCRUDFunction(AlertMessage, 'AlertMessage', '__all__')
BadgeTemplateViews = applicationAdminCRUDFunction(BadgeTemplate, 'BadgeTemplate', '__all__')