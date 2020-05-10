import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.gis.db import models
from django.utils.translation import ugettext as _
from django.core.validators import RegexValidator

WEEKDAYS = [
    (1, _("Saturday")),
    (2, _("Sunday")),
    (3, _("Monday")),
    (4, _("Tuesday")),
    (5, _("Wednesday")),
    (6, _("Thursday")),
    (7, _("Friday")),
]

phone2_regex = RegexValidator(
    regex=r"^0\d{2}\d{8}$",
    message="Phone number must be entered in the following format: '02112345678'.",
)


class Biz(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    phone = PhoneNumberField()
    phone2 = models.CharField(
        validators=[phone2_regex], max_length=11, null=True, blank=True
    )
    gallery = models.ImageField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    location = models.PointField(blank=True, null=True)


class Hours(models.Model):
    biz = models.ForeignKey(Biz, on_delete=models.CASCADE)
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        unique_together = ("biz", "weekday", "from_hour")
