from django.test import TestCase
from articles.models import Article
# from articles.forms import Article
from django.contrib.auth.models import User
from django.urls import reverse


class ArticlesDataTestCase(TestCase):
    def setUp(self):
        Article.get_app_config('haystack').signal_processor.teardown()

        self.user = User.objects.create_superuser(
            username='admin',
            email='admin@hellogithub.com',
            password='admin'
        )

        self.cate1 = Article.objects.create(name='Test category one')
        self.cate2 = Article.objects.create(name='Test category two')

        # label
        self.tag1 = Article.objects.create(tag='Test label one')
        self.tag2 = Article.objects.create(tag='Test label two')

        # article
        self.post1 = Article.objects.create(
            title='Test title one',
            body='Test content one',
            category=self.cate1,
            author=self.user,
        )
        self.post1.tags.add(self.tag1)
        self.post1.save()

        self.post2 = Article.objects.create(
            title='Test title two',
            body='Test content two',
            category=self.cate2,
            author=self.user,
            created_time=timezone.now() - timedelta(days=100)
        )


class ArticlesViewTestCase(ArticlesDataTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('articles', kwargs={'pk': self.cate1.pk})
        self.url2 = reverse('articles', kwargs={'pk': self.cate2.pk})

    def test_visit_a_nonexistent_category(self):
        url = reverse('articles', kwargs={'pk': 100})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_without_any_post(self):
        Article.objects.all().delete()
        response = self.client.get(self.url2)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('index.html')
        self.assertContains(response, 'No articles published yet!')

    def test_with_posts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('index.html')
        self.assertContains(response, self.post1.title)
        self.assertIn('post_list', response.context)
        self.assertIn('is_paginated', response.context)
        self.assertIn('page_obj', response.context)
        self.assertEqual(response.context['post_list'].count(), 1)
        expected_qs = self.cate1.post_set.all().order_by('-created_time')
        self.assertQuerysetEqual(response.context['post_list'], [repr(p) for p in expected_qs])

    def test_article_create_view(self):
        post = self.objects.create(author="user", title="Test", body="body")
        response = self.client.get(reverse('blog:post_detail', kwargs={'pk': post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test')
        self.assertContains(response, 'body')

    def test_article_update_view(self):
        post = self.objects.create(title='The Catcher in the Rye')
        response = self.client.post(
            reverse('update', kwargs={'pk': post.id}),
            {'title': 'title 2', 'author': 'author 2'})

        self.assertEqual(response.status_code, 302)

        post.refresh_from_db()
        self.assertEqual(post.author, 'author 2')

    def test_article_delete_view(self):
        response_get = self.client.get(reverse('article:delete', args=(self.id,)), follow=True)
        self.assertContains(response_get, 'delete')

        response_post = self.client.post(reverse('article:delete', args=(self.id,)), follow=True)
        self.assertRedirects(response_post, reverse('article:delete'), status_code=302)
