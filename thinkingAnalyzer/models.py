from django.db import models

class thinkingFunction(models.Model):
    functionChoices = [
        ('Perceive', 'Perceive'),
        ('Judgment', 'Judgment')
    ]

    typeChoices = [
        ('Sight', 'Sight'),
        ('Sound', 'Sound'),
        ('Touch', 'Touch'),
        ('Smell', 'Smell'),
        ('Taste', 'Taste'),
        ('Feeling', 'Feeling'),
        ('Thinking', 'Thinking')
    ]

    timeChoices = [
        ('Past', 'Past'),
        ('Now', 'Now'),
        ('Feature', 'Feature'),
        ('Possibility', 'possibility')
    ]

    title = models.CharField(max_length=50)     
    detail = models.CharField(max_length=500, blank=True)
    target = models.CharField(max_length=50)
    function = models.CharField(max_length=20, choices=functionChoices)
    fType = models.CharField(max_length=20, choices=typeChoices)
    time = models.CharField(max_length=20, choices=timeChoices)
    decideTo = models.CharField(max_length=50)

    def __str__(self):
        return self.title
