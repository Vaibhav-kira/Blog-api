from .serializer import (User, UserSerializer, )
from rest_framework.viewsets  import ModelViewSet

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serialiser_class = UserSerializer