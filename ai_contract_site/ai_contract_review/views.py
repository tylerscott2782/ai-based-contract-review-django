from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from.models import Contract
from.forms import ContractFileForm

# Create your views here.
def index(request):
    contract_list = Contract.objects.order_by("-upload_date")

    if request.method == "POST":
        form = ContractFileForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("")
    else:
        form = ContractFileForm()

    context = {"form": form, "contract_list": contract_list}
    return render(request, "ai_contract_review/index.html", context)