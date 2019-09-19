from django.db import models

# Create your models here.

# GENDER_LIST=(
#     (1,'男'),
#     (2,'女'),
# )
GENDER_LIST=(
    (1,'男'),
    (2,'女'),
)

class Author(models.Model):
    name=models.CharField(max_length=32,verbose_name='作者名字')
    age=models.IntegerField(verbose_name='年龄')
    # gender=models.CharField(max_length=8,verbose_name='性别')
    gender=models.IntegerField(choices=GENDER_LIST,verbose_name='性别')   ##1 男  2女
    email=models.CharField(max_length=32,verbose_name='邮箱')

    def __str__(self):
        return self.name

    class Meta:
        db_table='author'

class Type(models.Model):
    name=models.CharField(max_length=32)
    description=models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        db_table='type'

class Article(models.Model):
    title=models.CharField(max_length=32,verbose_name='标题')
    date=models.DateField(auto_now=True,verbose_name='日期')
    content= models.TextField(verbose_name='文章')
    description=models.TextField(verbose_name='描述')
    ##图片类型
    ##upload_to 指定文件上传位置   static 目录下的 images目录中
    picture = models.ImageField(upload_to='images')
    recommend= models.IntegerField(verbose_name='推荐',default=0)
    heat=models.IntegerField(verbose_name='热度',default=0)
    author=models.ForeignKey(to=Author,on_delete=models.SET_DEFAULT,default=1,verbose_name='作者')
    type=models.ManyToManyField(to=Type)

    def __str__(self):
        return self.title

    class Meta:
        db_table='article'


class User(models.Model):
    name=models.CharField(max_length=32)
    password=models.CharField(max_length=32)

    class Meta:
        db_table='user'