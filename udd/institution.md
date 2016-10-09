#Institution
* [TENANT_ID](#tenant_id) [1]
* [TENANT_NAME](#tenant_name) [0..1]

Primary key: ('TENANT_ID')

For more information about which properties are required for particular purposes or under particular conditions, please consult the [guide to mandatory properties in the UDD](../mandatory.md).

##TENANT_ID
###Description
This field records the unique identifier for the University College concerned - using the UK Provider Reference Number (UKRPN) which is the unique identifier allocated to institutions by the UK Register of Learning Providers (UKRLP).

###Purpose
To identify the organisation.

###Derivation
UK Register of Learning Providers (UKRLP).

###References

###Format
String (8)

###Notes
Further information (on UKPRN) available at www.ukrlp.co.uk


##TENANT_NAME
###Description
Institution's official legal name. This should match the name indicated in the UKRLP database, as used for TENANT_ID

###Purpose
To identify the organisation.

###Derivation
Insitution

###References

###Format
String (255)

###Notes
Omitting this property could impair the functionality of analytics applications such as student apps or dashboards.