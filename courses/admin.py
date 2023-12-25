from django.contrib import admin
from .models import Course, Learning, Prerequisite, Tag
from .models import Video
from .models import UserCourse, Payment
# Register your models here.

class TagAdmin(admin.TabularInline):
    model = Tag
    
class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class LearningAdmin(admin.TabularInline):
    model = Learning
    
class VideoAdmin(admin.TabularInline):
    model = Video

# 新增課程時，一併新增 Tag, Prerequisite, Learning, Video
class CourseAdmin(admin.ModelAdmin):
    inlines = [LearningAdmin, PrerequisiteAdmin, TagAdmin, VideoAdmin]

admin.site.register(Course, CourseAdmin)
admin.site.register(Video)
admin.site.register(UserCourse)
admin.site.register(Payment)