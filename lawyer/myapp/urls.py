
from django.urls import path, include
from .views import lawyerView,cityView, stateView

urlpatterns = [
    path("api/lawyer", lawyerView),
    path("api/city", cityView),
    path("api/state", stateView)
]