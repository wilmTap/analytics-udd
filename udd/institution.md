#institution
* [TENANT_ID](#tenant_id) [1] *
* [TENANT_NAME](#tenant_name) [0..1]

\* indicates that the property is the primary key for this entity.

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