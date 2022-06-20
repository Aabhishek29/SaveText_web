from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    name = models.CharField(
        max_length=30,blank=False,null=False)
    email = models.EmailField(
        max_length=100, blank=False, null=False, unique=True)
    password = models.CharField(
        max_length=15,blank=False,null=False
    )
    confirm_password = models.CharField(
        max_length=15,null=False,blank=False
    )
    hint_question_options = [
        ('first school name','First School Name'),
        ('pet name','Pet Name'),
        ('teacher name','Teacher Name'),
        ('favorate food','Favorate Food'),
        ('collage name','Collage Name')
    ]

    hint_question = models.CharField(
        max_length=30, blank=False, null=False,
        choices=hint_question_options,
    )

    hint_answer = models.CharField(
        max_length=30,blank=True,null=True
    )

    userId = models.CharField(
        max_length=15,null=False,blank=False,primary_key=True
    )


class SaveTextDocs(models.Model):
    file_name = models.CharField(
        max_length=30,null=True,blank=True
    )
    userId = models.ForeignKey(
        UserRegistration,
        default=None, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(
        blank=False, null=False
    )
    updateAt = models.DateTimeField(
        blank=False,null=False
    )
    docId = models.CharField(
        max_length=15, blank=False, null=False,
        primary_key=True
    )
    fileData = models.TextField(
        blank=True,null=True
    )

