from django.db import models
import uuid as uuid_model


class ModelPermissionsMixin:

    @staticmethod
    def has_list_permission(request):
        return True

    @staticmethod
    def has_write_permission(request):
        return True

    def has_object_write_permission(self, request):
        return True

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True


class BaseModel(ModelPermissionsMixin, models.Model):
    id = models.UUIDField(default=uuid_model.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class BaseIndexedModel(BaseModel):

    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, db_index=True)

    class Meta:
        abstract = True
