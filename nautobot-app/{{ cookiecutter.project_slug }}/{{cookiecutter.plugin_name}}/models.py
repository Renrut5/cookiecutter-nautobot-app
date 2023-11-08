"""Models for {{ cookiecutter.verbose_name }}."""

# Django imports
from django.db import models

# Nautobot imports
from nautobot.apps.models import PrimaryModel


# from nautobot.extras.utils import extras_features
# If you want to use the extras_features decorator please reference the following documentation
# https://docs.nautobot.com/projects/core/en/latest/plugins/development/#using-the-extras_features-decorator-for-graphql
# Then based on your reading you may decide to put the following decorator before the declaration of your class
# @extras_features("custom_fields", "custom_validators", "relationships", "graphql")

# If you want to choose a specific model to overload in your class declaration, please reference the following documentation:
# how to chose a database model: https://docs.nautobot.com/projects/core/en/stable/plugins/development/#database-models
class {{ cookiecutter.model_class_name }}(PrimaryModel):
    """Base model for {{ cookiecutter.verbose_name }} plugin."""

    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200, blank=True)
    # additional model fields

    class Meta:
        """Meta class."""

        ordering = ["name"]

        # Option for fixing capitalization (i.e. "Snmp" vs "SNMP")
        # verbose_name = "{{ cookiecutter.verbose_name }}"

        # Option for fixing plural name (i.e. "Chicken Tenders" vs "Chicken Tendies")
        # verbose_name_plural = "{{ cookiecutter.verbose_name }}s"

    def __str__(self):
        """Stringify instance."""
        return self.name
