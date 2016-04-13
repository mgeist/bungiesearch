from bungiesearch import Bungiesearch
from django.conf import settings
from django.core.management import call_command
from django.test import TestCase


class SettingsTestCase(TestCase):

    def tearDown(self):
        call_command('search_index', action='delete', confirmed='guilty-as-charged')

    def test_timeout_used(self):
        settings.BUNGIESEARCH['TIMEOUT'] = 29
        search = Bungiesearch()

        self.assertEqual(search.BUNGIE['TIMEOUT'], 29)
        self.assertEqual(search._using.transport.kwargs['timeout'], 29)

    def test_index_settings(self):
        search = Bungiesearch()
        config = settings.BUNGIESEARCH['INDICES']['bungiesearch_demo']['settings']

        call_command('search_index', action='delete', confirmed='guilty-as-charged')
        config['number_of_shards'] = 1
        config['number_of_replicas'] = 0
        call_command('search_index', action='create')

        index_settings = search._using.indices.get('bungiesearch_demo')['bungiesearch_demo']['settings']['index']
        self.assertEqual(index_settings['number_of_shards'], '1')
        self.assertEqual(index_settings['number_of_replicas'], '0')

        call_command('search_index', action='delete', confirmed='guilty-as-charged')
        config['number_of_shards'] = 2
        config['number_of_replicas'] = 0
        call_command('search_index', action='create')

        index_settings = search._using.indices.get('bungiesearch_demo')['bungiesearch_demo']['settings']['index']
        self.assertEqual(index_settings['number_of_shards'], '2')
        self.assertEqual(index_settings['number_of_replicas'], '0')
