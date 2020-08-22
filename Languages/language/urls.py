
from django.urls import path, include
from rest_framework import routers
from .views import ProgrammerView, ParadigmView, LanguageView

router = routers.DefaultRouter()

router.register('paradigm', ParadigmView)
router.register('language', LanguageView)
router.register('programmer', ProgrammerView)


urlpatterns = [ path('', include(router.urls))
]
