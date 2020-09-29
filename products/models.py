from django.db import models
# there is model to access user we have created but we have model to access django user
from django.contrib.auth.models import User

class Product(models.Model):

    title = models.CharField(max_length=250)
    pub_data = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    icon = models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:70]

    def pub_date_pretty(self):
        return self.pub_data.strftime('%b %e %Y')



# hunter
