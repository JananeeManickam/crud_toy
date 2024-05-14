from django.db import models

# Create your models here.
class Toy(models.Model):
    toy_name = models.CharField('toy_name', primary_key=True, max_length=200)
    toy_model = models.DecimalField('toy_model',max_digits=10, decimal_places=0)
    toy_price = models.FloatField('toy_price')
    toy_description = models.CharField('toy_description', max_length=2000)
    
    class Meta: 
        db_table = 'toys'
        
    def __str__(self):
        return "{} from Model {}".format(self.toy_name, self.toy_model)