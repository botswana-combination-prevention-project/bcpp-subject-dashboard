from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import (
    DashboardViewMixin as EdcDashboardViewMixin, AppConfigViewMixin)

from ...wrappers import AnonymousConsentModelWrapper
from .base_dashboard_view import BaseDashboardView
from .wrappers import (
    AppointmentModelWrapper,
    SubjectVisitModelWrapper, CrfModelWrapper, RequisitionModelWrapper)


class DashboardView(
        BaseDashboardView, EdcDashboardViewMixin,
        AppConfigViewMixin, EdcBaseViewMixin,
        TemplateView):

    app_config_name = 'bcpp_subject_dashboard'
    navbar_item_selected = 'bcpp_subject_dashboard'
    navbar_name = 'anonymous'
    consent_model_wrapper_cls = AnonymousConsentModelWrapper
    consent_model = 'bcpp_subject.anonymousconsent'
    crf_model_wrapper_cls = CrfModelWrapper
    requisition_model_wrapper_cls = RequisitionModelWrapper
    visit_model_wrapper_cls = SubjectVisitModelWrapper
    appointment_model_wrapper_cls = AppointmentModelWrapper

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.anonymous = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'anonymous': 'anonymous',
            'anonymous_dashboard_url_name': django_apps.get_app_config(
                'bcpp_subject_dashboard').anonymous_dashboard_url_name})
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
