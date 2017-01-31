from rest_framework import serializers

from app_name.models import Bleep

# Serializers allow complex data such as query sets and model instances to be
# converted to native Python data types that can then be easily rendered into
# JSON, XML or other content types. Serializers also provide deserialization,
# allowing parsed data to be converted back into complex types, after first
# validating the incoming data.

# ModelSerializer class which provides a useful shortcut for creating
# serializers that deal with model instances and querysets.


class BleepModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bleep
        fields = [
            'user',
            'content',
            'timestamp'
        ]