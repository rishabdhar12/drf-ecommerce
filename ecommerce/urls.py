from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ecommerce.products import views 

router = DefaultRouter()
router.register(r"category", viewset=views.CategoryView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
