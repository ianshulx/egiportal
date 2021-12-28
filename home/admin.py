from django.contrib import admin

from home.models import book,notice, notice1, quiz, book, image, event1, Main_Event

# Register your models here.
admin.site.register(notice)
admin.site.register(notice1)
admin.site.register(Main_Event)

admin.site.register(quiz)
admin.site.register(book)
admin.site.register(image)
admin.site.register(event1)
