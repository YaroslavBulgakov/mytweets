from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View
from userprofile.models import User
from tweets.models import Tweet,HashTag
from .forms import TweetForm

# Create your views here.


'''
Итак создадим классовое представление в них есть свои плюсы,для начала простое
а потом уже перейдем к немного более сложным

10.10.2018
Так ну что мы сделали на прошлом занятии
Это создали две модели одна в приложении userprofile другая в tweets
Отношение 1 пользователь - много твитов
Итак там где много будет ForeignKey() к username
То есть в твите должен быть вот этот ключ
Первая вьюха - мы берем пользователя, по пользователю выбираем его твиты
И помещаем пользователя и твиты в словарь

'''
class Index(View):
    def get(self,request):
        params={}

        params['name']='Django'
        return render(request,'base.html',params)
    def post(self,request):
        return HttpResponse('Запрос опубликован')

class Profile(View):
    #
    def get(self,request,username):
        user=User.objects.get(username=username)
        tweets=Tweet.objects.filter(user=user)
        ella_tweets=Tweet.ella_tweets.filter(text__icontains='ella')
        params={}
        params['user']=user
        params['tweets']=tweets
        params['ella_tweets']=ella_tweets
        return render(request,'profile.html',params)


'''
Итак мы создали форму в которой ссылаемся так
То есть
/user/username/ - вот так просто посты
post/ - вот так с формой
Мы вытягиваем username из УРЛ
И если форма валидная то создаем объект Твита и сохраняем его

'''

from .forms import TweetForm
class PostTweet(View):
    """Tweet Post form available on page /user/<username> URL"""
    def post(self,request,username):
        form=TweetForm(request.POST)

        if form.is_valid():
            user=User.objects.get(username=username)

            #Создаем объект и сохраняем алгоритм понятен из ссылки вытянули имя пользователя, по нему объект с которым свяжем Твит остальное из формы
            tweet=Tweet(text=form.cleaned_data['text'],user=user,country=form.cleaned_data['country'])
            tweet.save()
            words=form.cleaned_data['text'].split(" ")

        #Ага после того как создали твит нам нужно найти в тексте хэштег мы его разбили по словам и если нашли то создаем
        #хєштег метод get_or_create вернет сам объект и булево значение если создан объект то ТРУ или ФАЛСЕ если найден
            for word in words:
                if word[0]=='#':
                    hashtag,created=HashTag.objects.get_or_create(name=word[1:])
                #Затем т.к у нас пока в объекте хэш тега только имя, нам нужно еще добавить в немуу ссылку на объект твита что делается методом add это для полей ManyToMany
                    hashtag.tweet.add(tweet)
        #return HttpResponse(" ".join(words))
        return HttpResponseRedirect("/user/"+username)


#Теперь создадим странцу для хэш тегов
#в представление передается хэш тег

class HashTagCloud(View):
    def get(self,request,hashtag):
        params=dict()
        #Ну ладно с жтим разобрались
        hashtag=HashTag.objects.get(name=hashtag)
        #По объекту хэштега вытащим все твиты где он встречается
        params['tweets']=hashtag.tweet
        #Но можно еще и так
        return render(request,'hashtag.html',params)
