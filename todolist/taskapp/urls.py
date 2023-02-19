from rest_framework.routers import DefaultRouter
from taskapp.views import TaskViewSet

# router = DefaultRouter(trailing_slash=False)
router = DefaultRouter()

app_name = "taskappapp"


router.register(
    prefix="tasks",
    viewset=TaskViewSet,
    basename="tasks",
)

urlpatterns = router.urls
