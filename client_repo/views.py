# Create your views here.
from django.views.generic.detail import DetailView
from client_repo.models import Host

class HostDetailView(DetailView):
    model = Host
    template_name = "client_repo/admin/host_detail.html"

    context_object_name = "host"