from django.urls import include, path
# from rest_framework import routers
from . import views
from .views import product_detail

# router = routers.DefaultRouter()
# router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('users/',views.GetUser.as_view()),
    path('add/',views.CreateUSer.as_view()),
    path('iou/',views.CreateIOU.as_view()),
    path('iou/getsummary/<lender_id>/<borrower_id>/',views.product_detail.as_view())
]   