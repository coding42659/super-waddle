#DO NOT SEND TO GITHUB INCOMPLTLE CODE WILL BREAK WEBSITE


from django.contrib import admin
#<<<<<<< HEAD
from .models import Progresse, WebsiteIdea, VisualStudioCodeLink, Assignment, Message, File_Upload_Center, Statuse, ScheduledTask
#=======
from .models import Progresse, WebsiteIdea, VisualStudioCodeLink, Assignment, Message, File_Upload_Center, Availability
#>>>>>>> origin/Testing

class ProgresseAdmin(admin.ModelAdmin):
  list_display = ('name', 'date')

class WebsiteIdeaAdmin(admin.ModelAdmin):
  list_display = ('Website_Idea', 'Date')

class VisualStudioCodeLinkAdmin(admin.ModelAdmin):
  list_display = ('Title', 'Date')
  
class StatuseAdmin(admin.ModelAdmin):
  list_display = ('Document_Name','Date_Published')

class AvailabilityAdmin(admin.ModelAdmin):
  list_display = ('Name', 'Available', 'On_Docs', 'Notes','Updated_at')



class AssignmentAdmin(admin.ModelAdmin):
  list_display = ('Name_Of_Assignment', 'Resolved','Date_Assigned','Assigned_By',  'Primary_Assigned_Person', 'Secondary_Assigned_Person', 'Tertiary_Assigned_Person','Due_Date', 'Latest_Important_Message','Message_Posted_At',)

class MessageAdmin(admin.ModelAdmin):
  list_display = ('Message','From','To', 'Posted_At')

class File_Upload_CenterAdmin(admin.ModelAdmin):
  list_display = ('File_Name', 'Time')
  
class ScheduledTaskAdmin(admin.ModelAdmin):
  list_display = ('Task_Name', 'Due_At', 'Resolved')

admin.site.register(Progresse, ProgresseAdmin)
admin.site.register(WebsiteIdea, WebsiteIdeaAdmin)
admin.site.register(VisualStudioCodeLink,VisualStudioCodeLinkAdmin)

admin.site.register(Assignment, AssignmentAdmin )
admin.site.register(Message, MessageAdmin )
#<<<<<<< HEAD
admin.site.register(Statuse, StatuseAdmin )
admin.site.register(ScheduledTask, ScheduledTaskAdmin )
#=======
admin.site.register(Availability, AvailabilityAdmin)
#>>>>>>> origin/Testing
#admin.site.register(File_Upload_Center,File_Upload_CenterAdmin )

# Register your models here.
