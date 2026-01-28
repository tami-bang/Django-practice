from django import forms
from .models import Employees

class EmployeeForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('M', '남'),
        ('F', '여'),
    ]

    # 성별 선택
    gender = forms.ChoiceField(
        choices=[('', '성별 선택')] + GENDER_CHOICES,
        widget=forms.Select(attrs={
            "class": "form-select"
        }),
        required=True
    )

    birth_date = forms.DateField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "id": "birth_date_input",  # id 추가
            "placeholder": "생년월일 선택",
            "autocomplete": "off"
        })
    )

    hire_date = forms.DateField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "id": "hire_date_input",  # id 추가
            "placeholder": "입사일 선택",
            "autocomplete": "off"
        })
    )

    class Meta:
        model = Employees
        fields = ["emp_no", "birth_date", "first_name", "last_name", "gender", "hire_date"]
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