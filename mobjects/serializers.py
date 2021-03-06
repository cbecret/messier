from django.contrib.auth.models import User
from rest_framework import serializers

from mobjects.models import Mobject


# Définition des champs utilisés pour nos objets de Messier
class MobjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mobject
        fields = ['id', 'messier_number', 'usual_name', 'ngc', 'constellation',
                 'messier_type', 'dimension', 'distance_value', 'distance_unit',
                 'magnitude', 'ascension', 'discovery_year', 'discoverer', 'image_link',
                 'owner']
        owner = serializers.ReadOnlyField(source='owner.username')

# Définition des champs utilisés pour nos utilisateurs
class UserSerializer(serializers.ModelSerializer):
    mobjects = serializers.PrimaryKeyRelatedField(many=True, queryset=Mobject.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'mobjects']