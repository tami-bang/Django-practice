from django import forms
from .models import Employees

class EmployeeForm(forms.ModelForm) :
    GENDER_CHOICES = [
        ('M', '남'),
        ('F', '여'),
    ]

    gender = forms.ChoiceField(
        choices=[('', '성별 선택')] + GENDER_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta :
        model = Employees
        fields = ["emp_no", "first_name", "last_name", "gender"]
        widgets = {
            "emp_no": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "사원번호"
            }),
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "이름"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "성"
            }),
        }