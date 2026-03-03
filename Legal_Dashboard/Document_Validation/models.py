from django.db import models

class Document(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Valid', 'Valid'),
        ('Invalid', 'Invalid'),
    ]

    document_id = models.AutoField(primary_key=True)  # Unique ID
    name = models.CharField(max_length=255)
    document_type = models.CharField(max_length=100)
    client_name = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    issues = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.document_id} - {self.name}"


class UploadDocuments(models.Model):
    document_type = models.CharField(max_length=100)
    client_name = models.CharField(max_length=255)
    document_file = models.FileField(upload_to='uploaded_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.document_type}"