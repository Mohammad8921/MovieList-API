from rest_framework.views import APIView
from user_app.api.serialziers import RegisterationSerializer
from rest_framework.response import Response
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework import status

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class LogoutView(APIView):
    def post(self, request):
        user = request.user
        Token.objects.get(user=user).delete()
        return Response({'Logout status': 'Successful'}) 
    
class RegisterationView(APIView):
    def post(self, request):
        serialzer = RegisterationSerializer(data=request.data)
        if serialzer.is_valid():
            user = serialzer.save()
            data = {
                'username': user.username,
                'email': user.email,
                'token': Token.objects.get(user=user).key,
                'Registeration status': 'Successful'
                }
            return Response(data, status=status.HTTP_201_CREATED)
            