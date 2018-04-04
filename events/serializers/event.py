from rest_framework import serializers

from events.models.Event import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='pk')
    asso = serializers.StringRelatedField(many = False, source = 'asso.name') #Needed if asso is foreign key in the Event model

    class Meta:
        model = Event
        fields = ('id', 'name', 'asso', 'date', 'end_date', 'description', 'image', 'link', 'location', 'price') # All the fields you wish to get
