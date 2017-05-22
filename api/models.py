from django.db import models


class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    class Meta:
        db_table = "Bucketlist"
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=140, default='SOME STRING')
    port = models.CharField(max_length=140, default='SOME STRING')
    connection_type = models.CharField(max_length=140, default='SOME STRING')
    anonymity = models.CharField(max_length=140, default='SOME STRING')
    country = models.CharField(max_length=140, default='SOME STRING')
    name = models.CharField(max_length=140, default='SOME STRING')
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, null=True, blank=True)


    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)