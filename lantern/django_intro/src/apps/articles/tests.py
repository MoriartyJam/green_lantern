# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from django.test import TestCase
# from src.apps.articles.models import Article
# # from articles.forms import Article
# from django.contrib.auth.models import User
# from django.urls import reverse
#
#
# class ArticlesDataTestCase(TestCase):
#     def setUp(self):
#         Article.get_app_config('haystack').signal_processor.teardown()
#
#         self.user = User.objects.create_superuser(
#             username='admin',
#             email='admin@hellogithub.com',
#             password='admin'
#         )
#
#         self.cate1 = Article.objects.create(name='Test category one')
#         self.cate2 = Article.objects.create(name='Test category two')
#
#         # label
#         self.tag1 = Article.objects.create(tag='Test label one')
#         self.tag2 = Article.objects.create(tag='Test label two')
#
#         # article
#         self.post1 = Article.objects.create(
#             title='Test title one',
#             body='Test content one',
#             category=self.cate1,
#             author=self.user,
#         )
#         self.post1.tags.add(self.tag1)
#         self.post1.save()
#
#         self.post2 = Article.objects.create(
#             title='Test title two',
#             body='Test content two',
#             category=self.cate2,
#             author=self.user,
#             created_time=timezone.now() - timedelta(days=100)
#         )
#
#
# class ArticlesViewTestCase(ArticlesDataTestCase):
#     def setUp(self):
#         super().setUp()
#         self.url = reverse('articles', kwargs={'pk': self.cate1.pk})
#         self.url2 = reverse('articles', kwargs={'pk': self.cate2.pk})
#
#     def test_visit_a_nonexistent_category(self):
#         url = reverse('articles', kwargs={'pk': 100})
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 404)
#
#     def test_without_any_post(self):
#         Article.objects.all().delete()
#         response = self.client.get(self.url2)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed('index.html')
#         self.assertContains(response, 'No articles published yet!')
#
#     def test_with_posts(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed('index.html')
#         self.assertContains(response, self.post1.title)
#         self.assertIn('post_list', response.context)
#         self.assertIn('is_paginated', response.context)
#         self.assertIn('page_obj', response.context)
#         self.assertEqual(response.context['post_list'].count(), 1)
#         expected_qs = self.cate1.post_set.all().order_by('-created_time')
#         self.assertQuerysetEqual(response.context['post_list'], [repr(p) for p in expected_qs])
