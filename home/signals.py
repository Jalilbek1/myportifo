from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import ContactMessage


@receiver(post_save, sender=ContactMessage)
def send_email_on_new_message(sender, instance, created, **kwargs):
    if created:  # Faqat yangi xabarlar uchun
        recipient_list = [instance.email]  # ContactMessage modelidan emailni olish

        send_mail(
            subject="Sizga yangi xabar keldi!",
            message=f"Salom {instance.name},\n\nSizning xabaringiz qabul qilindi:\n\n{instance.message}",
            from_email="jack.com12j@gmail.com",
            recipient_list=recipient_list,
            fail_silently=False,
        )
