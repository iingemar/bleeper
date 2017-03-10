from django.utils.timesince import timesince

from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from app_name.models import Bleep

# Serializers allow complex data such as query sets and model instances to be
# converted to native Python data types that can then be easily rendered into
# JSON, XML or other content types. Serializers also provide deserialization,
# allowing parsed data to be converted back into complex types, after first
# validating the incoming data.

# ModelSerializer class which provides a useful shortcut for creating
# serializers that deal with model instances and querysets.


class BleepModelSerializer(serializers.ModelSerializer):
    # Only for reading.
    # You can also use write_only=True/False
    user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Bleep
        fields = [
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
            'url'
        ]

    def get_date_display(self, obj):
        return obj.timestamp.strftime('%b %d, %I:%M %p ')

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + ' ago'

    def get_url(self, obj):
        return obj.get_absolute_url()
