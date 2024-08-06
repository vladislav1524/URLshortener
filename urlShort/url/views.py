from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from .forms import UrlForm, UserRegistrationForm
from .models import UrlData
import random
import string
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login


def index(request):
    return HttpResponse("Hello World")


@login_required
def urlShort(request):
    url = shorten_url = None
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            while True:
                slug = ''.join(random.choice(string.ascii_letters) for x in range(10))
                if not UrlData.objects.filter(slug=slug).exists():
                    break
            new_url = UrlData(url=url, slug=slug)
            shorten_url = request.build_absolute_uri(f'/u/{slug}/')
            new_url.save()
    else:
        form = UrlForm()
    return render(request, 'url/index.html', {'form': form,
                                              'url': url,
                                              'shorten_url': shorten_url})


def urlRedirect(request, slug):
    data = UrlData.objects.get(slug=slug)
    return redirect(data.url)


class RegistrationView(CreateView):
    template_name = 'registration/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('url:urlShort')

    def form_valid(self, form):
        super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password1'])
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().form_invalid(form)