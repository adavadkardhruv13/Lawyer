
from django.urls import path, include
from .views import lawyerView,cityView, stateView, notaryView



urlpatterns = [
    path("api/lawyer", lawyerView),
    path("api/city", cityView),
    path("api/state", stateView),
    path("api/notary", notaryView),

]