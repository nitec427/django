from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

the_dict = {
    "January": "Elenaor Rigby",
    "February": "Penny Lane",
    "March": "All you need is love",
    "April": None,
    "May": "Hey Jude",
    "June": "Yesterday",
    "July": "Help!",
    "August": "Mozart",
    "September": "Vivaldi",
    "October": None,
    "November": "She loves you",
    "December": "From me to you",
}


def navigation_page(request, name):
    keys = list(the_dict.keys())
    return render(request, "challenges/index.html", {"months": keys, "name": name})


def months_by_number(req, number, name):
    find_month = list(the_dict.keys())
    redirect_month = find_month[number-1]
    redirect_to = reverse("month-str", args=[redirect_month, name])
    return HttpResponseRedirect(redirect_to)


def remaining_months(req, month, name):
    try:
        return render(req, "challenges/challenge.html", {"cur_month": month, "task": the_dict[month]})

    except:
        return HttpResponseNotFound("This value is not contained in the dictionary.")
