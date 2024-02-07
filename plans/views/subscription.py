from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from accounts.permissions.isVisitor import IsVisitor
from accounts.permissions.isMember import IsMember
from accounts.permissions.isCoach import IsCoach
from accounts.permissions.isAdmin import IsAdmin
from plans.permissions.isSubscriptionOwner import IsSubscriptionOwner
from plans.serializers.subscription import SubscriptionSerializer
from plans.filters.subscription import SubscriptionFilter
from plans.models.subscription import Subscription
from authentication.utils.token import JWTToken


class SubscriptionListCreate(ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SubscriptionFilter

    def get_queryset(self):
        qs = super().get_queryset()

        token = self.request.auth.token.decode()
        payload = JWTToken.get_payload(token)

        user_role = payload.get("user_role")
        if user_role == "admin":
            return qs
        elif user_role == "coach":
            return qs.filter(coach=payload.get("user_id"))
        elif user_role == "member":
            return qs.filter(member=payload.get("user_id"))

        return qs.none()

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & (IsAdmin | IsCoach | IsMember)]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated & (IsVisitor | IsMember)]
        return super().get_permissions()


class SubscriptionRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [
                IsAuthenticated & (IsAdmin | IsSubscriptionOwner)
            ]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()
