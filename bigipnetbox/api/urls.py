from rest_framework import routers
from .views import *

app_name = 'bigipnetbox-api'

router = routers.DefaultRouter()

router.register('node', NodeViewSet)
router.register('pool', PoolViewSet)
router.register('poolmember', PoolMemberViewSet)
router.register('virtualserver', VirtualServerViewSet)
router.register('virtualaddress', VirtualAddressViewSet)
router.register('clusterf5', Clusterf5ViewSet)
router.register('partition', PartitionViewSet)
router.register('irule', IruleViewSet)
router.register('devicef5', Devicef5ViewSet)


urlpatterns = router.urls