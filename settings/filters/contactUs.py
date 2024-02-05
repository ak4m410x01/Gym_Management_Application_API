import django_filters

from settings.models.contactUs import ContactUs


class ContactUsFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(field_name="country", lookup_expr="icontains")
    city = django_filters.CharFilter(field_name="city", lookup_expr="icontains")
    address = django_filters.CharFilter(field_name="address", lookup_expr="icontains")
    email = django_filters.CharFilter(field_name="email", lookup_expr="icontains")
    phone = django_filters.CharFilter(field_name="phone", lookup_expr="icontains")
    whatsapp = django_filters.CharFilter(field_name="whatsapp", lookup_expr="icontains")
    telegram = django_filters.CharFilter(field_name="telegram", lookup_expr="icontains")
    facebook = django_filters.CharFilter(field_name="facebook", lookup_expr="icontains")
    instagram = django_filters.CharFilter(
        field_name="instagram", lookup_expr="icontains"
    )
    twitter = django_filters.CharFilter(field_name="twitter", lookup_expr="icontains")

    class Meta:
        model = ContactUs
        fields = [
            "country",
            "city",
            "address",
            "email",
            "phone",
            "whatsapp",
            "telegram",
            "facebook",
            "instagram",
            "twitter",
        ]
