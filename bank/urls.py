from django.urls import include,path
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register(r'banks',views.BanksViewSet)
router.register(r'branches/autocomplete',views.BranchAutocompleteViewSet, basename='branches')
router.register(r'branches',views.BranchesViewSet,basename='branches')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]