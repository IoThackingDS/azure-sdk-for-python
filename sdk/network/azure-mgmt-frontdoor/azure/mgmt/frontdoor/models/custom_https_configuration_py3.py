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

from msrest.serialization import Model


class CustomHttpsConfiguration(Model):
    """Https settings for a domain.

    :param certificate_source: Defines the source of the SSL certificate.
     Possible values include: 'AzureKeyVault', 'FrontDoor'
    :type certificate_source: str or
     ~azure.mgmt.frontdoor.models.FrontDoorCertificateSource
    :param protocol_type: Defines the TLS extension protocol that is used for
     secure delivery. Possible values include: 'ServerNameIndication'
    :type protocol_type: str or
     ~azure.mgmt.frontdoor.models.FrontDoorTlsProtocolType
    :param vault: The Key Vault containing the SSL certificate
    :type vault:
     ~azure.mgmt.frontdoor.models.KeyVaultCertificateSourceParametersVault
    :param secret_name: The name of the Key Vault secret representing the full
     certificate PFX
    :type secret_name: str
    :param secret_version: The version of the Key Vault secret representing
     the full certificate PFX
    :type secret_version: str
    :param certificate_type: Defines the type of the certificate used for
     secure connections to a frontendEndpoint. Possible values include:
     'Dedicated'
    :type certificate_type: str or
     ~azure.mgmt.frontdoor.models.FrontDoorCertificateType
    """

    _attribute_map = {
        'certificate_source': {'key': 'certificateSource', 'type': 'str'},
        'protocol_type': {'key': 'protocolType', 'type': 'str'},
        'vault': {'key': 'keyVaultCertificateSourceParameters.vault', 'type': 'KeyVaultCertificateSourceParametersVault'},
        'secret_name': {'key': 'keyVaultCertificateSourceParameters.secretName', 'type': 'str'},
        'secret_version': {'key': 'keyVaultCertificateSourceParameters.secretVersion', 'type': 'str'},
        'certificate_type': {'key': 'frontDoorCertificateSourceParameters.certificateType', 'type': 'str'},
    }

    def __init__(self, *, certificate_source=None, protocol_type=None, vault=None, secret_name: str=None, secret_version: str=None, certificate_type=None, **kwargs) -> None:
        super(CustomHttpsConfiguration, self).__init__(**kwargs)
        self.certificate_source = certificate_source
        self.protocol_type = protocol_type
        self.vault = vault
        self.secret_name = secret_name
        self.secret_version = secret_version
        self.certificate_type = certificate_type