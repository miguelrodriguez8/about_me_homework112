from django.urls import path
# from .views import view_function
from .views import HomeView, AboutView
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns=[
    path("", HomeView.as_view(),name="home"),
    path("about/", AboutView.as_view(), name="about")]
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)