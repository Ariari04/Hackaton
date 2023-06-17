from django.db import models


class Language(models.Model):
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value


class ServiceCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Document(models.Model):
    value = models.ImageField(upload_to='')

    def __str__(self):
        return self.value


INSTITUTE_CATEGORY = (('Детский сад', 'Детский сад'),
                      ('Школа', 'Школа'),
                      ('Колледж', 'Колледж'),
                      ('ВУЗ', 'ВУЗ'))


class Institute(models.Model):
    category = models.CharField(choices=INSTITUTE_CATEGORY, max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title


class InstituteEvent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    organizer = models.ForeignKey('Institute', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


RATING = ((1, 1),
          (2, 2),
          (3, 3),
          (4, 4),
          (5, 5),)


class Review(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    rating = models.IntegerField(choices=RATING)
    related_to = models.ForeignKey('Institute', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
