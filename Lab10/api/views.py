from django.shortcuts import render
from .models import Company,Vacancy
from django.http import HttpResponse,JsonResponse

def scroll_company(request):
    companies = Company.objects.all()
    company_json = [company.to_json() for company in companies]
    return JsonResponse(company_json, safe = False)

def company_info(request,company_id):
    company = Company.objects.get(id = company_id)
    return JsonResponse(company.to_json())

def company_vacancy(request,company_id):
    company = Company.objects.get(id = company_id)
    vacancies = Vacancy.objects.all()
    match = []
    for i in vacancies:
        if i.company == company:
            match.append(i)
    vacancies_json = [vacancy.to_json() for vacancy in match]
    return JsonResponse(vacancies_json,safe=False)

def scroll_vacancy(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe = False)

def vacancy_info(request,vacancy_id):
    vacancy = Vacancy.objects.get(id = vacancy_id)
    return JsonResponse(vacancy.to_json())

def top_ten(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json,safe=False)
# Create your views here.
