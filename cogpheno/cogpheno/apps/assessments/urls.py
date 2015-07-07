from .views import assessments_view, questions_view, edit_assessment, edit_question, view_assessment, view_question, delete_assessment, delete_question, edit_questions, export_questions, export_questions, export_assessment
from django.views.generic.base import TemplateView
from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Assessments
    url(r'^assessments$', assessments_view, name="assessments"),
    url(r'^questions$', questions_view, name="questions"),
    url(r'^assessments/new$',edit_assessment,name='new_assessment'),
    url(r'^questions/(?P<qid>\d+|[A-Z]{8})/edit$',edit_question,name='edit_question'),
    url(r'^assessments/(?P<aid>\d+|[A-Z]{8})/$',view_assessment, name='assessment_details'),
    url(r'^questions/(?P<qid>\d+|[A-Z]{8})/$',view_question, name='question_details'),
    url(r'^assessments/(?P<aid>\d+|[A-Z]{8})/delete$',delete_assessment,name='delete_assessment'),
    url(r'^assessments/(?P<aid>\d+|[A-Z]{8})/export$',export_assessment,name='export_assessment'),
    url(r'^questions/export$',export_questions,name='export_questions'),
    url(r'^questions/(?P<qid>\d+|[A-Z]{8})/delete$',delete_question,name='delete_question'),
    url(r'^assessments/(?P<assessment_aid>\d+|[A-Z]{8})/edit$',edit_questions,name="edit_questions"),

)
