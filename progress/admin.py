from django.contrib import admin
from .models import Progresse, WebsiteIdea, VisualStudioCodeLink, Excel, Assignment, Messages

class ProgresseAdmin(admin.ModelAdmin):
  list_display = ('name', 'date')

class WebsiteIdeaAdmin(admin.ModelAdmin):
  list_display = ('Website_Idea', 'Date')

class VisualStudioCodeLinkAdmin(admin.ModelAdmin):
  list_display = ('Title', 'Date')

class ExcelAdmin(admin.ModelAdmin):
  list_display = ('Title', 'Date')

class AssignmentAdmin(admin.ModelAdmin):
  list_display = ('Task', 'Resolved','Date_Assigned', 'Assigned_To','Assigned_By', 'Due_Date', 'Latest_Important_Message','Message_Posted_At',)

class MessagesAdmin(admin.ModelAdmin):
  list_display = ('Message', 'Time','To', 'From','Response', 'Time_Of_Response')


admin.site.register(Progresse, ProgresseAdmin)
admin.site.register(WebsiteIdea, WebsiteIdeaAdmin)
admin.site.register(VisualStudioCodeLink,VisualStudioCodeLinkAdmin)
admin.site.register(Excel, ExcelAdmin)
admin.site.register(Assignment, AssignmentAdmin )
admin.site.register(Messages, MessagesAdmin )
# Register your models here.
