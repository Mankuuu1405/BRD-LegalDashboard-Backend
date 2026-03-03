from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Agreement
from .Serializers import AgreementSerializer


# 1️⃣ Agreements Table
class AgreementListView(APIView):

    def get(self, request):

        agreements = Agreement.objects.all()
        serializer = AgreementSerializer(agreements, many=True)

        return Response(serializer.data)


# 2️⃣ Dashboard Numbers
class DashboardStatsView(APIView):

    def get(self, request):

        total = Agreement.objects.count()
        pending = Agreement.objects.filter(status="Pending").count()
        approved = Agreement.objects.filter(status="Approved").count()
        high_priority = Agreement.objects.filter(priority="High").count()

        data = {
            "total_agreements": total,
            "pending_review": pending,
            "approved": approved,
            "high_priority": high_priority
        }

        return Response(data)


# 3️⃣ New Agreement
class CreateAgreementView(APIView):

    def post(self, request):

        serializer = AgreementSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Agreement created successfully"})

        return Response(serializer.errors)


# 4️⃣ Bulk Assign
class BulkAssignView(APIView):

    def post(self, request):

        agreements = request.data.get("agreements")
        assignee = request.data.get("assigned_to")

        Agreement.objects.filter(
            agreement_id__in=agreements
        ).update(assigned_to=assignee)

        return Response({"message": "Bulk assignment successful"})