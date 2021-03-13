from django.urls import path
from.import views
urlpatterns=[
path('hospitail/',views.hospitail_detail,name='hospitail_detail'),

path('survey/',views.survey , name='covid_survey')

]