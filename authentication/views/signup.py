from rest_framework.generics import CreateAPIView
from accounts.models.visitor import Visitor
from authentication.serializers.signup import SignUpSerializer

class SignUp(CreateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = SignUpSerializer

