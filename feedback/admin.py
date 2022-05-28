from django.contrib import admin
from .models import Question
from .models import Feedback

admin.site.register(Question)
admin.site.register(Feedback)

# Register your models here.
