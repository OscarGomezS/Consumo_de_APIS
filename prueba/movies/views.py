from django.shortcuts import render, get_object_or_404

from bs4 import BeautifulSoup

import requests
import json

from .models import NamePeople, PhysicalCharac


def get_html(request):

    template = 'movies/index.html'
    url = 'https://www.python.org/about/'

    resp = requests.get(url)
    html_page = resp.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    output = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head',
    ]

    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)

    context = {
        'text': output,
    }

    return render(request, template, context)

def get_people(request):
    template = 'movies/people.html'
    url = 'https://swapi.py4e.com/api/people/'

    resp = requests.get(url)
    html_page = resp.content
    soup = BeautifulSoup(html_page, 'html.parser')
    json_data = json.loads(soup.text)
    results = json_data['results']


    data_names = NamePeople.objects.all()

    if not data_names:
        results_len = len(results)
        for i in range(results_len - 1):
            names = results[i]["name"]
            n = NamePeople(name=names)
            n.save()
            p = PhysicalCharac(
                namePeople=n, 
                height=results[i]["height"], 
                mass=results[i]["mass"],
                hair_color=results[i]["hair_color"]
                )
            p.save()

    data_names = NamePeople.objects.all()
    
    context = {
        'people': data_names,
    }

    return render(request, template, context)

def show_detail(request, name):
    template = "movies/detail.html"
    people = get_object_or_404(NamePeople, name=name)

    height = people.physicalcharac_set.values("height")
    mass = people.physicalcharac_set.values("mass")
    hair_color = people.physicalcharac_set.values("hair_color")
    
    context = {
        'name': name,
        'height': height[0]["height"],
        'mass': mass[0]["mass"],
        'hair_color': hair_color[0]["hair_color"]
    }

    return render(request, template, context)


