from django.urls import path
from Aeonapp import views
urlpatterns = [
    path('',views.home),
    path('internship1/',views.trainingandIntern1),
    path('internship2/',views.trainingandIntern1),
    path('internform/',views.trainingform),
    path('workshops/',views.workshop),
    path('workshopform/',views.workshopform),
    path('publication/',views.research_papers),
    path('publicationform/',views.publicationform),
    path('manuscript/',views.manuscript),
    path('contactus/',views.contactus),
    path('about/',views.aboutus)
]
