from django.conf.urls import url

from edc_constants.constants import UUID_PATTERN

from bcpp_subject_dashboard.views import AnonymousDashboardView, AnonymousListboardView
from bcpp_subject_dashboard.views import ListboardView, DashboardView
from household.patterns import household_identifier
from survey.patterns import survey_schedule, survey


# app_name = 'bcpp_subject'
subject_identifier = '066\-[0-9\-]+'


def listboard_urls():
    urlpatterns = []
    listboard_configs = [
        ('listboard_url', ListboardView, 'listboard'),
        ('anonymous_listboard_url', AnonymousListboardView, 'anonymous_listboard')]

    for listboard_url_name, listboard_view_class, label in listboard_configs:
        urlpatterns.extend([
            url(r'^' + label + '/'
                '(?P<subject_identifier>' + subject_identifier + ')/'
                '(?P<survey_schedule>' + survey_schedule + ')/'
                '(?P<survey>' + survey + ')/'
                '(?P<page>\d+)/',
                listboard_view_class.as_view(), name=listboard_url_name),
            url(r'^' + label + '/'
                '(?P<subject_identifier>' + subject_identifier + ')/'
                '(?P<survey>' + survey + ')/'
                '(?P<page>\d+)/',
                listboard_view_class.as_view(), name=listboard_url_name),
            url(r'^' + label + '/'
                '(?P<subject_identifier>' + subject_identifier + ')/'
                '(?P<survey_schedule>' + survey_schedule + ')/',
                listboard_view_class.as_view(), name=listboard_url_name),
            url(r'^' + label + '/'
                '(?P<subject_identifier>' + subject_identifier + ')/'
                '(?P<survey>' + survey + ')/',
                listboard_view_class.as_view(), name=listboard_url_name),
            url(r'^' + label + '/'
                '(?P<subject_identifier>' + subject_identifier + ')/',
                listboard_view_class.as_view(), name=listboard_url_name),
            url(r'^' + label + '/(?P<page>\d+)/',
                listboard_view_class.as_view(), name=listboard_url_name),
            url(r'^' + label + '/',
                listboard_view_class.as_view(), name=listboard_url_name)])
    return urlpatterns


def dashboard_urls():
    urlpatterns = []

    dashboard_configs = [
        ('dashboard_url', DashboardView, 'dashboard'),
        ('anonymous_dashboard_url', AnonymousDashboardView, 'anonymous_dashboard')]

    for dashboard_url_name, dashboard_view_class, label in dashboard_configs:
        urlpatterns.extend([
            url(r'^' + label + '/'
                '(?P<household_identifier>' + household_identifier + ')/'
                '(?P<subject_identifier>' + subject_identifier + ')/'
                '(?P<appointment>' + UUID_PATTERN.pattern + ')/'
                '(?P<survey_schedule>' + survey_schedule + ')/'
                '(?P<survey>' + survey + ')/',
                dashboard_view_class.as_view(), name=dashboard_url_name),
            url(r'^' + label + '/'
                '(?P<household_identifier>' + household_identifier + ')/'
                '(?P<subject_identifier>' + subject_identifier + ')/'
                '(?P<survey_schedule>' + survey_schedule + ')/'
                '(?P<survey>' + survey + ')/',
                dashboard_view_class.as_view(), name=dashboard_url_name),
            url(r'^' + label + '/'
                '(?P<household_identifier>' + household_identifier + ')/'
                '(?P<subject_identifier>' + UUID_PATTERN.pattern + ')/'
                '(?P<survey_schedule>' + survey_schedule + ')/'
                '(?P<survey>' + survey + ')/',
                dashboard_view_class.as_view(), name=dashboard_url_name),
            url(r'^' + label + '/'
                '(?P<household_identifier>' + household_identifier + ')/'
                '(?P<subject_identifier>' + subject_identifier + ')/'
                '(?P<survey_schedule>' + survey_schedule + ')/',
                dashboard_view_class.as_view(), name=dashboard_url_name),
            url(r'^' + label + '/'
                '(?P<household_identifier>' + household_identifier + ')/'
                '(?P<subject_identifier>' + UUID_PATTERN.pattern + ')/'
                '(?P<survey_schedule>' + survey_schedule + ')/',
                dashboard_view_class.as_view(), name=dashboard_url_name),
        ])
    return urlpatterns


urlpatterns = listboard_urls() + dashboard_urls()
