from models import Organization
from rest_framework import viewsets
from Project1.testdb.serializer import OrgSerializer

class OrgViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all().order_by('-date_joined')
    serializer_class = OrgSerializer