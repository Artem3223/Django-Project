from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    img = models.ImageField(default = 'default.jpg', upload_to = 'user_images')


    def __str__(self):
        return f'Профиль пользователя {self.user.username}'

def save(self, *args, **kwards):
    super().save()
    image = Image.open(self.img.path)

    if image.height > 254 or image.width > 254:
        resize = {254, 254 }
        image.thumbnail(resize)
        image.save(self.img.path)
