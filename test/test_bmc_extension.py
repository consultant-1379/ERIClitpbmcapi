##############################################################################
# COPYRIGHT Ericsson AB 2013
#
# The copyright to the computer program(s) herein is the property of
# Ericsson AB. The programs may be used and/or copied only with written
# permission from Ericsson AB. or in accordance with the terms and
# conditions stipulated in the agreement/contract under which the
# program(s) have been supplied.
##############################################################################

import unittest

from litp.core.plugin_manager import PluginManager
from litp.core.model_manager import ModelManager
from litp.core.plugin_context_api import PluginApiContext
from litp.extensions.core_extension import CoreExtension

from litp.core.execution_manager import ExecutionManager
from litp.core.puppet_manager import PuppetManager
from litp.core.model_type import Property

from bmc_extension.bmc_extension import BmcExtension


class TestBmcExtension(unittest.TestCase):

    def setUp(self):
        self.api = BmcExtension()

    def tearDown(self):
        pass

    def test_item_types_registered(self):
        itemtype = self.api.define_item_types()[0]
        self.assertEqual('bmc', itemtype.item_type_id)

        self.assertTrue(isinstance(itemtype.structure['ipaddress'], Property))
        self.assertTrue(isinstance(itemtype.structure['username'], Property))
        self.assertTrue(isinstance(itemtype.structure['password_key'], Property))
        self.assertEqual(False, itemtype.structure['password_key'].updatable_rest)
        self.assertEqual(True, itemtype.structure['username'].updatable_rest)

        self.assertRaises(KeyError, lambda:itemtype.structure['bogus'])

if __name__ == '__main__':
    unittest.main()
