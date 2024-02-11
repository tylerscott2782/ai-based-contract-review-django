from django.shortcuts import render
from django.http import HttpResponse

from.models import Contract

# Create your views here.
def index(request):
    contract_list = Contract.objects.order_by("-upload_date")
    context = {"contract_list": contract_list}
    return render(request, "ai_contract_review/index.html", context)