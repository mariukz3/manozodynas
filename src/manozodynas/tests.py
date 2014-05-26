# encoding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from manozodynas.testutils import StatefulTesting
from manozodynas.models import Word

class IndexTestCase(StatefulTesting):
    def test_index_page(self):
        self.open(reverse('index'))
        self.assertStatusCode(200)


class LoginTestCase(StatefulTesting):

    fixtures = ['test_fixture.json']

    def test_login_page(self):
        self.open(reverse('login'))
        self.assertStatusCode(200)

    def test_good_login(self):
        self.open(reverse('login'))
        self.selectForm('#login')
        self.submitForm({
            'username': 'test',
            'password': 'test',
        })
        self.assertStatusCode(302)

    def test_bad_login(self):
        self.open(reverse('login'))
        self.selectForm('#login')
        self.submitForm({
            'username': 'bad',
            'password': 'bad',
        })
        self.assertStatusCode(200)
        self.selectOne('.errorlist')

    def test_no_input(self):
        self.open(reverse('login'))
        self.selectForm('#login')
        self.submitForm({
            'username': '',
            'password': '',
        })
        self.assertStatusCode(200)
        self.selectMany('.errorlist')

    def test_no_username(self):
        self.open(reverse('login'))
        self.selectForm('#login')
        self.submitForm({
            'username': '',
            'password': 'test',
        })
        self.assertStatusCode(200)
        self.selectOne('.errorlist')

    def test_no_password(self):
        self.open(reverse('login'))
        self.selectForm('#login')
        self.submitForm({
            'username': 'test',
            'password': '',
        })
        self.assertStatusCode(200)
        self.selectOne('.errorlist')

class VerstiZodi(StatefulTesting):
    def test_index_page(self):
        self.open(reverse('word_type'))
        self.selectForm('#ivesti_zodi')
        self.submitForm({
            'zodis': 'pasibandyt5i'
        })
        self.assertStatusCode(302)
        self.assertTrue(Word.objects.filter(zodis='pasibandyt5i'))

        #self.open(reverse('words_list'))
        #self.selectTable('#zodziu_sarasas')
        #self.assertTableHasRows('pasibandyti')
