from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import now
from django.db.models import Avg
from datetime import timedelta

from .models import Document, Review, Report
from .serializers import (
    DocumentSerializer,
    ReviewSerializer,
    ReportSerializer
)


# =========================
# DOCUMENT VIEWSET
# =========================
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


# =========================
# REVIEW VIEWSET
# =========================
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# =========================
# REPORT VIEWSET
# =========================
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


# =========================
# DASHBOARD SUMMARY API
# =========================
class DashboardSummaryAPIView(APIView):

    def get(self, request):

        pending_reviews = Review.objects.filter(status="Pending").count()

        approved_today = Review.objects.filter(
            status="Approved",
            created_at__date=now().date()
        ).count()

        total_reviews = Review.objects.count()
        compliance_score = 0

        if total_reviews > 0:
            approved_count = Review.objects.filter(status="Approved").count()
            compliance_score = round((approved_count / total_reviews) * 100, 2)

        return Response({
            "pending_reviews": pending_reviews,
            "approved_today": approved_today,
            "compliance_score": compliance_score
        })
from rest_framework.generics import RetrieveAPIView
from .models import DocumentDetail
from .serializers import DocumentDetailSerializer


class DocumentDetailAPIView(RetrieveAPIView):
    queryset = DocumentDetail.objects.all()
    serializer_class = DocumentDetailSerializer
    lookup_field = 'document_id'