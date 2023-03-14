from django.db import models
from register.models import RegisterModel

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Posts(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=200)
    author=models.ForeignKey(RegisterModel, on_delete=models.CASCADE)
    content=models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return str(self.title)+' '+str(self.author)+' '+str(self.content)+' '+str(self.status)
    

