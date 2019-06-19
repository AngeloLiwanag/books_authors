from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_book$', views.add_books),
    url(r'^books/(?P<book_id>\d+)$', views.go_to_books),
    url(r'^insert_author$', views.insert_author),
    url(r'^go_to_author$', views.author_page),
    url(r'^add_author$', views.add_authors),
    url(r'^authors/(?P<author_id>\d+)$', views.go_to_authors),
    url(r'^insert_book$', views.insert_book),
]