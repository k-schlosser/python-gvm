# -*- coding: utf-8 -*-
# Copyright (C) 2019 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from enum import Enum

from typing import Optional

from gvm.errors import InvalidArgument

from gvm.protocols.gmpv8.types import (
    AlertCondition,
    AlertEvent,
    AlertMethod,
    AliveTest,
    AssetType,
    CredentialFormat,
    CredentialType,
    EntityType,
    FeedType,
    FilterType,
    HostsOrdering,
    InfoType,
    PermissionSubjectType,
    PortRangeType,
    ScannerType,
    SeverityLevel,
    SnmpAuthAlgorithm,
    SnmpPrivacyAlgorithm,
    TicketStatus,
    TimeUnit,
    get_alert_condition_from_string,
    get_alert_event_from_string,
    get_alert_method_from_string,
    get_alive_test_from_string,
    get_asset_type_from_string,
    get_credential_format_from_string,
    get_credential_type_from_string,
    get_entity_type_from_string,
    get_feed_type_from_string,
    get_filter_type_from_string,
    get_hosts_ordering_from_string,
    get_info_type_from_string,
    get_permission_subject_type_from_string,
    get_port_range_type_from_string,
    get_severity_level_from_string,
    get_scanner_type_from_string,
    get_snmp_auth_algorithm_from_string,
    get_snmp_privacy_algorithm_from_string,
    get_ticket_status_from_string,
)


__all__ = [
    "AlertCondition",
    "AlertEvent",
    "AlertMethod",
    "AliveTest",
    "AssetType",
    "CredentialFormat",
    "CredentialType",
    "EntityType",
    "FeedType",
    "FilterType",
    "HostsOrdering",
    "InfoType",
    "PermissionSubjectType",
    "PortRangeType",
    "ScannerType",
    "SeverityLevel",
    "SnmpAuthAlgorithm",
    "SnmpPrivacyAlgorithm",
    "TicketStatus",
    "TimeUnit",
    "get_alert_condition_from_string",
    "get_alert_event_from_string",
    "get_alert_method_from_string",
    "get_alive_test_from_string",
    "get_asset_type_from_string",
    "get_credential_format_from_string",
    "get_credential_type_from_string",
    "get_entity_type_from_string",
    "get_feed_type_from_string",
    "get_filter_type_from_string",
    "get_hosts_ordering_from_string",
    "get_info_type_from_string",
    "get_permission_subject_type_from_string",
    "get_port_range_type_from_string",
    "get_scanner_type_from_string",
    "get_severity_level_from_string",
    "get_snmp_auth_algorithm_from_string",
    "get_snmp_privacy_algorithm_from_string",
    "get_ticket_status_from_string",
]


class _UsageType(Enum):
    """ Enum for usage types """

    AUDIT = "audit"
    POLICY = "policy"
    SCAN = "scan"


def __get_usage_type_from_string(
    usage_type: Optional[str]
) -> Optional[_UsageType]:
    """ Convert a usage type string to an actual _UsageType instance

    Arguments:
        entity_type: Usage type string to convert to a _UsageType
    """
    if not usage_type:
        return None

    if usage_type == 'audit':
        return _UsageType.AUDIT

    if usage_type == 'policy':
        return _UsageType.POLICY

    if usage_type == 'scan':
        return _UsageType.SCAN

    try:
        return _UsageType[usage_type.upper()]
    except KeyError:
        raise InvalidArgument(
            argument='usage_type',
            function=__get_usage_type_from_string.__name__,
        )
