from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,SkillViewSet,TaskViewSet,BidViewSet

router =  DefaultRouter()

router.register("users",UserViewSet)
router.register("tasks",TaskViewSet)
router.register("bids",BidViewSet)
router.register("skills",SkillViewSet)

urlpatterns = [
    path("",include(router.urls))
]