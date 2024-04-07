from django.db import models

class Sign_type(models.Model):
  category = models.TextField()
  num = models.IntegerField("номер знака")
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to="sign_image/")
  description = models.TextField()

  def __str__(self):
    return self.name
    
  class Meta:
    verbose_name = "тип знака"
    verbose_name_plural = "типы знаков"


  
