#encoding=utf-8
from django.db import models
from django.contrib import admin

class DepProject(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=300, blank=True, default='')
    itemsNum = models.IntegerField(default=0, blank=True)   # 组件个数
    successNum = models.IntegerField(default=0, blank=True) # 成功部署的次数
    failNum = models.IntegerField(default=0, blank=True) # 失败的部署次数
    status = models.IntegerField(default=0, blank=True)
    updateTime = models.DateTimeField(default=None, blank=True)
    createTime = models.DateTimeField(default=None, blank=True)

    def __unicode__(self):
        return u"%s_%s" % (self.name, self.desc)



class ProjectItems(models.Model):
    proId = models.ForeignKey(DepProject)     #对应的项目id
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=300, blank=True, default='')
    successNum = models.IntegerField(default=0, blank=True)     # 成功部署的次数
    failNum = models.IntegerField(default=0, blank=True)        # 失败的部署次数
    status = models.IntegerField(default=0, blank=True)
    buildUrl = models.URLField(blank=True)                      # 构建系统的地址
    buildArgs = models.CharField(max_length=300, blank=True)                # 构建参数
    updateTime = models.DateTimeField(default=None, blank=True)
    createTime = models.DateTimeField(default=None, blank=True)


    def __unicode__(self):
        return u'%s_%s' % (self.name, self.desc)



class itemLocation(models.Model):
    itemId = models.ForeignKey(ProjectItems)     # 组件id
    itemName = models.CharField(max_length=100)  # 组件名称
    name = models.CharField(max_length=100)      # 地址名称
    desc = models.TextField(max_length=300, blank=True, default='')  #地址描述
    hostIP = models.IPAddressField()             # 地址所在服务器的IP
    hostType = models.IntegerField(default=0)    # 服务器类型，0为linux服务器，1为windows服务器
    locatePath = models.CharField(max_length=400, blank=True)  # 在服务器的位置信息，目录
    bakPath = models.CharField(max_length=400, blank=True)     # 在服务器上的备份目录
    updateTime = models.DateTimeField(default=None, blank=True)
    createTime = models.DateTimeField(default=None, blank=True)

    def __unicode__(self):
        return u'%s_%s' % (self.name, self.desc)

admin.site.register(DepProject)
admin.site.register(ProjectItems)
admin.site.register(itemLocation)
