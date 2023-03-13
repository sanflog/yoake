from django.contrib import admin

from .models import thinkingFunction
from .models import thinkingFunctionDetail

admin.site.register(thinkingFunction)
admin.site.register(thinkingFunctionDetail)

