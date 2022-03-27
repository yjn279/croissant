from django.db import models


class Layer(models.Model):
    title = models.CharField(max_length=64, blank=True, default='')
    description = models.TextField(blank=True, default='')
    # children = models.ManyToManyField('self', blank=True)
    # tasks = models.PositiveIntegerField(default=1)
    # progress = models.PositiveIntegerField(default=0)
    # owner = models.ForeignKey(get_user_model(), related_name='own', on_delete=models.CASCADE)  # 自身を自動で入れる  なぜかIDでなくnameになる
    # participants = models.ManyToManyField(get_user_model(), related_name='participate', blank=True)  # デフォルトを自身に
    # end_date = models.DateField(null=True)
    # end_time = models.TimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ['created']


# class Child(models.Model):
#     parent_id = models.ForeignKey(Layer, related_name='children', on_delete=models.CASCADE)
#     child_id = models.ForeignKey(Layer, related_name='parents', on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)


# class Tasks(models.Model):
#     layer_id = models.ForeignKey(Layer, related_name='tasks', on_delete=models.CASCADE)
#     amount = models.PositiveIntegerField(default=1)
#     created = models.DateTimeField(auto_now_add=True)


class Start(models.Model):
    layer = models.ForeignKey(Layer, related_name='start', on_delete=models.DO_NOTHING, db_constraint=False)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date) + ' ' +  str(self.time)
