from django.db import models

from carzApis.models import UserModel
from django.utils.translation import gettext_lazy as _


class AddressModel(models.Model):
    title = models.CharField()
    address = models.CharField()
    user = models.ForeignKey(
        UserModel,
        on_delete= models.CASCADE,
     
 )

class PaymentMethod(models.Model):
    class CardType(models.TextChoices):
        VISA = "visa", _("Visa")
        MASTERCARD = "mastercard", _("MasterCard")
        AMEX = "amex", _("American Express")
        DISCOVER = "discover", _("Discover")
        OTHER = "other", _("Other")

    user = models.ForeignKey(
        UserModel,
        default= "",
        on_delete=models.CASCADE,
        related_name="payment_methods"
    )

    card_holder_name = models.CharField(max_length=100 , default= "")
    last4_digits = models.CharField(max_length=4, default= "")
    card_type = models.CharField(
        max_length=20,
        choices=CardType.choices,
        default=CardType.OTHER
    )
    expiry_month = models.CharField(max_length=2, default= "")
    expiry_year = models.CharField(max_length=4, default= "")
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

  
    
    
