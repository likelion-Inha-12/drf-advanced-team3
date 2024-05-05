from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    title=models.CharField(max=100)
    created_date=models.DateTimeField(auto_now_add=True)
    deadline=models.DateTimeField() #json body 입력형식 : YYYY-MM-DDThh:mm:ssZ/예:''deadline':'2024-05-10T23:59:59Z'
    part_choices=[
        ('B', 'BE'),
        ('F', 'FE'), #튜플 형식. 첫번째 값 : 데이터베이스에 저장되는 값
        ('A', 'ALL') #          두번째 값 : 사용자에게 보여지는 값
    ]
    part=models.CharField(max_length=1,choices=part_choices)#정해진 옵션 중 하나만 쓸 수 있게 하는 용도, json body 입력예시 : 'part':'B'
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    assign_github_link=models.URLField()
    assign_content=models.CharField()

    def __str__(self):
        return self.title

class Submission(models.Model):
    assignment_id=models.ForeignKey(Assignment,on_delete=models.CASCADE)
    submit_content=models.TextField()
    submit_github_link=models.URLField()
    submit_date=models.DateTimeField(auto_now_add=True)

