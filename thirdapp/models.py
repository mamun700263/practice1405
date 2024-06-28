# myapp/models.py
from django.db import models
from django.core.exceptions import ValidationError



class Mymodel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    aim = models.BigIntegerField()
    Enter_binary = models.BinaryField()
    Are_you_happy = models.BooleanField()
    skills = models.CharField(
        validators=[],
        max_length=255

    )
    birth_day = models.DateField()
    birth_day1 = models.DateTimeField()
    cgpa = models.DecimalField(max_digits=5,decimal_places=2)
    duration = models.DurationField()
    resume = models.FileField(upload_to='files/')
    # filepath = models.FilePathField(path='/firstapp/')
    floatf = models.FloatField()
    # Foreign_key = models.ForeignKey()
    your_ip = models.GenericIPAddressField()
    your_photo = models.ImageField()
    json_field = models.JSONField()
    # manytomany = models.ManyToManyField(onno_model)
    # yes_no = models.NullBooleanField()
    # one2one = models.OneToOneField()
    slugfield = models.SlugField()
    paragraph = models.TextField()
    linkedin = models.URLField()
    unique = models.UUIDField()
    






    def __str__(self):
        return self.name
