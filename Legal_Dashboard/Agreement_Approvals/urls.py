from django.urls import path
from .views import (
    AgreementListView,
    DashboardStatsView,
    CreateAgreementView,
    BulkAssignView
)

urlpatterns = [

    path('list/', AgreementListView.as_view()),

    path('dashboard/', DashboardStatsView.as_view()),

    path('create/', CreateAgreementView.as_view()),

    path('bulk-assign/', BulkAssignView.as_view()),
]