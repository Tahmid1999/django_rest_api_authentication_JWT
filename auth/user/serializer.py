from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only':True}
        }
        
    def create(self, validated_data):
        #print("validated_data => ")
        #print(validated_data)
        password = validated_data.pop('password', None)
        #print("After validated_data.pop => ")
        #print(validated_data)
        #print("password = validated_data.pop('password', None) =>")
        #print(password)
        instance = self.Meta.model(**validated_data)
        #print("instance =>")
        #print(instance)
        if password is  not None:
            instance.set_password(password)
        instance.save()
        return instance