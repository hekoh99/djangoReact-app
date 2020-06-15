from django.contrib import admin
from chat.models import Chat

# Register your models here.
@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'create_dt') #Post 객체를 보여줄 때 id와 title, modify_dt를 화면에 출력
    list_filter = ('create_dt',)
    search_fields = ('name',) #검색 박스를 표시하고 내용은 제목과 내용에서 검색되도록
