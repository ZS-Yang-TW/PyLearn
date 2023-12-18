from django.db import models

# 課程資料
class Course(models.Model):
    name = models.CharField(max_length = 30, null = False)
    slug = models.CharField(max_length = 30, null = False, unique = True)
    description = models.CharField(max_length = 200, null = True)
    price = models.IntegerField(null = False)   
    discount = models.IntegerField(default = 0, null = False)
    active = models.BooleanField(default = False)
    thumbnail = models.ImageField(upload_to = "files/thumbnail")
    date = models.DateField(auto_now_add = True)
    resource = models.FileField(upload_to = "files/resource")
    length = models.IntegerField(null = False)
    
    def __str__(self):
        return self.name

# 給 Tag, Prerequisite, Learning 用的抽象類別
class CourseProperty(models.Model):
    description = models.CharField(max_length = 100, null = False)
    course = models.ForeignKey(Course, on_delete = models.CASCADE, null = True)

    class Meta:
        abstract = True

# 學習內容
class Learning(CourseProperty):
    pass

# 先備知識
class Prerequisite(CourseProperty):
    pass

# 標籤
class Tag(CourseProperty):
    pass


class Video(models.Model):
    title = models.CharField(max_length = 100, null = False)
    course = models.ForeignKey(Course, on_delete = models.CASCADE, null = True)
    serial_number = models.IntegerField(null = False)
    video_id = models.CharField(max_length = 100, null = False)
    is_preview = models.BooleanField(default = False)
    
    def __str__(self):
        return self.title