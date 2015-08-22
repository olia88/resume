#-*- coding: utf-8 -*-
from django import forms
from myapp.models import Member
from django.forms import MultiValueField, CharField, ChoiceField, MultiWidget, TextInput, Select
from django.core.exceptions import NON_FIELD_ERRORS


class PhoneWidget(MultiWidget):
    def __init__(self, code_length=3, num_length=7, attrs = None):
        widgets = [TextInput(attrs={'size': code_length, 'max_length': 3}),
                   TextInput(attrs={'size': num_length, 'max_length': num_length})]
        super(PhoneWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.code, value.number]
        else:
            return ['ххх', 'ххххххх']

    def format_output(self, rendered_widgets):
        return '(' + rendered_widgets[0] + ') - ' + rendered_widgets[1]


class PhoneField(MultiValueField):
    def __init__(self, code_length=3, num_length=7, *args, **kwargs):
        list_fields = [CharField(max_length=3),
                       CharField(max_length=7)]
        super(PhoneField, self).__init__(list_fields, widget=PhoneWidget(code_length, num_length), *args, **kwargs)

    def compress(self, values):
        return values[0] + values[1]


class DateWidget(MultiWidget):
    def __init__(self, year_length=4, month_length=2, day_length=2, attrs=None):
        widgets = [TextInput(attrs={'size': year_length, 'max_length': year_length}),
                   TextInput(attrs={'size': month_length, 'max_length': month_length}),
                   TextInput(attrs={'size': day_length, 'max_length': day_length})]
        super(DateWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.year, value.month, value.day
        else:
            return 'гггг', 'мм', 'дд'

    def format_output(self, rendered_widgets):
        return  rendered_widgets[0] + ' - ' + rendered_widgets[1] + ' - ' + rendered_widgets[2]


class DateField(MultiValueField):
    def __init__(self, year_length=4, month_length=2, day_length=2, *args, **kwargs):
        list_fields = [CharField(max_length=4),
                       CharField(max_length=2),
                       CharField(max_length=2)]
        super(DateField, self).__init__(list_fields, widget=DateWidget(year_length, month_length, day_length), *args, **kwargs)

    def compress(self, values):
        return str(values[0] + '-' + values[1] + '-' + values[2])


class MemberForm(forms.ModelForm):
    phone_number = PhoneField(code_length=3, num_length=7, label='Номер телефона')
    date_of_birth = DateField(label='Дата рождения')

    class Meta:
        model = Member
        widgets = {'date_of_birth': DateWidget, 'phone_number':PhoneWidget()}
        fields=['first_name', 'last_name', 'phone_number', 'date_of_birth', 'avatar']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone_number': 'Номер телефона',
            'date_of_birth': 'Дата рождения',
            'avatar' : 'Загрузить изображение'
        }
        error_messages = {NON_FIELD_ERRORS:{'phone_number':'Введите верный номер телефона',
                          'date_of_birth':'Введите дату формата ХХХХ-ХХ-ХХ',
        }
        }

    def clean_first_name(self):
        first_name=self.cleaned_data.get('first_name')
        return first_name

    def clean_last_name(self):
        last_name=self.cleaned_data.get('last_name')
        return last_name

    def clean_phone_number(self):
        # phone_number = forms.PhoneField()
        phone_number = self.cleaned_data.get('phone_number')
        # if phone_number.is_valid:
        #     phone_number
        # else:
        #     raise forms.ValidationError(
        #         self.error_messages['phone_number']
        return phone_number
