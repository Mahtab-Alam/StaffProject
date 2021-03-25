from staffapp.viewsets import StaffViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('staff', StaffViewset)