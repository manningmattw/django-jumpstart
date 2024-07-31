from django.db import models
from django.contrib import admin


# https://docs.djangoproject.com/en/5.0/ref/models/
class Example(models.Model):
    CHOICE_0 = 0
    CHOICE_1 = 1
    CHOICE_2 = 2
    CHOICE_3 = 3
    CHOICE_4 = 4
    CHOICE_5 = 5
    CHOICES = (
        (CHOICE_0, ''),
        (CHOICE_1, '1st'),
        (CHOICE_2, '2nd'),
        (CHOICE_3, '3rd'),
        (CHOICE_4, '4th'),
        (CHOICE_5, '5th'))

    name = models.CharField(max_length=100)
    choice = models.SmallIntegerField(default=CHOICE_1, choices=CHOICES)
    is_something = models.BooleanField(default=False)

    def __repr__(self) -> str:
        return f'{self.name}'

    def __str__(self) -> str:
        return self.name

    @property
    def choice_value(self) -> str:
        for option, value in self.CHOICES:
            if option == self.choice:
                return value

        return ''

    @property
    def values_phrase(self) -> str:
        choice = f" ({self.choice_value})" if self.choice_value else ""
        is_something = "is something" if self.is_something else "is not something"

        return f"{self.name}{choice} {is_something}"


# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/
@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    pass
