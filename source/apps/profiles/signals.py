from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

""" Only delete the file if no other instances of that model are using it """


def delete_file_if_unused(model, instance, field, instance_file_field):
    dynamic_field = {}
    dynamic_field[field.name] = instance_file_field.name
    other_refs_exist = (
        model.objects.filter(**dynamic_field).exclude(pk=instance.pk).exists()
    )
    if not other_refs_exist:
        instance_file_field.delete(False)


""" Whenever ANY model is deleted, if it has a file field on it, delete the associated file too """


@receiver(post_delete)
def delete_files_when_row_deleted_from_db(sender, instance, **kwargs):
    for field in sender._meta.concrete_fields:
        if isinstance(field, models.FileField):
            instance_file_field = getattr(instance, field.name)
            delete_file_if_unused(sender, instance, field, instance_file_field)


""" Delete the file if something else get uploaded in its place """


@receiver(pre_save)
def delete_files_when_file_changed(sender, instance, **kwargs):
    # Don't run on initial save
    if not instance.pk:
        return
    for field in sender._meta.concrete_fields:
        if isinstance(field, models.FileField):
            # its got a file field. Let's see if it changed
            try:
                instance_in_db = sender.objects.get(pk=instance.pk)
            except sender.DoesNotExist:
                # We are probably in a transaction and the PK is just temporary
                # Don't worry about deleting attachments if they aren't actually saved yet.
                return
            instance_in_db_file_field = getattr(instance_in_db, field.name)
            instance_file_field = getattr(instance, field.name)
            if instance_in_db_file_field.name != instance_file_field.name:
                delete_file_if_unused(
                    sender, instance, field, instance_in_db_file_field
                )
