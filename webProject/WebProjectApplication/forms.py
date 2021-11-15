from django import forms
from .models import *
from django.contrib.auth.models import User

class TovarForm(forms.ModelForm):
    class Meta:
        model = Tovar
        fields = 'name', 'edizm', 'kodkategorii'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Название товара'
        self.fields['edizm'].label = 'Единицы измерения'
        self.fields['kodkategorii'].label = 'Код категории'

class KategoryForm(forms.ModelForm):
    class Meta:
        model = Kategoriitovara
        fields = 'namekategorii',
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['namekategorii'].label = 'Название категории'

class NalogiForm(forms.ModelForm):
    class Meta:
        model = Nalogi
        fields = 'namenaloga', 'percent'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['namenaloga'].label = 'Название налога'
        self.fields['percent'].label = 'Процент'

class DvizhenieForm(forms.ModelForm):
    class Meta:
        model = Dvizhenie
        fields = 'articul', 'kolvotovara', 'cena'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['articul'].label = 'Артикул товара'
        self.fields['kolvotovara'].label = 'Кол-во товара'
        self.fields['cena'].label = 'Цена'

class OrgForm(forms.ModelForm):
    class Meta:
        model = Organizatsiya
        fields = 'nameorg', 'kodbanka', 'schetorg', 'adress', 'fioruk', 'phone'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nameorg'].label = 'Название организации'
        self.fields['kodbanka'].label = 'Код банка'
        self.fields['schetorg'].label = 'Счет организации'
        self.fields['adress'].label = 'Адрес'
        self.fields['fioruk'].label = 'ФИО руководителя'
        self.fields['phone'].label = 'Телефон'

class NakladnieForm(forms.ModelForm):
    class Meta:
        model = Nakladnie
        fields = 'nnakladnoy', 'date', 'priznak', 'kodorg'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nnakladnoy'].label = 'Номер накладной'
        self.fields['date'].label = 'Дата'
        self.fields['priznak'].label = 'Признак накладной'
        self.fields['kodorg'].label = 'Код организации'

class PodrForm(forms.ModelForm):
    class Meta:
        model = Podrazdeleniya
        fields = 'kodsklada', 'namesklada', 'fio'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kodsklada'].label = 'Код склада'
        self.fields['namesklada'].label = 'Название склада'
        self.fields['fio'].label = 'ФИО складовщика'

class TaksForm(forms.ModelForm):
    class Meta:
        model = Taksirovka
        fields = 'nnakladnoy', 'kodnaloga', 'sumnaloga'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nnakladnoy'].label = 'Номер накладной'
        self.fields['kodnaloga'].label = 'Код налога'
        self.fields['sumnaloga'].label = 'Сумма налога'

class OstForm(forms.ModelForm):
    class Meta:
        model = Ostatki
        fields = 'articul', 'srcena', 'kolvotovarananachalo', 'kolvoprihod', 'kolvorashod'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['articul'].label = 'Артикул'
        self.fields['srcena'].label = 'Средняя цена'
        self.fields['kolvotovarananachalo'].label = 'Кол-во товара на начало месяца'
        self.fields['kolvoprihod'].label = 'Кол-во приход'
        self.fields['kolvorashod'].label = 'Кол-во расход'

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

