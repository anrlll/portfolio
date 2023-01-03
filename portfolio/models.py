from django.db import models

#プロフィール
class Profile(models.Model):
    name = models.CharField('名前',max_length=100)
    introduction = models.TextField('自己紹介')
    address = models.CharField('連絡先',max_length=100)
    github = models.CharField('github',max_length=100)
    topimage = models.ImageField('メイン画像')
    subimage = models.ImageField('サブ画像')

    def __str__(self):
        return self.name

#実績
class Achievement(models.Model):
    title = models.CharField('タイトル',max_length=100)
    description = models.TextField('説明')
    Image = models.ImageField('画像')
    url = models.CharField('URL',max_length=100)
    created = models.DateField('作成日時')

    def __str__(self):
        return self.title

#news
class News(models.Model):
    title = models.CharField('タイトル',max_length=100)
    article = models.TextField('記事')
    mainImage = models.ImageField('メイン画像')
    subImage = models.ImageField('サブ画像')
    created = models.DateField('作成日時')

    def __str__(self):
        return self.title

