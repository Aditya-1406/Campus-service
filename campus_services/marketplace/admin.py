from django.contrib import admin
from .models import User, Skill, Task, Bid

admin.site.register(User)
admin.site.register(Skill)
admin.site.register(Task)
admin.site.register(Bid)