from django.conf.urls import patterns, url
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import index_view, login_view, words_view, TypeTranslation, TypeWord

urlpatterns = patterns('',
    url(r'^$', index_view, name='index'),
    url(r'^login$', login_view, name='login'),
    url(r'^list_words/$', words_view, name='words_list'),
    url(r'^type_word/$', TypeWord.as_view(), name='word_type'),
    url(r'^type_translation/(?P<pk>\d*)/$', TypeTranslation.as_view(), name='translations_type')
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)
