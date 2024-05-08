from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    title=models.CharField(max_length=100,verbose_name="과제 제목")
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="생성 일자")
    deadline=models.DateTimeField(verbose_name="마감 일자") #json body 입력형식 : YYYY-MM-DDThh:mm:ssZ/예:''deadline':'2024-05-10T23:59:59Z'
    part_choices=[
        ('B', 'BE'),
        ('F', 'FE'), #튜플 형식. 첫번째 값 : 데이터베이스에 저장되는 값
        ('A', 'ALL') #          두번째 값 : 사용자에게 보여지는 값
    ]
    part=models.CharField(max_length=1,choices=part_choices,verbose_name="과제 파트")#정해진 옵션 중 하나만 쓸 수 있게 하는 용도, json body 입력예시 : 'part':'B'
    tag = models.CharField(max_length=100, verbose_name="태그")
    assign_github_link=models.URLField(verbose_name="깃허브 링크")
    assign_content=models.TextField(verbose_name="과제 내용")

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs): #save 함수 오버라이딩. 기존의 save() 메서드 : 모델 인스턴스를 데이터베이스에 저장하는 역할
    # tag 값을 기준으로 Category를 생성하거나 가져옴
        tag=Category.objects.filter(name=self.tag).first()
        if not tag:
            tag = Category.objects.create(name=self.tag)
        self.tag = tag
        super().save(*args, **kwargs)

class Submission(models.Model):
    assignment_id=models.ForeignKey(Assignment,on_delete=models.CASCADE)
    submit_content=models.TextField(verbose_name="과제 설명")
    submit_github_link=models.URLField(verbose_name="깃허브 링크")
    submit_date=models.DateTimeField(auto_now_add=True, verbose_name="작성 일자")

    def __str__(self):
        return f"{self.assignment_id.id}번째 과제의 {self.id}번째 제출물입니다"