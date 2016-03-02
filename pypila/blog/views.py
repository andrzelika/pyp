from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import View

from django.http import JsonResponse
from blog.decorators import parse_json

from django.views.generic import TemplateView
from blog.forms import HelloForm
from blog.models import CzlonekRodziny
# Tutaj
from blog.forms import CzlonekRodzinyForm

def index(request):
    return render(request, 'linki.html')

class WyszukajDodajCzlonka(TemplateView):
    template_name = 'lista_czlonkow2.html'

    def get_queryset(self, request):
        qs = CzlonekRodziny.objects.filter()
        if 'imie' in request.GET and request.GET['imie']:
            qs = qs.filter(imie=request.GET['imie'])
        if 'nazwisko' in request.GET and request.GET['nazwisko']:
            qs = qs.filter(nazwisko=request.GET['nazwisko'])
        if 'wiek' in request.GET and request.GET['wiek']:
            qs = qs.filter(wiek=request.GET['wiek'])

        return qs

    def get_context_data(self, data=None, **kwargs):
        context = {
            'form': CzlonekRodzinyForm(data),
            'members': self.get_queryset(self.request)
        }

        return context

    def post(self, request):
        form = CzlonekRodzinyForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/czlonkowie_rodziny2/')
        else:
            return render(
                request, self.template_name,
                self.get_context_data(request.POST)
            )

        return HttpResponseRedirect('/czlonkowie_rodziny2/')

class SayHello(TemplateView):
    template_name = 'say_hello.html'

    def get_context_data(self, **kwargs):
        context = {
            'form': HelloForm()
        }

        return context

    def post(self, request):
        form = HelloForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect(
                '/hello_name/{}'.format(form.cleaned_data['name'])
            )
        return HttpResponseRedirect('/say_hello/')

class CzlonkowieRodziny(TemplateView):
    template_name = 'lista_czlonkow.html'

    def get_context_data(self, **kwargs):
        context = {
            'members': CzlonekRodziny.objects.all()
        }

        return context

class HelloName(TemplateView):
    template_name = 'hello_name.html'

    def get_context_data(self, name, **kwargs):
        context = {
            'name': name
        }

        return context

class HelloWorld(TemplateView):
    template_name = 'hello_world.html'

class CzlonkowieRodzinyAPIView(View):

    def filter_queryset(self, request, pk):
        qs = CzlonekRodziny.objects.filter()
        if pk:
            qs = qs.filter(pk=pk)
        else:
            if 'imie' in request.GET:
                qs = qs.filter(imie__in=request.GET.getlist('imie'))
            if 'nazwisko' in request.GET:
                qs = qs.filter(nazwisko__in=request.GET.getlist('nazwisko'))
            if 'wiek' in request.GET:
                qs = qs.filter(wiek__in=request.GET.getlist('wiek'))

        return qs

    def get(self, request, pk=None, *args, **kwargs):
        result = self.filter_queryset(request, pk)

        return JsonResponse({'result': list(result.values())})

    @parse_json
    def post(self, request, *args, **kwargs):
        result = {}
        try:
            CzlonekRodziny.objects.create(**request.data)
            status = 201
        except Exception as e:
            result = {'errors': e.message}
            status = 400
        finally:
            return JsonResponse(result, status=status)

    @parse_json
    def put(self, request, pk, *args, **kwargs):
        result = self.filter_queryset(request, pk)
        result.update(**request.data)

        return JsonResponse({'result': list(result.values())})

    def delete(self, request, pk, *args, **kwargs):
        status = 200
        result = self.filter_queryset(request, pk)
        if result:
            result.delete()
        else:
            status = 400

        return JsonResponse({}, status=status)

#class CzlonkowieRodziny(View):
#    def get(self, request):
#        context = {
#        'members': CzlonekRodziny.objects.all()
#        }
#        return render(request, 'lista_czlonkow.html', context=context)

#class CzlonkowieRodziny(View):
#
#    def get(self, request, **kwargs):
#        members = CzlonekRodziny.objects.all()
#
#        return HttpResponse(members)

#def hello_world(request):
#    return HttpResponse('Hello world!')

#def hello_name(request, name):
#    return HttpResponse('Hello {}!'.format(name))

#def hello_family(request, id):
#    person = CzlonekRodziny.objects.get(pk=id)
#    return HttpResponse('Hello {person.imie} {person.nazwisko}!'.format(person=person))
