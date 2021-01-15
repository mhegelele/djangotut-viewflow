from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class PollsConfig(ModuleMixin, AppConfig):
    name = 'djangotut.polls'
    icon = '<i class="material-icons">settings_applications</i>'
