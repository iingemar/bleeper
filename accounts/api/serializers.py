from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from rest_framework import serializers

from app_name.models import Bleep

# Serializers allow complex data such as query sets and model instances to be
# converted to native Python data types that can then be easily rendered into
# JSON, XML or other content types. Serializers also provide deserialization,
# allowing parsed data to be converted back into complex types, after first
# validating the incoming data.

# ModelSerializer class which provides a useful shortcut for creating
# serializers that deal with model instances and querysets.


User = get_user_model()


class UserDisplaySerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            # 'email',
            'follower_count',
            'url'
        ]

    # Must be 'get_' followed by field name above.
    # Obj is the User instance.
    def get_follower_count(self, obj):
        print(obj.username)
        return 0

    def get_url(self, obj):
        return reverse_lazy('profiles:detail', kwargs={'username': obj.username})

