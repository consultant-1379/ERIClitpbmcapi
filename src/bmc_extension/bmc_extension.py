#!/usr/bin/env python

##############################################################################
# COPYRIGHT Ericsson AB 2013
#
# The copyright to the computer program(s) herein is the property of
# Ericsson AB. The programs may be used and/or copied only with written
# permission from Ericsson AB. or in accordance with the terms and
# conditions stipulated in the agreement/contract under which the
# program(s) have been supplied.
##############################################################################

from litp.core.extension import ModelExtension
from litp.core.model_type import ItemType, Property


class BmcExtension(ModelExtension):
    """
    BMC (Baseboard Management Controller) manages the interface \
    between System management software and platform hardware.

    This model extension allows for definition of item types \
    for BMC credentials.
    """

    def define_item_types(self):

        '''
        Create a BMC under a Blade "system" to manage the iLO
        .. code-block:: bash
            litp create \
            -t blade \
            -p /infrastructure/systems/blade1 \
            -o system_name=abcd1234
            litp create \
            -t bmc \
            -p /infrastructure/systems/blade1/bmc \
            -o ipaddress=1.2.3.4 username=root password_key=key-for-root
        '''

        ip_prop = Property('ipv4_address',
                           prop_description='IP V4 Address.',
                           site_specific=True,
                           updatable_rest=False,
                           required=True)
        user_prop = Property('any_string',
                             prop_description='Username.',
                             updatable_rest=True,
                             required=True)
        pwd_key_prop = Property('basic_string',
                                prop_description='Password Key.',
                                updatable_rest=False,
                                required=True)

        bmc_itemtype = ItemType('bmc',
                                item_description='This item type represents'
                                                 ' a BMC (Baseboard Management'
                                                 ' Controller), where a BMC'
                                                 ' manages the interface'
                                                 ' between system management'
                                                 ' software and platform '
                                                 ' hardware.',
                                extend_item='bmc-base',
                                ipaddress=ip_prop,
                                username=user_prop,
                                password_key=pwd_key_prop)

        return [bmc_itemtype]
