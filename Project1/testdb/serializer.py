from models import Organization
from rest_framework import serializers

class OrgSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'name', 'parent', 'cid', 'key', 'FullName', 'position', 'human_id', 'subposition')
