"""
URLs for twou_titan_plugin.
"""
from django.urls import re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    re_path(r'titan-plugin', TemplateView.as_view(template_name="twou_titan_plugin/base.html")),
]
