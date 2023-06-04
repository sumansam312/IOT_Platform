from django.shortcuts import render, redirect
from django.contrib.auth.views import login_required
from django.views.generic.list import ListView
from django.http import JsonResponse
from .models import CircuitModel, CircuitStatusModel, ApiModel
from .forms import CircuitForm
from django.contrib.auth.forms import UserCreationForm


class CircuitControlView(ListView):
    model = CircuitModel
    ordering = "-id"
    paginate_by = 20


class CircuitStatusView(ListView):
    model = CircuitStatusModel
    ordering = "-id"
    paginate_by = 20


def write_api_view(request):
    write_api = ApiModel.objects.last().write_api
    api_key = request.GET.get("api", "")
    if write_api == api_key:
        led1 = request.GET.get("led1", "")
        led2 = request.GET.get("led2", "")
        obj = CircuitStatusModel.objects.create(led_1=led1, led_2=led2)
        obj.save()
        context = {"data": "Success"}
    else:
        context = {"data": "You are not authorized"}
    return JsonResponse(context)


@login_required
def to_circuit(request):
    if request.method == "POST" and request.user.has_perm("ckt.add_circuitmodel"):
        form = CircuitForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("ckt")
    else:
        form = CircuitForm()
    context = {"form": form}
    return render(request, "ckt/control.html", context)


def read_api_view(request):
    read_api = ApiModel.objects.last().read_api
    api_key = request.GET.get("api", "")
    if read_api == api_key:
        content = CircuitModel.objects.last()
        context = {
            "led1": content.led_1,
            "led2": content.led_2,
            "user": content.user.username,
        }
    else:
        context = {"data": "You are not authorized"}
    return JsonResponse(context)


def plot_graph(request):
    # tz = pytz.timezone("Asia/Kolkata")
    led_1 = []
    led_2 = []
    date = []
    datas = CircuitStatusModel.objects.values("led_1", "led_2", "id").order_by("-id")[
        :40
    ]
    for mc in datas:
        led_1.append(mc["led_1"])
        led_2.append(mc["led_2"])
        date.append(mc["id"])
    led_1.reverse()
    led_2.reverse()
    date.reverse()
    data = {"led1": led_1, "led2": led_2, "date": date}
    return JsonResponse(data)


def chartview(request):
    return render(request, "chartview.html")


def graph_two(request):
    return render(request, "chartview_two.html")


def usercreation(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    content = {"form": form}
    return render(request, "login.html", content)


def aboutpage(request):
    return render(request, "About_us.html")


def privacy(request):
    return render(request, "Privacy_policy.html")
