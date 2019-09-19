from django import forms

class Register(forms.Form):
    name=forms.CharField(required=True,label='名字')
    password=forms.CharField(max_length=8,min_length=6,label='密码')


    ##固定写法
    def clean_name(self):
        name=self.cleaned_data.get('name')
        if name=='admin':
            self.add_error('name','不可以是admin')
        else:
            return name