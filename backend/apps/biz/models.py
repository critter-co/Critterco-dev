import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.gis.db import models
from django.utils.translation import ugettext as _
from django.core.validators import RegexValidator
from apps.core.models import User

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

instagram_regex = RegexValidator(
    regex=r"^(?:(?:http|https):\/\/)?(?:www\.)?(?:instagram\.com|instagr\.am)\/([A-Za-z0-9-_\.]+)",
    message="Please enter a valid Instagram ID.",
)

telegram_regex = RegexValidator(
    regex=r"^(?:(?:http|https):\/\/)?(?:www\.)?(?:telegram\.me|t\.me|telegram.dog)\/([A-Za-z0-9-_\.]+)$",
    message="Please enter a valid Telegram ID.",
)


class Biz(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=100)
    phone = PhoneNumberField(blank=True)
    phone2 = models.CharField(
        validators=[phone2_regex], max_length=17, default='', blank=True)
    gallery = models.ImageField(default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    location = models.PointField()
    website = models.URLField(max_length=50, default='', blank=True)
    instagram = models.CharField(
        validators=[instagram_regex], max_length=255, default='', blank=True
    )
    telegram = models.CharField(
        validators=[telegram_regex], max_length=255, default='', blank=True
    )
    is_claimed = models.BooleanField(default=False)
    claimed_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )


class Hours(models.Model):
    biz = models.ForeignKey(Biz, on_delete=models.CASCADE)
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        unique_together = ("biz", "weekday", "from_hour")
        verbose_name = _("Hour")
        verbose_name_plural = _("Hours")
