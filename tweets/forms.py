'''
Итак тут мы создаем формы
Сам объект формы мы также передаем в представление в
Также что еще удобно для любых полей мы можем передавать виджеты, в которых они будут выведены
а также задавать некоторые аатрибуты, передавая их словарем в конструтор виджета
Опции
label - метка формы будет выведена при генерации кода
widget - виджет вывода
help_text - справка по полю, віводиться во всплівающем окне

Поля
Тип поля	Описание
CharField	Возвращает строку.
IntegerField	Возвращает целое число.
DateField	Возвращает объект Python datetime.date
DateTimeField	Возвращает объект Python datetime.datetime
EmailField	Возвращает верный адрес электронной почты как строку
URLField	Возвращает действительный URL-адрес в виде строки.
Вот неполный список доступных форме виджетов:

Тип виджета	Описание
PasswordInput	Текстовое поле пароля.
Hiddenlnput	Скрытое поле ввода.
Textarea	Текстовая область, которая разрешает многострочный ввод
Filelnput	Поле загрузки файла.

'''
from django import forms

class TweetForm(forms.Form):
    text=forms.CharField(widget=forms.Textarea(attrs={'rows':1,'cols':85}),max_length=160,help_text='Максимально 160 символов')
    country=forms.CharField(widget=forms.HiddenInput(),required=False)
