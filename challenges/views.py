from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.shortcuts import render, redirect

month_map = {'january': 'Go to Ahmed Birthday Party', 'febuary': 'find girl for marriage',
             'march': 'Do shopping for marriage', 'april': 'Marriage a young girl',
             'may': 'Go on honeymoon', 'june': 'Visit some northern areas',
             'july': 'plan for a child', 'august': 'take care of wife',
             'september': 'have a good diet', 'october': 'take wife to her parents',
             'november': 'do pre shopping for new born child', 'december': 'wait for child birth'
             }


def index(request):
    months_list = list(month_map.keys())
    return render(request, 'challenges/index.html', {'months_list': months_list})


def monthly_challenge_by_num(request, month):
    months_list = list(month_map.keys())
    try:
        forward_month = months_list[month-1]
        return redirect('month-str', forward_month)
    except:
        return HttpResponseNotFound('<h1 style="color: red">Month Not Found</h1>')


def monthly_challenge(request, month):
    try:
        desc = month_map[month]
        return render(request, 'challenges/activity.html', {'activity': desc, 'month': month})
    except:
        raise Http404()
