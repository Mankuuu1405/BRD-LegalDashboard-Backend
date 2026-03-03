from rest_framework import serializers
from .models import Document, Review, Report,DocumentDetail


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
class DocumentDetailSerializer(serializers.ModelSerializer):
    average_tat = serializers.SerializerMethodField()

    class Meta:
        model = DocumentDetail
        fields = '__all__'

    def get_average_tat(self, obj):
        return obj.average_tat()       