from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    
    def save(self):
        if self.validated_data['password'] != self.validated_data['password2']:
            raise serializers.ValidationError({'error': 'password1 and password2 are not same'})
        elif User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists'})
        
        user = User.objects.create_user(username=self.validated_data['username'], email=self.validated_data['email'], password=self.validated_data['password'])
        user.save()
        return user
            
                