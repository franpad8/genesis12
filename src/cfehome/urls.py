"""cfehome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="home"),
    url(r'^charities$', TemplateView.as_view(template_name="charities.html"), name="charities"),
    url(r'^about$', TemplateView.as_view(template_name="about.html"), name="about"),
    url(r'^fundraising$', TemplateView.as_view(template_name="fundraising.html"), name="fundraising"),
    url(r'^e-fundraising$', TemplateView.as_view(template_name="e-fundraising.html"), name="e-fundraising"),
    url(r'^faq$', TemplateView.as_view(template_name="faq.html"), name="faq"),

]
