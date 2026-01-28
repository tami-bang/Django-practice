# departments/models.py
from django.db import models

# Create your models here.
class Departments(models.Model):
    dept_no = models.CharField(max_length=4, primary_key=True)  # e.g. d001
    dept_name = models.CharField(max_length=40)                # e.g. Marketing

    class Meta:
        db_table = 'departments'   # 실제 DB 테이블 이름 지정
        managed = True             # Django가 테이블 관리

    def __str__(self):
        return f"{self.dept_no} - {self.dept_name}"