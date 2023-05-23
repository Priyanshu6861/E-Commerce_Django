import imp
from xml.dom.minidom import Document
from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index, name="ShopHome"),
    path("about/",views.about, name="AboutUs"),
    path("contact/",views.contact, name="ContactUs"),
    path("tracker/",views.tracker, name="TrakingStatus"),
    path("search/",views.search, name="Search"),
    path("products/<int:myid>",views.productView, name="ProductView"),
    path("checkout/",views.checkout, name="Checkout"),
    path("handlerequest/",views.handlerequest, name="HandleRequest"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)