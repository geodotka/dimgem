from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    icon = models.ImageField('Ikonka Kategorii', upload_to='icons',
                              blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    posted_date = models.DateField()
    author = models.CharField(max_length=50)
    text = models.TextField()
    dim = models.BooleanField()
    categories = models.ForeignKey(Category)
    old_text = models.TextField(null=True, blank=True)
    picture = models.ImageField(
        upload_to='dimgem/static/dimgem/post_pictures', null=True,  blank=True)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return self.title

    @property
    def votes_up(self):
        return Vote.objects.filter(post=self, vote=True).count()

    @property
    def votes_down(self):
        return Vote.objects.filter(post=self, vote=False).count()


class Vote(models.Model):
    ip = models.IPAddressField()
    vote = models.BooleanField()
    post = models.ForeignKey(Post)
