from rest_framework import serializers
from api.models import CheckBox
from django.db.models import fields


class CheckBoxSerializer(serializers.ModelSerializer):

   # get_title =serializers.SerializerMethodField()
    class Meta:
        model = CheckBox
        fields = ["is_checked"] 

        @staticmethod
        def get_title(obj):
           return obj.name 


class DataSerializer(serializers.Serializer):

    title = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    attrs = serializers.JSONField(required=False) 
    type = serializers.CharField()   
    val_1 = serializers.IntegerField()  
    val_2 = serializers.IntegerField()  

    @staticmethod  
    def validate_type(type):
        if not type in ("dict", "list", "tuple"):
            raise serializers.ValidationError(f"{type} is not allowed") 
        return type     