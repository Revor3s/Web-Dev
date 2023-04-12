from django.urls import path
from .views import *

urlpatterns = [
    path('companies/',scroll_company),
    path('companies/<int:company_id>/',company_info),
    path('companies/<int:company_id>/vacancies/',company_vacancy),
    path('vacancies/',scroll_vacancy),
    path('vacancies/<int:vacancy_id>/',vacancy_info),
    path('vacancies/top_ten/',top_ten)
]