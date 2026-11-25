from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json

# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class BMIView(View):
    def post(self, request):
        data = json.loads(request.body)
        height = data.get("height")
        weight = data.get("weight")
        height_m = height / 100
        bmi = round(weight / (height_m ** 2), 2)
        return JsonResponse({
            "height": height,
            "weight": weight,
            "bmi": bmi
        })

@method_decorator(csrf_exempt, name="dispatch")
class AgeView(View):
    def post(self, request):
        data = json.loads(request.body)
        birth_year = data.get("birth_year")
        current_year = datetime.now().year
        return JsonResponse({
            "age": current_year - birth_year
        })

@method_decorator(csrf_exempt, name="dispatch")
class PercentageView(View):
    def post(self, request):
        data = json.loads(request.body)
        marks_obtained = data.get("marks_obtained")
        total_marks = data.get("total_marks")
        return JsonResponse({
            "percentage": (marks_obtained/total_marks) * 100
        })

# simple interest = (principal amount * rate * time) / 100
@method_decorator(csrf_exempt, name="dispatch")
class SimpleInterestView(View):
    def post(self, request):
        data = json.get(request.body)
        principal = data.get("principal")
        rate = data.get("rate")
        time = data.get("time")
        return JsonResponse({
            "principal": principal,
            "rate": rate,
            "time": time,
            "time": time,
        })

# electricity bill = units * rate
@method_decorator(csrf_exempt, name="dispatch")
class View(View):
    def post(self, request):
        data = json.get(request.body)
        return JsonResponse({
            "":
        })
