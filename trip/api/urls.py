from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripView, AreaView, upload_file

router = DefaultRouter()
router.register(r'trip', TripView, basename='trip')
router.register(r'area', AreaView, basename='area')


# urlpatterns = [
#     path('',include(router.urls)),
#     path('<int:pk>/<str:language>/', TripView.as_view({'get': 'retrieve'}), name='trip-detail'),
#     path('list/<str:language>/', TripView.as_view({'post': 'create', 'get': 'list'}), name='trip-list'),
#     # path('<str:language>/', TripView.as_view({'get': 'list_by_language'}), name='list-by-language'),
# ]
urlpatterns = router.urls

urlpatterns += [
    path("upload/", upload_file, name="upload"),
]