from django.db import models
from auxn_backend.settings import AUTH_USER_MODEL
from auxn_backend.utility import get_current_user


class HistoryModelMixin(models.Model):

    created_by = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="+"
    )
    updated_by = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+"
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """Automatically assign created_by and updated_by before saving."""
        user = get_current_user()
        if user and not self.pk:  # Assign created_by only on first save
            self.created_by = user
        if user:  # Always update updated_by
            self.updated_by = user
        super().save(*args, **kwargs)
