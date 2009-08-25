#!/usr/bin/python2.4
#
# Copyright 2009 Google Inc.
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

"""Rich Text Test Definitions."""

__author__ = 'elsigh@google.com (Lindsey Simon)'


from categories import test_set_base


_CATEGORY = 'richtext'


class RichtextTest(test_set_base.TestBase):
  TESTS_URL_PATH = '/%s/test' % _CATEGORY

  def __init__(self, key, name, doc, is_hidden_stat=True, category=None):
    """Initialze a test.

    Args:
      key: key for this in dict's
      name: a human readable label for display
      url_name: the name used in the url
      score_type: 'boolean' or 'custom'
      doc: a description of the test
      value_range: (min_value, max_value) as integer values
      is_hidden_stat: whether or not the test shown in the stats table
    """
    test_set_base.TestBase.__init__(
        self,
        key=key,
        name=name,
        url=self.TESTS_URL_PATH,
        score_type='boolean',
        doc=doc,
        min_value=0,
        max_value=1,
        is_hidden_stat=is_hidden_stat)

    # This way we can assign tests to a test group, i.e. apply, unapply, etc..
    if category:
      self.category = category

  def GetScoreAndDisplayValue(self, median, tests):
    """Returns a tuple with display text for the cell as well as a 1-100 value.
    """
    if score == None or score == '':
      return 0, ''

    display = score
    return score, display

_TESTS = (
  # key, name, doc
  RichtextTest('apply', 'Apply Formatting', '''About this test...''', False),
  RichtextTest('unapply', 'Un-Apply Formatting', '''About this test...''', False),
  RichtextTest('change', 'Change Existing Formatting', '''About this test...''', False),
  RichtextTest('query', 'Query State and Value', '''About this test...''', False),
  # Annie, put the rest of the individual tests here, like ...
  #RichtextTest('bold', 'Bolding', None, category='apply')
)


TEST_SET = test_set_base.TestSet(
    category=_CATEGORY,
    category_name='Rich Text',
    tests=_TESTS,
    subnav={
      'Test': '/%s/test' % _CATEGORY,
      'About': '/%s/about' % _CATEGORY
    },
    home_intro='These are the Rich Text tests...'
)
