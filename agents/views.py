from random import randint

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.db.models import QuerySet
from django.urls import reverse
from django.views import generic
from leads.models import Agent

from .forms import AgentModelForm
from .mixins import OrganisorAndLoginRequiredMixin


class AgentListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        pwd = f"{user.username}{randint(100,1000000)}"
        user.set_password(pwd)
        user.save()
        Agent.objects.create(
            user=user,
            organisation=self.request.user.userprofile,
        )
        send_mail(
            subject="You are invited to be an agent",
            message=f"You were added as an agent on DJCRM. Please come login to start working.\nYour login is: {user.username}\nYour temporary password is: {pwd}",
            from_email="admin@test.com",
            recipient_list=[user.email],
        )
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")


class AgentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")
