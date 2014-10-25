from django.db import models

class Campaign(models.Model):
    name = models.CharField(max_length = 128)
    target = models.DecimalField(max_digits = 9, decimal_places = 2)
    def __unicode__(self):
        return self.name
        
    def get_total(self):
        donations=self.donations_set.all()
        return sum([d.amount for d in donations])
    
    def get_togo(self):
        return self.target - self.get_total()
    
    def percent_complete(self):
        total = self.get_total()
        target = self.target
        if total >= target:
            return 1
        else:
            return total/target
    
# Create your models here.
class Donations(models.Model):
    full_name = models.CharField(max_length = 256)
    created_at = models.DateTimeField(auto_now_add = True)
    amount = models.DecimalField(
        max_digits = 9,
        decimal_places = 2
        )
    email = models.EmailField()
    campaign = models.ForeignKey(Campaign, null = True)
    
    def __unicode__(self):
        return '{0} - {1} - {2}'.format(
            self.full_name,
            self.email,
            self.amount)
            
