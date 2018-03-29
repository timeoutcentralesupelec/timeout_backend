from rest_framework import serializers

from events.models.Association import Association


class AssociationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='pk')

    class Meta:
        model = Association
        fields = ('id', 'name') # All the fields you wish to get
