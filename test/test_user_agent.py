#!/usr/bin/python2.4
#
# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the 'License')
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""User Agent Unit Tests."""

__author__ = 'elsigh@google.com (Lindsey Simon)'

import logging
import unittest

from google.appengine.ext import db
from models.user_agent import *

class UserAgentTest(unittest.TestCase):

  def test_factory(self):
    """Creates two instances of a UserAgent with our factory function
    and test that they're in fact the same entity, ensuring uniqueness."""
    ua_string = ('Mozilla/5.0 (X11 U Linux armv6l de-DE rv:1.9a6pre) '
                 'Gecko/20080606 '
                 'Firefox/3.0a1 Tablet browser 0.3.7 '
                 'RX-34+RX-44+RX-48_DIABLO_4.2008.23-14')
    ua1 = UserAgent.factory(ua_string)
    self.assertNotEqual(ua1, None)

    ua2 = UserAgent.factory(ua_string)
    self.assertEqual(ua1.key(), ua2.key())

    query = db.Query(UserAgent)
    query.filter('string =', ua_string)
    results = query.fetch(2)
    self.assertEqual(1, len(results))


  def test_parse(self):
    ua_string = ('Mozilla/5.0 (X11 U Linux armv6l de-DE rv:1.9a6pre) '
                 'Gecko/20080606 '
                 'Firefox/3.0a1 Tablet browser 0.3.7 '
                 'RX-34+RX-44+RX-48_DIABLO_4.2008.23-14')
    self.assertEqual(('MicroB', '0', '3', '7'),
                     UserAgent.parse(ua_string))

    ua_string = ('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.6) '
                 'Gecko/2009011912 Firefox/3.0.6')
    self.assertEqual(('Firefox', '3', '0', '6'),
                     UserAgent.parse(ua_string))

    ua_string = ('Mozilla/5.0 (compatible; Konqueror/3.5; Linux; X11; de) '
                 'KHTML/3.5.2 (like Gecko) Kubuntu 6.06 Dapper')
    self.assertEqual(('Konqueror', '3', '5', None),
                     UserAgent.parse(ua_string))

    ua_string = 'Opera/10.00 (Windows NT 5.1; U; en) Presto/2.2.0'
    self.assertEqual(('Opera', '10', '00', None),
                     UserAgent.parse(ua_string))

    ua_string = ('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) '
                 'AppleWebKit/530.1 (KHTML, like Gecko) '
                 'Chrome/2.0.169.1 Safari/530.1')
    self.assertEqual(('Chrome', '2', '0', '169'),
                     UserAgent.parse(ua_string))

    ua_string = ('Mozilla/4.0 '
                 '(compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; '
                 '.NET CLR 2.0.50727; .NET CLR 1.1.4322; '
                 '.NET CLR 3.0.04506.648; .NET CLR 3.5.21022)')
    self.assertEqual(('IE', '8', '0', None),
                     UserAgent.parse(ua_string))

    # New opera UA string
    ua_string = ('Opera/9.80 (Macintosh; Intel Mac OS X; U; en) '
                  'Presto/2.2.15 Version/10.00')
    self.assertEqual(('Opera', '10', '00', None),
                     UserAgent.parse(ua_string))


    ua_string = 'SomethingWeNeverKnewExisted'
    self.assertEqual(('Other', None, None, None), UserAgent.parse(ua_string))


  def test_get_string_list(self):
    ua_string = ('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.6) '
                 'Gecko/2009011912 Firefox/3.0.6')
    ua = UserAgent.factory(ua_string)
    self.assertEqual(['Firefox', 'Firefox 3', 'Firefox 3.0', 'Firefox 3.0.6'],
                     ua.get_string_list())

    ua_string = ('Mozilla/4.0 '
                 '(compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; '
                 '.NET CLR 2.0.50727; .NET CLR 1.1.4322; '
                 '.NET CLR 3.0.04506.648; .NET CLR 3.5.21022)')
    ua = UserAgent.factory(ua_string)
    self.assertEqual(['IE', 'IE 8', 'IE 8.0'],
                     ua.get_string_list())

    ua_string = ('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) '
                 'AppleWebKit/530.1 (KHTML, like Gecko) '
                 'Chrome/2.0.169.1 Safari/530.1')
    ua = UserAgent.factory(ua_string)
    self.assertEqual(['Chrome', 'Chrome 2', 'Chrome 2.0', 'Chrome 2.0.169'],
                     ua.get_string_list())


  def test_pretty_print(self):
    self.assertEqual('MicroB 3',
                     UserAgent.pretty_print('MicroB', '3', None, None))

    self.assertEqual('Firefox 3.0.6',
                     UserAgent.pretty_print('Firefox', '3', '0', '6'))

    self.assertEqual('Other',
                     UserAgent.pretty_print('Other', None, None, None))


class UserAgentGroupTest(unittest.TestCase):

  def setUp(self):

    # purge memcache
    for version_level, label in BROWSER_NAV:
      memcache_key = UserAgentGroup.MakeMemcacheKey(version_level)
      memcache.delete(key=memcache_key, seconds=0)

    user_agent_strings = [
        ('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.6) '
        'Gecko/2009011912 Firefox/3.0.7'),
        ('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.6) '
         'Gecko/2009011912 Firefox/3.1.8'),
        ('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.6) '
         'Gecko/2009011912 Firefox/3.1.8'),
        ('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.6) '
         'Gecko/2009011912 Firefox/3.1.7'),
        ('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; '
         '.NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.04506.648;'
         '.NET CLR 3.5.21022)'),
        ]
    for user_agent_string in user_agent_strings:
      user_agent = UserAgent.factory(user_agent_string)
      user_agent.update_groups()

  def test_update_groups_version_level_zero(self):
    self.assertEqual(
        ['Firefox', 'IE'],
        UserAgentGroup.GetByVersionLevel('0'))

  def test_update_groups_version_level_one(self):
    self.assertEqual(
        ['Firefox 3', 'IE 7'],
        UserAgentGroup.GetByVersionLevel('1'))

  def test_update_groups_version_level_two(self):
    self.assertEqual(
        ['Firefox 3.0', 'Firefox 3.1', 'IE 7.0'],
        UserAgentGroup.GetByVersionLevel('2'))

  def test_update_groups_version_level_three(self):
    # This also tests that the order comes out the way we'd want even though
    # they didn't go in in that order.
    self.assertEqual(
        ['Firefox 3.0.7', 'Firefox 3.1.7', 'Firefox 3.1.8', 'IE 7.0'],
        UserAgentGroup.GetByVersionLevel('3'))


if __name__ == '__main__':
  unittest.main()