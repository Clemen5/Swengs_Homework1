from django.db import models


class Publisher(models.Model):
    name = models.TextField()
    origin = models.TextField(default="Origin")

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'

    def __str__(self): return self.name


class Book(models.Model):
    CHOICES = (
        ('t', 'Thriller'),
        ('a', 'Adventure')
    )

    title = models.TextField()
    genre = models.CharField(max_length=1, choices=CHOICES)
    release_date = models.DateField()
    plot = models.TextField()
    pages = models.PositiveIntegerField(help_text="in Pages")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField('Author')

    def __str__(self): return self.title


class AuthorManager(models.Manager):

    def duplicates(self):
        # TODO: implement an algorithm to find duplicate entries
        return []


class Author(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    year_of_birth = models.IntegerField()

    objects = AuthorManager()

    def __str__(self): return self.first_name + " " + self.last_name