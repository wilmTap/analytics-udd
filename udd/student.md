#Student
* [STUDENT_ID](#student_id) [1]
* [ULN](#uln) [0..1]
* [DOB](#dob) [0..1]
* [ETHNICITY](#ethnicity) [0..1]
* [SEXID](#sexid) [0..1]
* [AGE](#age) [0..1]
* [LEARN_DIF](#learn_dif) [0..1]
* [DISABILITY1](#disability1) [0..1]
* [DISABILITY2](#disability2) [0..1]
* [DOMICILE](#domicile) [0..1]
* [TERMTIME_ACCOM](#termtime_accom) [0..1]
* [PARENTS_ED](#parents_ed) [0..1]
* [SOCIO_EC](#socio_ec) [0..1]
* [OVERSEAS](#overseas) [0..1]
* [APPSHIB_ID](#appshib_id) [0..1]
* [VLE_ID](#vle_id) [0..*]
* [HUSID](#husid) [0..1]
* [USERNAME](#username) [0..1]
* [LAST_NAME](#last_name) [0..1]
* [FIRST_NAME](#first_name) [0..1]
* [ADDRESS_LINE_1](#address_line_1) [0..1]
* [ADDRESS_LINE_2](#address_line_2) [0..1]
* [ADDRESS_LINE_3](#address_line_3) [0..1]
* [ADDRESS_LINE_4](#address_line_4) [0..1]
* [POSTCODE](#postcode) [0..1]
* [PRIMARY_EMAIL_ADDRESS](#primary_email_address) [0..1]
* [HOME_PHONE](#home_phone) [0..1]
* [MOBILE_PHONE](#mobile_phone) [0..1]
* [PHOTO_URL](#photo_url) [0..1]
* [TUTOR_STAFF_ID](#tutor_staff_id) [0..1]
* [ENTRY_POSTCODE](#entry_postcode) [0..1]

##STUDENT_ID
###Description
The institution's own unique identifier of the student. In the case or event of requiring to provide anonymous data for trial/ evaluation purposes with JISC, institutions should use a suitable method or algorithm (which can be reversed by that institution, for evaluation purposes thereafter) to ensure that this studentid provided is different to that actual ID held locally.

###Purpose
To identify the student across multiple records within an institution

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/OWNSTU

###References

###Format
String 255

###Notes


##ULN
###Description
Unique Learner Number. For initial trial and data model development for the predictive model, this field should be left out.

###Purpose
For future use, tracking student journey.

###Derivation
Skills Funding Agency: See https://www.gov.uk/government/publications/lrs-unique-learner-numbers

###References

###Format
String (10)

###Notes
The ULN can be provided as an additional point of reference, however the STUDENT_ID will always take precedence as the unique learner/ student identifier


##DOB
###Description
Student's date of birth

###Purpose
For analytics comparisons.

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/BIRTHDTE

###References

###Format
ISO8601 format of YYYY-MM-DD

###Notes
A date of birth of 2099-12-31 can be provided on a temporary basis.
Omitting this property may hinder the development or use of an effective analytics model.

##ETHNICITY
###Description
This field records the ethnicity of the student, on the basis of their own self-assessment

###Purpose
To allow equal opportunities monitoring, within detailed learning analytics/ data modelling.

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/ETHNIC

###Format
String (10)

###Valid Values & Mappings:  

<table>
<tr><td>ETHNICITY</td><td>DESCRIPTION(ENGLISH)</td><td>DESCRIPTION(WELSH)</td><td>HESA(ETHNIC)</td><td>FEILR(ETHNICITY)</td></tr>
<tr><td>10</td><td>White</td><td>Gwyn</td><td>10</td><td>31</td></tr>
<tr><td>13</td><td>White - Scottish</td><td>Gwyn - Alban</td><td>13</td><td>N/A</td></tr>
<tr><td>51</td><td>Irish</td><td>Gwyddel</td><td>N/A</td><td>32</td></tr>
<tr><td>14</td><td>Irish Traveller</td><td></td><td>14</td><td>N/A</td></tr>
<tr><td>15</td><td>Gypsy or Traveller</td><td></td><td>15</td><td>33</td></tr>
<tr><td>19</td><td>Other White background</td><td>Gwyn Arall</td><td>19</td><td>34</td></tr>
<tr><td>21</td><td>Black or Black British - Caribbean</td><td></td><td>21</td><td>45</td></tr>
<tr><td>22</td><td>Black or Black British - African</td><td></td><td>22</td><td>44</td></tr>
<tr><td>29</td><td>Other Black background</td><td></td><td>29</td><td>46</td></tr>
<tr><td>31</td><td>Asian or Asian British - Indian</td><td></td><td>31</td><td>39</td></tr>
<tr><td>32</td><td>Asian or Asian British - Pakistani</td><td></td><td>32</td><td>40</td></tr>
<tr><td>33</td><td>Asian or Asian British - Bangladeshi</td><td></td><td>33</td><td>41</td></tr>
<tr><td>34</td><td>Chinese</td><td></td><td>34</td><td>42</td></tr>
<tr><td>39</td><td>Other Asian background</td><td></td><td>39</td><td>43</td></tr>
<tr><td>41</td><td>Mixed - White and Black Caribbean</td><td></td><td>41</td><td>35</td></tr>
<tr><td>42</td><td>Mixed - White and Black African</td><td></td><td>42</td><td>36</td></tr>
<tr><td>43</td><td>Mixed - White and Asian</td><td></td><td>43</td><td>37</td></tr>
<tr><td>49</td><td>Other mixed background</td><td></td><td>49</td><td>38</td></tr>
<tr><td>50</td><td>Arab</td><td></td><td>50</td><td>47</td></tr>
<tr><td>80</td><td>Other ethnic background</td><td>Cefndir Ethnig Arall</td><td>80</td><td>98</td></tr>
<tr><td>90</td><td>Not known</td><td>Anhysbys</td><td>90</td><td>N/A</td></tr>
<tr><td>98</td><td>Information refused</td><td></td><td>98</td><td>99</td></tr>
</table>

Please Note - N/A denotes that no mapping value is applicable (and should not be confused with NULL)  

###Notes
Where any ethnicity details are unknown, this field must be coded with '90'
Omitting this property may hinder the development or use of an effective analytics model.

##SEXID
###Description
To record a Learner's current sex, on the basis of their own self-assessment

###Purpose
For equal opportunities monitoring within learning analytics / data modelling

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/SEXID

###Format
Int

###Valid Values & Mappings

<table>
<tr><td>SEXID</td><td>DESCRIPTION(ENGLISH)</td><td>DESCRIPTION(WELSH)</td><td>HESA(SEXID)</td><td>FEILR(SEX)</td></tr>
<tr><td>1</td><td>Male</td><td>Gwryw</td><td>1</td><td>M  </td></tr>
<tr><td>2</td><td>Female</td><td>Beny</td><td>2</td><td>F  </td></tr>
<tr><td>3</td><td>Other</td><td>Arall</td><td>3</td><td>N/A  </td></tr>
<tr><td>4</td><td>Unknown</td><td>Anhysbys</td><td>N/A</td><td>N/A</td></tr>
</table>

Please Note - N/A denotes that no mapping value is applicable (and should not be confused with NULL)   

###Notes
If the sex is unknown, return code '4' in all cases
Omitting this property may hinder the development or use of an effective analytics model.

##AGE
###Description
The current age of the learner/ student

###Purpose
To be used purely for display purposes within the Learning Analytics software suite

###Format
Int

###Notes
This will typically auto-calculated on a daily basis, based on field DOB. The LA system will provide this field.
Omitting this property may hinder the development or use of an effective analytics model.

##LEARN_DIF
###Description
This field records whether the learner considers themselves to have a learning difficulty

###Purpose
For detailed analysis or intervention purposes within Learning Analytics eg. Data Insight Tool

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/LLDDHEALTHPROB

###Valid Values & Mappings

<table>
<tr><td>LEARN_DIF</td><td>DESCRIPTION(ENGLISH)</td><td>DESCRIPTION(WELSH)</td><td>HESA(LEARNDIF)</td><td>FEILR(LLDDCAT)  </td></tr>
<tr><td>1</td><td>Moderate learning difficulty</td><td></td><td>1</td><td>10  </td></tr>
<tr><td>2</td><td>Severe learning difficulty</td><td></td><td>2</td><td>11  </td></tr>
<tr><td>10</td><td>Dyslexia</td><td></td><td>10</td><td>12  </td></tr>
<tr><td>11</td><td>Dyscalculia</td><td></td><td>11</td><td>13  </td></tr>
<tr><td>19</td><td>Other specific learning difficulty</td><td></td><td>19</td><td>94  </td></tr>
<tr><td>20</td><td>Autism spectrum disorder</td><td></td><td>20</td><td>14  </td></tr>
<tr><td>90</td><td>Multiple learning difficulties</td><td></td><td>90</td><td>3  </td></tr>
<tr><td>97</td><td>Other</td><td></td><td>97</td><td>96  </td></tr>
<tr><td>98</td><td>No learning difficulty</td><td></td><td>98</td><td>N/A  </td></tr>
<tr><td>99</td><td>Not known / information not provided</td><td></td><td>99</td><td>N/A  </td></tr>
</table>

Please Note - N/A denotes that no mapping value is applicable (and should not be confused with NULL)  

###Format
Int

###Notes
If a learner's learning difficulty is unknown, then code '99' should be used for those cases
Omitting this property may hinder the development or use of an effective analytics model.

##DISABILITY1
###Description
Whether the student is indicated as being disabled, according to their own self-assessment. This will be their primary disability.

###Purpose
For equal opportunities monitoring within Learning Analytics/ Data Modelling

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/DISABLE

###Valid Values & Mappings

<table>
<tr>
<td>DISABILITY1</td>
<td>DESCRIPTION(ENGLISH)</td>
<td>DESCRIPTION(WELSH)</td>
<td>HESA(DISABLE)</td>
<td>FEILR(LLDDCat) </td>
</tr>
<tr>
<td>0</td>
<td>No known disability</td>
<td>Dim Anabledd</td>
<td>0</td>
<td>N/A </td>
</tr>
<tr>
<td>5</td>
<td>Personal care support</td>
<td></td>
<td>5</td>
<td>N/A </td>
</tr>
<tr>
<td>7</td>
<td>An unseen disability, e.g. diabetes, epilepsy, asthma</td>
<td></td>
<td>7</td>
<td>N/A </td>
</tr>
<tr>
<td>8</td>
<td>Two or more impairments and/or disabling medical conditions</td>
<td></td>
<td>8</td>
<td>2 </td>
</tr>
<tr>
<td>51</td>
<td>A specific learning difficulty such as dyslexia dyspraxia or AD(H)D</td>
<td></td>
<td>11</td>
<td>12 </td>
</tr>
<tr>
<td>53</td>
<td>A social/communication impairment such as Asperger's syndrome/other autistic
spectrum disorder</td>
<td></td>
<td>53</td>
<td>15, 1</td>
</tr>
<tr>
<td>54</td>
<td>A long standing illness or health condition such as cancer HIV diabetes chronic
heart disease or epilepsy</td>
<td></td>
<td>54</td>
<td>95 </td>
</tr>
<tr>
<td>55</td>
<td>A mental health condition such as depression schizophrenia or anxiety
disorder</td>
<td></td>
<td>6, 55</td>
<td>9 </td>
</tr>
<tr>
<td>56</td>
<td>A physical impairment or mobility issues such as difficulty using arms or using
a wheelchair or crutches</td>
<td></td>
<td>4, 56</td>
<td>6, 93</td>
</tr>
<tr>
<td>57</td>
<td>Deaf or a serious hearing impairment</td>
<td></td>
<td>3, 57</td>
<td>5 </td>
</tr>
<tr>
<td>58</td>
<td>Blind or a serious visual impairment uncorrected by glasses</td>
<td></td>
<td>2, 58</td>
<td>4 </td>
</tr>
<tr>
<td>96</td>
<td>A disability impairment or medical condition that is not listed above</td>
<td></td>
<td>96</td>
<td>7, 8, 16, 97</td>
</tr>
<tr>
<td>97</td>
<td>Information refused</td>
<td></td>
<td>97</td>
<td>98 </td>
</tr>
<tr>
<td>98</td>
<td>Information not sought</td>
<td></td>
<td>98</td>
<td>N/A </td>
</tr>
<tr>
<td>99</td>
<td>Not known</td>
<td>Anhysbys</td>
<td>99</td>
<td>99 </td>
</tr>
</table>  

Please Note - N/A denotes that no mapping value is applicable (and should not be confused with NULL)  

###Format
Int

###Notes
If disability is unknown, code '0' or '99' should be provided
Omitting this property may hinder the development or use of an effective analytics model.

##DISABILITY2
###Description
Whether the student is indicated as being disabled, according to their own self-assessment. This will be their secondary disability.

###Purpose
For equal opportunities monitoring within Learning Analytics/ Data Modelling

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/DISABLE

###Valid Values & Mappings

<table>
<tr>
<td>DISABILITY2</td>
<td>DESCRIPTION(ENGLISH)</td>
<td>DESCRIPTION(WELSH)</td>
<td>HESA(DISABLE)</td>
<td>FEILR(LLDDCat) </td>
</tr>
<tr>
<td>0</td>
<td>No known disability</td>
<td>Dim Anabledd</td>
<td>0</td>
<td>N/A </td>
</tr>
<tr>
<td>5</td>
<td>Personal care support</td>
<td></td>
<td>5</td>
<td>N/A </td>
</tr>
<tr>
<td>7</td>
<td>An unseen disability, e.g. diabetes, epilepsy, asthma</td>
<td></td>
<td>7</td>
<td>N/A </td>
</tr>
<tr>
<td>8</td>
<td>Two or more impairments and/or disabling medical conditions</td>
<td></td>
<td>8</td>
<td>2 </td>
</tr>
<tr>
<td>51</td>
<td>A specific learning difficulty such as dyslexia dyspraxia or AD(H)D</td>
<td></td>
<td>11</td>
<td>12 </td>
</tr>
<tr>
<td>53</td>
<td>A social/communication impairment such as Asperger's syndrome/other autistic
spectrum disorder</td>
<td></td>
<td>53</td>
<td>15, 1</td>
</tr>
<tr>
<td>54</td>
<td>A long standing illness or health condition such as cancer HIV diabetes chronic
heart disease or epilepsy</td>
<td></td>
<td>54</td>
<td>95 </td>
</tr>
<tr>
<td>55</td>
<td>A mental health condition such as depression schizophrenia or anxiety
disorder</td>
<td></td>
<td>6, 55</td>
<td>9 </td>
</tr>
<tr>
<td>56</td>
<td>A physical impairment or mobility issues such as difficulty using arms or using
a wheelchair or crutches</td>
<td></td>
<td>4, 56</td>
<td>6, 93</td>
</tr>
<tr>
<td>57</td>
<td>Deaf or a serious hearing impairment</td>
<td></td>
<td>3, 57</td>
<td>5 </td>
</tr>
<tr>
<td>58</td>
<td>Blind or a serious visual impairment uncorrected by glasses</td>
<td></td>
<td>2, 58</td>
<td>4 </td>
</tr>
<tr>
<td>96</td>
<td>A disability impairment or medical condition that is not listed above</td>
<td></td>
<td>96</td>
<td>7, 8, 16, 97</td>
</tr>
<tr>
<td>97</td>
<td>Information refused</td>
<td></td>
<td>97</td>
<td>98 </td>
</tr>
<tr>
<td>98</td>
<td>Information not sought</td>
<td></td>
<td>98</td>
<td>N/A </td>
</tr>
<tr>
<td>99</td>
<td>Not known</td>
<td>Anhysbys</td>
<td>99</td>
<td>99 </td>
</tr>
</table>  

Please Note - N/A denotes that no mapping value is applicable (and should not be confused with NULL)  

###Format
Int

###Notes
If disability is unknown, code '0' or '99' should be provided
Omitting this property may hinder the development or use of an effective analytics model.

##DOMICILE
###Description
This field holds the country code of the student's permanent home address prior to entry to the course. It is not necessarily the correspondence address of the student.

###Purpose
For detailed analysis within Learning Analytics/ Data Modelling

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/DOMICILE

###Format
String (2)

###Valid Values (No Mappings)
<table>
	<tr>
		<td>Code</td>
		<td>Label</td>
	</tr>
	<tr>
		<td>AF</td>
		<td>Afghanistan</td>
	</tr>
	<tr>
		<td>XQ</td>
		<td>Africa not otherwise specified</td>
	</tr>
	<tr>
		<td>AX</td>
		<td>Åland Islands {Ahvenamaa}</td>
	</tr>
	<tr>
		<td>AL</td>
		<td>Albania</td>
	</tr>
	<tr>
		<td>DZ</td>
		<td>Algeria</td>
	</tr>
	<tr>
		<td>AS</td>
		<td>American Samoa</td>
	</tr>
	<tr>
		<td>AD</td>
		<td>Andorra</td>
	</tr>
	<tr>
		<td>AO</td>
		<td>Angola</td>
	</tr>
	<tr>
		<td>AI</td>
		<td>Anguilla</td>
	</tr>
	<tr>
		<td>XX</td>
		<td>Antarctica and Oceania not otherwise specified</td>
	</tr>
	<tr>
		<td>AG</td>
		<td>Antigua and Barbuda</td>
	</tr>
	<tr>
		<td>AR</td>
		<td>Argentina</td>
	</tr>
	<tr>
		<td>AM</td>
		<td>Armenia</td>
	</tr>
	<tr>
		<td>AW</td>
		<td>Aruba</td>
	</tr>
	<tr>
		<td>XS</td>
		<td>Asia (Except Middle East) not otherwise specified</td>
	</tr>
	<tr>
		<td>AU</td>
		<td>Australia</td>
	</tr>
	<tr>
		<td>AT</td>
		<td>Austria</td>
	</tr>
	<tr>
		<td>AZ</td>
		<td>Azerbaijan</td>
	</tr>
	<tr>
		<td>BS</td>
		<td>Bahamas, The</td>
	</tr>
	<tr>
		<td>BH</td>
		<td>Bahrain</td>
	</tr>
	<tr>
		<td>BD</td>
		<td>Bangladesh</td>
	</tr>
	<tr>
		<td>BB</td>
		<td>Barbados</td>
	</tr>
	<tr>
		<td>BY</td>
		<td>Belarus</td>
	</tr>
	<tr>
		<td>BE</td>
		<td>Belgium</td>
	</tr>
	<tr>
		<td>BZ</td>
		<td>Belize</td>
	</tr>
	<tr>
		<td>BJ</td>
		<td>Benin</td>
	</tr>
	<tr>
		<td>BM</td>
		<td>Bermuda</td>
	</tr>
	<tr>
		<td>BT</td>
		<td>Bhutan</td>
	</tr>
	<tr>
		<td>BO</td>
		<td>Bolivia [Bolivia, Plurinational State of]</td>
	</tr>
	<tr>
		<td>BQ</td>
		<td>Bonaire, Sint Eustatius and Saba</td>
	</tr>
	<tr>
		<td>BA</td>
		<td>Bosnia and Herzegovina</td>
	</tr>
	<tr>
		<td>BW</td>
		<td>Botswana</td>
	</tr>
	<tr>
		<td>BR</td>
		<td>Brazil</td>
	</tr>
	<tr>
		<td>VG</td>
		<td>British Virgin Islands [Virgin Islands, British]</td>
	</tr>
	<tr>
		<td>BN</td>
		<td>Brunei [Brunei Darussalam]</td>
	</tr>
	<tr>
		<td>BG</td>
		<td>Bulgaria</td>
	</tr>
	<tr>
		<td>BF</td>
		<td>Burkina [Burkina Faso]</td>
	</tr>
	<tr>
		<td>MM</td>
		<td>Burma [Myanmar]</td>
	</tr>
	<tr>
		<td>BI</td>
		<td>Burundi</td>
	</tr>
	<tr>
		<td>KH</td>
		<td>Cambodia</td>
	</tr>
	<tr>
		<td>CM</td>
		<td>Cameroon</td>
	</tr>
	<tr>
		<td>CA</td>
		<td>Canada</td>
	</tr>
	<tr>
		<td>IC</td>
		<td>Canary Islands</td>
	</tr>
	<tr>
		<td>CV</td>
		<td>Cape Verde</td>
	</tr>
	<tr>
		<td>XW</td>
		<td>Caribbean not otherwise specified</td>
	</tr>
	<tr>
		<td>KY</td>
		<td>Cayman Islands</td>
	</tr>
	<tr>
		<td>CF</td>
		<td>Central African Republic</td>
	</tr>
	<tr>
		<td>XU</td>
		<td>Central America not otherwise specified</td>
	</tr>
	<tr>
		<td>TD</td>
		<td>Chad</td>
	</tr>
	<tr>
		<td>XL</td>
		<td>Channel Islands not otherwise specified</td>
	</tr>
	<tr>
		<td>CL</td>
		<td>Chile</td>
	</tr>
	<tr>
		<td>CN</td>
		<td>China</td>
	</tr>
	<tr>
		<td>CX</td>
		<td>Christmas Island</td>
	</tr>
	<tr>
		<td>CC</td>
		<td>Cocos (Keeling) Islands</td>
	</tr>
	<tr>
		<td>CO</td>
		<td>Colombia</td>
	</tr>
	<tr>
		<td>KM</td>
		<td>Comoros</td>
	</tr>
	<tr>
		<td>CG</td>
		<td>Congo</td>
	</tr>
	<tr>
		<td>CD</td>
		<td>Congo (Democratic Republic) [Congo (The Democratic Republic of the)] {formerly Zaire}</td>
	</tr>
	<tr>
		<td>CK</td>
		<td>Cook Islands</td>
	</tr>
	<tr>
		<td>CR</td>
		<td>Costa Rica</td>
	</tr>
	<tr>
		<td>HR</td>
		<td>Croatia</td>
	</tr>
	<tr>
		<td>CU</td>
		<td>Cuba</td>
	</tr>
	<tr>
		<td>CW</td>
		<td>Curaçao</td>
	</tr>
	<tr>
		<td>XA</td>
		<td>Cyprus (European Union)</td>
	</tr>
	<tr>
		<td>XB</td>
		<td>Cyprus (Non-European Union)</td>
	</tr>
	<tr>
		<td>XC</td>
		<td>Cyprus not otherwise specified</td>
	</tr>
	<tr>
		<td>CZ</td>
		<td>Czech Republic</td>
	</tr>
	<tr>
		<td>DK</td>
		<td>Denmark</td>
	</tr>
	<tr>
		<td>DJ</td>
		<td>Djibouti</td>
	</tr>
	<tr>
		<td>DM</td>
		<td>Dominica</td>
	</tr>
	<tr>
		<td>DO</td>
		<td>Dominican Republic</td>
	</tr>
	<tr>
		<td>TL</td>
		<td>East Timor [Timor Leste]</td>
	</tr>
	<tr>
		<td>EC</td>
		<td>Ecuador</td>
	</tr>
	<tr>
		<td>EG</td>
		<td>Egypt</td>
	</tr>
	<tr>
		<td>SV</td>
		<td>El Salvador</td>
	</tr>
	<tr>
		<td>XF</td>
		<td>England</td>
	</tr>
	<tr>
		<td>GQ</td>
		<td>Equatorial Guinea</td>
	</tr>
	<tr>
		<td>ER</td>
		<td>Eritrea</td>
	</tr>
	<tr>
		<td>EE</td>
		<td>Estonia</td>
	</tr>
	<tr>
		<td>ET</td>
		<td>Ethiopia</td>
	</tr>
	<tr>
		<td>XP</td>
		<td>Europe not otherwise specified</td>
	</tr>
	<tr>
		<td>EU</td>
		<td>European Union not otherwise specified</td>
	</tr>
	<tr>
		<td>FK</td>
		<td>Falkland Islands [Falkland Islands (Malvinas)]</td>
	</tr>
	<tr>
		<td>FO</td>
		<td>Faroe Islands</td>
	</tr>
	<tr>
		<td>FJ</td>
		<td>Fiji</td>
	</tr>
	<tr>
		<td>FI</td>
		<td>Finland</td>
	</tr>
	<tr>
		<td>FR</td>
		<td>France {includes Corsica}</td>
	</tr>
	<tr>
		<td>GF</td>
		<td>French Guiana</td>
	</tr>
	<tr>
		<td>PF</td>
		<td>French Polynesia</td>
	</tr>
	<tr>
		<td>GA</td>
		<td>Gabon</td>
	</tr>
	<tr>
		<td>GM</td>
		<td>Gambia, The</td>
	</tr>
	<tr>
		<td>GE</td>
		<td>Georgia</td>
	</tr>
	<tr>
		<td>DE</td>
		<td>Germany</td>
	</tr>
	<tr>
		<td>GH</td>
		<td>Ghana</td>
	</tr>
	<tr>
		<td>GI</td>
		<td>Gibraltar</td>
	</tr>
	<tr>
		<td>GR</td>
		<td>Greece</td>
	</tr>
	<tr>
		<td>GL</td>
		<td>Greenland</td>
	</tr>
	<tr>
		<td>GD</td>
		<td>Grenada</td>
	</tr>
	<tr>
		<td>GP</td>
		<td>Guadeloupe</td>
	</tr>
	<tr>
		<td>GU</td>
		<td>Guam</td>
	</tr>
	<tr>
		<td>GT</td>
		<td>Guatemala</td>
	</tr>
	<tr>
		<td>GG</td>
		<td>Guernsey</td>
	</tr>
	<tr>
		<td>GN</td>
		<td>Guinea</td>
	</tr>
	<tr>
		<td>GW</td>
		<td>Guinea-Bissau</td>
	</tr>
	<tr>
		<td>GY</td>
		<td>Guyana</td>
	</tr>
	<tr>
		<td>HT</td>
		<td>Haiti</td>
	</tr>
	<tr>
		<td>HN</td>
		<td>Honduras</td>
	</tr>
	<tr>
		<td>HK</td>
		<td>Hong Kong (Special Administrative Region of China) [Hong Kong]</td>
	</tr>
	<tr>
		<td>HU</td>
		<td>Hungary</td>
	</tr>
	<tr>
		<td>IS</td>
		<td>Iceland</td>
	</tr>
	<tr>
		<td>IN</td>
		<td>India</td>
	</tr>
	<tr>
		<td>ID</td>
		<td>Indonesia</td>
	</tr>
	<tr>
		<td>IR</td>
		<td>Iran [Iran, Islamic Republic of]</td>
	</tr>
	<tr>
		<td>IQ</td>
		<td>Iraq</td>
	</tr>
	<tr>
		<td>IE</td>
		<td>Ireland</td>
	</tr>
	<tr>
		<td>IM</td>
		<td>Isle of Man</td>
	</tr>
	<tr>
		<td>IL</td>
		<td>Israel</td>
	</tr>
	<tr>
		<td>IT</td>
		<td>Italy {Includes Sardinia, Sicily}</td>
	</tr>
	<tr>
		<td>CI</td>
		<td>Ivory Coast [Côte D'ivoire]</td>
	</tr>
	<tr>
		<td>JM</td>
		<td>Jamaica</td>
	</tr>
	<tr>
		<td>JP</td>
		<td>Japan</td>
	</tr>
	<tr>
		<td>JE</td>
		<td>Jersey</td>
	</tr>
	<tr>
		<td>JO</td>
		<td>Jordan</td>
	</tr>
	<tr>
		<td>KZ</td>
		<td>Kazakhstan</td>
	</tr>
	<tr>
		<td>KE</td>
		<td>Kenya</td>
	</tr>
	<tr>
		<td>KI</td>
		<td>Kiribati</td>
	</tr>
	<tr>
		<td>KP</td>
		<td>Korea (North) [Korea, Democratic People's Republic of]</td>
	</tr>
	<tr>
		<td>KR</td>
		<td>Korea (South) [Korea, Republic of]</td>
	</tr>
	<tr>
		<td>QO</td>
		<td>Kosovo</td>
	</tr>
	<tr>
		<td>KW</td>
		<td>Kuwait</td>
	</tr>
	<tr>
		<td>KG</td>
		<td>Kyrgyzstan</td>
	</tr>
	<tr>
		<td>LA</td>
		<td>Laos [Lao People's Democratic Republic]</td>
	</tr>
	<tr>
		<td>LV</td>
		<td>Latvia</td>
	</tr>
	<tr>
		<td>LB</td>
		<td>Lebanon</td>
	</tr>
	<tr>
		<td>LS</td>
		<td>Lesotho</td>
	</tr>
	<tr>
		<td>LR</td>
		<td>Liberia</td>
	</tr>
	<tr>
		<td>LY</td>
		<td>Libya</td>
	</tr>
	<tr>
		<td>LI</td>
		<td>Liechtenstein</td>
	</tr>
	<tr>
		<td>LT</td>
		<td>Lithuania</td>
	</tr>
	<tr>
		<td>LU</td>
		<td>Luxembourg</td>
	</tr>
	<tr>
		<td>MO</td>
		<td>Macao (Special Administrative Region of China) [Macao]</td>
	</tr>
	<tr>
		<td>MK</td>
		<td>Macedonia [Macedonia, The Former Yugoslav Republic of]</td>
	</tr>
	<tr>
		<td>MG</td>
		<td>Madagascar</td>
	</tr>
	<tr>
		<td>MW</td>
		<td>Malawi</td>
	</tr>
	<tr>
		<td>MY</td>
		<td>Malaysia</td>
	</tr>
	<tr>
		<td>MV</td>
		<td>Maldives</td>
	</tr>
	<tr>
		<td>ML</td>
		<td>Mali</td>
	</tr>
	<tr>
		<td>MT</td>
		<td>Malta</td>
	</tr>
	<tr>
		<td>MH</td>
		<td>Marshall Islands</td>
	</tr>
	<tr>
		<td>MQ</td>
		<td>Martinique</td>
	</tr>
	<tr>
		<td>MR</td>
		<td>Mauritania</td>
	</tr>
	<tr>
		<td>MU</td>
		<td>Mauritius</td>
	</tr>
	<tr>
		<td>YT</td>
		<td>Mayotte</td>
	</tr>
	<tr>
		<td>MX</td>
		<td>Mexico</td>
	</tr>
	<tr>
		<td>FM</td>
		<td>Micronesia [Micronesia, Federated States of]</td>
	</tr>
	<tr>
		<td>XR</td>
		<td>Middle East not otherwise specified</td>
	</tr>
	<tr>
		<td>MD</td>
		<td>Moldova [Moldova, Republic of]</td>
	</tr>
	<tr>
		<td>MC</td>
		<td>Monaco</td>
	</tr>
	<tr>
		<td>MN</td>
		<td>Mongolia</td>
	</tr>
	<tr>
		<td>ME</td>
		<td>Montenegro</td>
	</tr>
	<tr>
		<td>MS</td>
		<td>Montserrat</td>
	</tr>
	<tr>
		<td>MA</td>
		<td>Morocco</td>
	</tr>
	<tr>
		<td>MZ</td>
		<td>Mozambique</td>
	</tr>
	<tr>
		<td>NA</td>
		<td>Namibia</td>
	</tr>
	<tr>
		<td>NR</td>
		<td>Nauru</td>
	</tr>
	<tr>
		<td>NP</td>
		<td>Nepal</td>
	</tr>
	<tr>
		<td>NL</td>
		<td>Netherlands</td>
	</tr>
	<tr>
		<td>AN</td>
		<td>Netherlands Antilles</td>
	</tr>
	<tr>
		<td>NC</td>
		<td>New Caledonia</td>
	</tr>
	<tr>
		<td>NZ</td>
		<td>New Zealand</td>
	</tr>
	<tr>
		<td>NI</td>
		<td>Nicaragua</td>
	</tr>
	<tr>
		<td>NE</td>
		<td>Niger</td>
	</tr>
	<tr>
		<td>NG</td>
		<td>Nigeria</td>
	</tr>
	<tr>
		<td>NU</td>
		<td>Niue</td>
	</tr>
	<tr>
		<td>NF</td>
		<td>Norfolk Island</td>
	</tr>
	<tr>
		<td>XT</td>
		<td>North America not otherwise specified</td>
	</tr>
	<tr>
		<td>XG</td>
		<td>Northern Ireland</td>
	</tr>
	<tr>
		<td>MP</td>
		<td>Northern Mariana Islands</td>
	</tr>
	<tr>
		<td>NO</td>
		<td>Norway</td>
	</tr>
	<tr>
		<td>ZZ</td>
		<td>Not known</td>
	</tr>
	<tr>
		<td>PS</td>
		<td>Occupied Palestinian Territories [Palestine, State of] {formerly West Bank (including East Jerusalem) and Gaza Strip}</td>
	</tr>
	<tr>
		<td>OM</td>
		<td>Oman</td>
	</tr>
	<tr>
		<td>PK</td>
		<td>Pakistan</td>
	</tr>
	<tr>
		<td>PW</td>
		<td>Palau</td>
	</tr>
	<tr>
		<td>PA</td>
		<td>Panama</td>
	</tr>
	<tr>
		<td>PG</td>
		<td>Papua New Guinea</td>
	</tr>
	<tr>
		<td>PY</td>
		<td>Paraguay</td>
	</tr>
	<tr>
		<td>PE</td>
		<td>Peru</td>
	</tr>
	<tr>
		<td>PH</td>
		<td>Philippines</td>
	</tr>
	<tr>
		<td>PN</td>
		<td>Pitcairn, Henderson, Ducie and Oeno Islands [Pitcairn]</td>
	</tr>
	<tr>
		<td>PL</td>
		<td>Poland</td>
	</tr>
	<tr>
		<td>PT</td>
		<td>Portugal {includes Madeira, Azores}</td>
	</tr>
	<tr>
		<td>PR</td>
		<td>Puerto Rico</td>
	</tr>
	<tr>
		<td>QA</td>
		<td>Qatar</td>
	</tr>
	<tr>
		<td>RE</td>
		<td>Réunion</td>
	</tr>
	<tr>
		<td>RO</td>
		<td>Romania</td>
	</tr>
	<tr>
		<td>RU</td>
		<td>Russia [Russian Federation]</td>
	</tr>
	<tr>
		<td>RW</td>
		<td>Rwanda</td>
	</tr>
	<tr>
		<td>WS</td>
		<td>Samoa</td>
	</tr>
	<tr>
		<td>SM</td>
		<td>San Marino</td>
	</tr>
	<tr>
		<td>ST</td>
		<td>Sao Tome and Principe</td>
	</tr>
	<tr>
		<td>SA</td>
		<td>Saudi Arabia</td>
	</tr>
	<tr>
		<td>XH</td>
		<td>Scotland</td>
	</tr>
	<tr>
		<td>SN</td>
		<td>Senegal</td>
	</tr>
	<tr>
		<td>RS</td>
		<td>Serbia</td>
	</tr>
	<tr>
		<td>SC</td>
		<td>Seychelles</td>
	</tr>
	<tr>
		<td>SL</td>
		<td>Sierra Leone</td>
	</tr>
	<tr>
		<td>SG</td>
		<td>Singapore</td>
	</tr>
	<tr>
		<td>SX</td>
		<td>Sint Maarten (Dutch part)</td>
	</tr>
	<tr>
		<td>SK</td>
		<td>Slovakia</td>
	</tr>
	<tr>
		<td>SI</td>
		<td>Slovenia</td>
	</tr>
	<tr>
		<td>SB</td>
		<td>Solomon Islands</td>
	</tr>
	<tr>
		<td>SO</td>
		<td>Somalia</td>
	</tr>
	<tr>
		<td>ZA</td>
		<td>South Africa</td>
	</tr>
	<tr>
		<td>XV</td>
		<td>South America not otherwise specified</td>
	</tr>
	<tr>
		<td>GS</td>
		<td>South Georgia and The South Sandwich Islands</td>
	</tr>
	<tr>
		<td>SS</td>
		<td>South Sudan</td>
	</tr>
	<tr>
		<td>ES</td>
		<td>Spain {includes Ceuta, Melilla}</td>
	</tr>
	<tr>
		<td>LK</td>
		<td>Sri Lanka</td>
	</tr>
	<tr>
		<td>BL</td>
		<td>St Barthélemy</td>
	</tr>
	<tr>
		<td>SH</td>
		<td>St Helena, Ascension and Tristan da Cunha</td>
	</tr>
	<tr>
		<td>KN</td>
		<td>St Kitts and Nevis</td>
	</tr>
	<tr>
		<td>LC</td>
		<td>St Lucia</td>
	</tr>
	<tr>
		<td>MF</td>
		<td>St Martin (French Part) [St Martin]</td>
	</tr>
	<tr>
		<td>PM</td>
		<td>St Pierre and Miquelon</td>
	</tr>
	<tr>
		<td>VC</td>
		<td>St Vincent and The Grenadines</td>
	</tr>
	<tr>
		<td>SD</td>
		<td>Sudan</td>
	</tr>
	<tr>
		<td>SR</td>
		<td>Surinam [Suriname]</td>
	</tr>
	<tr>
		<td>SJ</td>
		<td>Svalbard and Jan Mayen</td>
	</tr>
	<tr>
		<td>SZ</td>
		<td>Swaziland</td>
	</tr>
	<tr>
		<td>SE</td>
		<td>Sweden</td>
	</tr>
	<tr>
		<td>CH</td>
		<td>Switzerland</td>
	</tr>
	<tr>
		<td>SY</td>
		<td>Syria [Syrian Arab Republic]</td>
	</tr>
	<tr>
		<td>TW</td>
		<td>Taiwan [Taiwan, Province of China]</td>
	</tr>
	<tr>
		<td>TJ</td>
		<td>Tajikistan</td>
	</tr>
	<tr>
		<td>TZ</td>
		<td>Tanzania [Tanzania, United Republic of]</td>
	</tr>
	<tr>
		<td>TH</td>
		<td>Thailand</td>
	</tr>
	<tr>
		<td>TG</td>
		<td>Togo</td>
	</tr>
	<tr>
		<td>TK</td>
		<td>Tokelau</td>
	</tr>
	<tr>
		<td>TO</td>
		<td>Tonga</td>
	</tr>
	<tr>
		<td>TT</td>
		<td>Trinidad and Tobago</td>
	</tr>
	<tr>
		<td>TN</td>
		<td>Tunisia</td>
	</tr>
	<tr>
		<td>TR</td>
		<td>Turkey</td>
	</tr>
	<tr>
		<td>TM</td>
		<td>Turkmenistan</td>
	</tr>
	<tr>
		<td>TC</td>
		<td>Turks and Caicos Islands</td>
	</tr>
	<tr>
		<td>TV</td>
		<td>Tuvalu</td>
	</tr>
	<tr>
		<td>UG</td>
		<td>Uganda</td>
	</tr>
	<tr>
		<td>UA</td>
		<td>Ukraine</td>
	</tr>
	<tr>
		<td>AE</td>
		<td>United Arab Emirates</td>
	</tr>
	<tr>
		<td>XK</td>
		<td>United Kingdom, not otherwise specified</td>
	</tr>
	<tr>
		<td>US</td>
		<td>United States</td>
	</tr>
	<tr>
		<td>VI</td>
		<td>United States Virgin Islands [Virgin Islands, U. S.]</td>
	</tr>
	<tr>
		<td>UY</td>
		<td>Uruguay</td>
	</tr>
	<tr>
		<td>UZ</td>
		<td>Uzbekistan</td>
	</tr>
	<tr>
		<td>VU</td>
		<td>Vanuatu</td>
	</tr>
	<tr>
		<td>VA</td>
		<td>Vatican City [Holy See (Vatican City State)]</td>
	</tr>
	<tr>
		<td>VE</td>
		<td>Venezuela [Venezuela, Bolivarian Republic of]</td>
	</tr>
	<tr>
		<td>VN</td>
		<td>Vietnam [Viet Nam]</td>
	</tr>
	<tr>
		<td>XI</td>
		<td>Wales</td>
	</tr>
	<tr>
		<td>WF</td>
		<td>Wallis and Futuna</td>
	</tr>
	<tr>
		<td>EH</td>
		<td>Western Sahara</td>
	</tr>
	<tr>
		<td>YE</td>
		<td>Yemen</td>
	</tr>
	<tr>
		<td>ZM</td>
		<td>Zambia</td>
	</tr>
	<tr>
		<td>ZW</td>
		<td>Zimbabwe</td>
	</tr>
</table>

###Notes
If a domicile country is unknown, please use code 'ZZ'
Omitting this property may hinder the development or use of an effective analytics model.

##TERMTIME_ACCOM
###Description
The current term time accomodation type of student

###Purpose
For detailed analysis within Learning Analytics/ Data Modelling

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/TTACCOM

###Valid Values & Mappings

<table>
<tr><td>TERMTIME_ACCOM</td><td>DESCRIPTION(ENGLISH)</td><td>DESCRIPTION(WELSH)</td><td>HESA(TTACCOM)</td><td>FEILR(ACCOM)  </td></tr>
<tr><td>1</td><td>Provider maintained property</td><td></td><td>1</td><td>5  </td></tr>
<tr><td>2</td><td>Parental/guardian home</td><td></td><td>2</td><td>N/A  </td></tr>
<tr><td>4</td><td>Other</td><td>Arall</td><td>4</td><td>NULL  </td></tr>
<tr><td>5</td><td>Not known</td><td>Anhysbys</td><td>5</td><td>N/A  </td></tr>
<tr><td>6</td><td>Not in attendance at the provider</td><td></td><td>6</td><td>N/A  </td></tr>
<tr><td>7</td><td>Own residence</td><td></td><td>7</td><td>N/A  </td></tr>
<tr><td>8</td><td>Other rented accommodation</td><td></td><td>8</td><td>N/A  </td></tr>
<tr><td>9</td><td>Private-sector halls</td><td></td><td>9</td><td>N/A  </td></tr>
</table>   

Please Note - N/A denotes that no mapping value is applicable (and should not be confused with NULL)  

###Format
Int

###Notes
If the type is unknown, code '5' should be used
Omitting this property may hinder the development or use of an effective analytics model.

##PARENTS_ED
###Description
Whether parents have higher education qualification

###Purpose
For detailed analysis within Learning Analytics/ Data Modelling

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/PARED

###Valid Values

<table>
<tr><td>PARENTS_ED</td><td>DESCRIPTION(ENGLISH)</td><td>DESCRIPTION(WELSH)  </td></tr>
<tr><td>1</td><td>Yes</td><td>Ie  </td></tr>
<tr><td>2</td><td>No</td><td>Na  </td></tr>
<tr><td>7</td><td>No response given</td><td>Dim Ateb  </td></tr>
<tr><td>8</td><td>Don't know</td><td>Anhysbys  </td></tr>
<tr><td>9</td><td>Information refused</td><td>Gwybodaeth wedi ei ddal yn ol  </td></tr>
</table>

###Format
Int

###Notes
Where this is unknown, the code '8' should be provided. This information may not be available for FE/ ILR institutions, and only HE.
Omitting this property may hinder the development or use of an effective analytics model.

##SOCIO_EC
###Description
This field collects the socio-economic classification of students participating in HE if 21 or over at the start of their course or parental classification if under 21

###Purpose
For detailed analysis within Learning Analytics/ Data Modelling

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/SEC

###Valid Values

<table>
<tr><td>SOCIO_EC</td><td>DESCRIPTION(ENGLISH)</td><td>DESCRIPTION(WELSH)  </td></tr>
<tr><td>1</td><td>Higher managerial &amp; professional occupations</td><td>  </td></tr>
<tr><td>2</td><td>Lower managerial &amp; professional occupations</td><td>   </td></tr>
<tr><td>3</td><td>Intermediate occupations</td><td>  </td></tr>
<tr><td>4</td><td>Small employers &amp; own account workers</td><td>  </td></tr>
<tr><td>5</td><td>Lower supervisory &amp; technical occupations</td><td>  	</td></tr>
<tr><td>6</td><td>Semi-routine occupations</td><td>  	</td></tr>
<tr><td>7</td><td>Routine occupations</td><td>  	</td></tr>
<tr><td>8</td><td>Never worked &amp; long-term unemployed</td><td>  	</td></tr>
<tr><td>9</td><td>Not classified</td><td>Dim math</td></tr>
</table>  

###Format
Int

###Notes
Where this is unknown, the code '9' should be provided. This information may not be available for FE/ ILR institutions, and only HE.
Omitting this property may hinder the development or use of an effective analytics model.


##OVERSEAS
###Description
Whether the student is classified as a home student (UK), or European (EU) or as Overseas (rest of the world)

###Purpose
For detailed analysis within Learning Analytics/ Data Modelling

###Derivation
Jisc

###Valid Values

<table>
<tr><td>OVERSEAS</td><td>DESCRIPTION(ENGLISH)</td><td>DESCRIPTION(WELSH)</td></tr>
<tr><td>1</td><td>United Kingdom</td><td>Deyrnas Unedig  </td></tr>
<tr><td>2</td><td>Europe (EU)</td><td>Ewrop (UE)  </td></tr>
<tr><td>3</td><td>Rest of the World (Overseas)</td><td>Gweddill y Byd  </td></tr>
<tr><td>99</td><td>Not Known</td><td>Anhysbys</td></tr>
</table>  

###Format
Int

###Notes
If this value is unknown, then code '99' should be used. The mapping for these fields could be done using the Nationality indicator, or other relevant source within the HESA/ student records system database.
Omitting this property may hinder the development or use of an effective analytics model.


##APPSHIB_ID
###Description.
The person identifier used by Shibboleth / The UK Access Management Federation to grant access to the Jisc analytics student app via the Shibboleth - JWT gateway.

###Purpose
Analytics

###Derivation
https://www.internet2.edu/media/medialibrary/2013/09/04/internet2-mace-dir-eduperson-200604.html

###Valid Values
Not specified

###Format
String (256)

###Notes
There may be a more general AIM_ID property later that can be used for any UK Federation service provider ID, not just the Jisc analytics student app Shibboleth - JWT gateway.


##VLE_ID
###Description.
The ID assigned to a student by the VLE.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
Not specified

###Format
String (256)

###Notes
Note that this is not a universal user ID; there maybe several VLEs, or records from other types of tools.


##HUSID
###Description.
A HESA student identifier unique to each student. It is intended that the identifier is to be transferred with the student to each provider of higher education he or she may attend. The objective is that the use of this number will facilitate the accurate tracking of students throughout their experience within the sector for which HESA collects data.

###Purpose
Analytics

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/HUSID

###Format of Valid Values
- First 2 digits:</td><td>Year of entry into provider (last 2 digits of year)
- Next 4 digits:</td><td>HESA institution identifier + 1000
- Next 6 digits:</td><td>6 digit reference number internally allocated by provider.
- Last digit:</td><td>Check digit.

###Format
String (13)

###Notes


##USERNAME
###Description
This is the username for systems access at the Institution

###Purpose
To be used for user login/ account lookup purposes

###Format
String (255)

###Notes
This will typically be imported and updated continuously from Institution identity management systems.


##LAST_NAME
###Description
Students family or surname.

###Purpose
For display. Used by Student App, Student Success Planner, Tribal Insight

###Derivation
Jisc

###Valid Values
Any

###Format
String

###Notes


##FIRST_NAME
###Description
Students given or first name

###Purpose
For display. Used by Student App, Student Success Planner, Tribal Insight

###Derivation
Jisc

###Valid Values
Any

###Format
String

###Notes


##ADDRESS_LINE_1
###Description
Address Line 1 - term-time accommodation

###Purpose
For display. Used by Student Success Planner

###Derivation
Jisc

###Valid Values
Any

###Format
String

###Notes
This is usually imported from the Institution's SRS.


##ADDRESS_LINE_2
###Description
Address Line 2 - term-time accommodation

###Purpose
For display. Used by Student Success Planner

###Derivation
Jisc

###Valid Values
Any

###Format
String

###Notes
This is usually imported from the Institution's SRS.


##ADDRESS_LINE_3
###Description
Address Line 3 - term-time accommodation

###Purpose
For display. Used by Student Success Planner

###Derivation
Jisc

###Valid Values
Any

###Format
String

###Notes
This is usually imported from the Institution's SRS.


##ADDRESS_LINE_4
###Description
Address Line 4 - term-time accommodation

###Purpose
For display. Used by Student Success Planner

###Derivation
Jisc

###Valid Values
Any

###Format
String

###Notes
This is usually imported from the Institution's SRS.


##POSTCODE
###Description
This is the current (term-time) postcode corresponding to the student's accommodation address provided

###Purpose
For display. Used by Student Success Planner

###Derivation
Jisc
https://www.hesa.ac.uk/collection/c16051/a/TTPCODE

###Valid Values
See [https://www.hesa.ac.uk/collection/c16051/a/TTPCODE](HESA definition for details.)

###Format
String (8)

###Notes
This should relate to the term-time postcode of the student's residency, and NOT the entry postcode onto the student's learning instance


##PRIMARY_EMAIL_ADDRESS
###Description
Students primary email address

###Purpose
For display and contact via student success planner. Used by Student Success Planner

###Derivation
Jisc

###Valid Values
Any

###Format
String(255)

###Notes
Will be input/ batched directly from central IT or identification management systems at the institution


##HOME_PHONE
###Description
Students home telephone number. This can refer to the landline telephone number of their term-time or non term-time accomodation.

###Purpose
For display and contact purposes. Used by Student Success Planner

###Derivation
Jisc

###Valid Values
Any

###Format
String(255)

###Notes
This is usually imported from the Institution's SRS.


##MOBILE_PHONE
###Description
Students mobile telephone number.

###Purpose
For display and contact purposes. Used by Student Success Planner

###Derivation
Jisc

###Valid Values
Any

###Format
String(255)

###Notes
This is usually imported from the Institution's SRS.


##PHOTO_URL
###Description
URL link provided to a latest/ recent photo of student

###Purpose
For display purposes. Used by Student Success Planner

###Derivation
Jisc

###Valid Values
Any

###Format
GIF or JPG (exact list of formats, and ideal (minimum) photo resolution, to be confirmed)

###Notes
This assumes that there is a way of securing access to the photo.


##TUTOR_STAFF_ID
###Description
This is the unique identification number for the learner's academic or course year supervisor/ tutor, or alternatively the id of the contact who will be responsible for handling Learning Analytics alerts and notification regarding the student

###Purpose
For notification and alerts purposes for Learning Analytics SSP and other software tools

###Derivation
https://www.hesa.ac.uk/collection/c15025/a/OWNSTAFFID

###References

###Format
String(255)

###Notes
This will be the unique identifier/ primary key for the member of staff who is responsible for the student (course/ year tutor) or the person responsible for receiving alerts and notifications from the Learning Analytics software suite/ tools. This will typically be the staff/ HR/ payroll number for the member of academic staff, which links to their email address in the institutions identity management system.


##ENTRY_POSTCODE
###Description.
Identifies the postcode of the student's permanent or home address prior to entry to the course. It is not necessarily the correspondence address of the student.

###Purpose
Analytics 

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/postcode/

###Valid Values
[https://www.hesa.ac.uk/collection/c16051/a/postcode/](See HESA definition for particulars)

###Format
String (8)

###Notes