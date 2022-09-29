from django.contrib import admin
from .models import Book,StudentExtra,IssuedBook
class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)
class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, StudentExtraAdmin)
class IssuedBookAdmin(admin.ModelAdmin):
    pass
admin.site.register(IssuedBook, IssuedBookAdmin)
