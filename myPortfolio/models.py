from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    phone = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        verbose_name="Phone Number"
    )
    subject = models.CharField(
        max_length=200, 
        blank=True, 
        null=True, 
        verbose_name="Subject"
    )
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Submitted On"
    )

    def __str__(self):
        return f"{self.name} ({self.email})"
