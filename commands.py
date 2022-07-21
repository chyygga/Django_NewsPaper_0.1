from django.contrib.auth.models import User
from news.models import Author, Category, Post, PostCategory, Comment

# Создать двух пользователей (с помощью метода User.objects.create_user('username')).
user_1 = User.objects.create_user(username='user_1', email='user_1@mail.ru', password='password1')
user_2 = User.objects.create_user(username='user_2', email='user_2@mail.ru', password='password2')
user_3 = User.objects.create_user(username='user_3', email='user_3@mail.ru', password='password3')

# Создать два объекта модели Author, связанные с пользователями.
user_1 = Author.objects.create(user=user_1)
user_2 = Author.objects.create(user=user_2)
user_3 = Author.objects.create(user=user_3)

# Добавить 4 категории в модель Category.
cat_sport = Category.objects.create(name="Спорт")
cat_music = Category.objects.create(name="Музыка")
cat_cinema = Category.objects.create(name="Кино")
cat_IT = Category.objects.create(name="IT")

# Добавить 2 статьи и 1 новость.
article_user_1 = Post.objects.create(author=user_1, post_type=Post.article, title="статья_спорт_кино_by_user_1", text='"статья_спорт_кино"')
article_user_2 = Post.objects.create(author=user_2, post_type=Post.article, title="статья_музыка_by_user_2", text='"статья_музыка"')
news_user_2 = Post.objects.create(author=user_2, post_type=Post.news, title="новость_IT_by_user_2", text='"новость_IT"')
news_user_3 = Post.objects.create(author=user_3, post_type=Post.news, title="новость_IT_by_user_3", text='"новость_IT_и_многое_другое"')

# Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
PostCategory.objects.create(post=article_user_1, category=cat_sport)
PostCategory.objects.create(post=article_user_1, category=cat_cinema)
PostCategory.objects.create(post=article_user_2, category=cat_music)
PostCategory.objects.create(post=news_user_2, category=cat_IT)

# Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
comment1 = Comment.objects.create(post=article_user_1, user=user_1.user, text="коммент №1 к статье User_2")
comment2 = Comment.objects.create(post=article_user_2, user=user_2.user, text="коммент №2 к статье User_1")
comment3 = Comment.objects.create(post=news_user_2, user=user_1.user, text="коммент №3 к новости User_2")
comment4 = Comment.objects.create(post=news_user_2, user=user_2.user, text="коммент №4 к новости User_2")


# Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
like_for_articles_user_1 = Post.like(article_user_1)
dislike_for_articles_user_2 = Post.dislike(article_user_2)
like_for_news_user_2 = Post.like(news_user_2)

like_for_comment1 = Comment.like(comment1)
like_for_comment2 = Comment.like(comment2)
like_for_comment3 = Comment.like(comment3)
like_for_comment4 = Comment.like(comment4)
dislike_for_comment3 = Comment.dislike(comment3)

# подсчет рейтингов
rating_user_1 = (sum([post.rating * 3 for post in Post.objects.filter(author=user_1)]) +
                 sum([comment.rating for comment in Comment.objects.filter(user=user_1.user)]) +
                 sum([comment.rating for comment in Comment.objects.filter(post__author=user_1)]))
rating_user_2 = (sum([post.rating * 3 for post in Post.objects.filter(author=user_2)]) +
                 sum([comment.rating for comment in Comment.objects.filter(user=user_2.user)]) +
                 sum([comment.rating for comment in Comment.objects.filter(post__author=user_2)]))

# Обновление рейтингов
user_1.update_rating(rating_user_1)
user_2.update_rating(rating_user_2)

# Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).

best_author = Author.objects.all().order_by('-rating')[0]
best_author = Author.objects.order_by('-rating').values('user__username', 'rating').first()
print(f'Лучший автор: {best_author.user.username} с рейтингом: {best_author.rating}')


# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
best_article = Post.objects.filter(post_type=Post.article).order_by('-rating')[0]
print(f'Лучшая статья: {best_article} \n'
      f'Дата добавления: {best_article.created} \n'
      f'Автор: {best_article.author.user.username} \n'
      f'Рейтинг: {best_article.rating} \n'
      f'Заголовок: {best_article.title} \n'
      f'Превью: {best_article.preview} \n')


# Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
for comment in Comment.objects.filter(post=best_article):
    print("Дата:", comment.created)
    print("Автор:", comment.user.username)
    print("Рейтинг:", comment.rating)
    print("Комментарий:", comment.text)

cats = Category.objects.all()


def users_dict(cats):
    users_list = {}
    for cat in cats:
        for users in cat.subscribes.all():
            print(cat.name, users.username)
