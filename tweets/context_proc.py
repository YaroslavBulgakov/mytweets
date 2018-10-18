'''
Этот файл нам нужен чтобы в глобальном контексте зарегать нашу переменную с формой
'''
from .forms import TweetForm

def FormRegiter(request):
    return {'form':TweetForm}