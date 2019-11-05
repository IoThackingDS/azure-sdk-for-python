# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_only_resource import ProxyOnlyResource


class FunctionEnvelope(ProxyOnlyResource):
    """Web Job Information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param function_app_id: Function App ID.
    :type function_app_id: str
    :param script_root_path_href: Script root path URI.
    :type script_root_path_href: str
    :param script_href: Script URI.
    :type script_href: str
    :param config_href: Config URI.
    :type config_href: str
    :param secrets_file_href: Secrets file URI.
    :type secrets_file_href: str
    :param href: Function URI.
    :type href: str
    :param config: Config information.
    :type config: object
    :param files: File list.
    :type files: dict[str, str]
    :param test_data: Test data used when testing via the Azure Portal.
    :type test_data: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'function_app_id': {'key': 'properties.function_app_id', 'type': 'str'},
        'script_root_path_href': {'key': 'properties.script_root_path_href', 'type': 'str'},
        'script_href': {'key': 'properties.script_href', 'type': 'str'},
        'config_href': {'key': 'properties.config_href', 'type': 'str'},
        'secrets_file_href': {'key': 'properties.secrets_file_href', 'type': 'str'},
        'href': {'key': 'properties.href', 'type': 'str'},
        'config': {'key': 'properties.config', 'type': 'object'},
        'files': {'key': 'properties.files', 'type': '{str}'},
        'test_data': {'key': 'properties.test_data', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(FunctionEnvelope, self).__init__(**kwargs)
        self.function_app_id = kwargs.get('function_app_id', None)
        self.script_root_path_href = kwargs.get('script_root_path_href', None)
        self.script_href = kwargs.get('script_href', None)
        self.config_href = kwargs.get('config_href', None)
        self.secrets_file_href = kwargs.get('secrets_file_href', None)
        self.href = kwargs.get('href', None)
        self.config = kwargs.get('config', None)
        self.files = kwargs.get('files', None)
        self.test_data = kwargs.get('test_data', None)