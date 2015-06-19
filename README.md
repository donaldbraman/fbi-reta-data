# FBI-RETA-DATA
This contains the Return A Masterfiles of the FBI's Uniform Crime Reporting dataset. 

FIXED LENGTH, UNPACKED DATA FORMAT
LRECL	=  7385
BLOCKSIZE  =  29540  (default)

POSITION		TYPE		DESCRIPTION

1			A1		1 =  Identifier code for RETURN-A master file.
2  -  3		A2		Numeric State Code.   Range is 01-62.  Data records are in
order by ORI code within numeric state code. The values are:
50  = AK -Alaska
01  = AL  -Alabama
03  = AR - Arkansas
54  = AS - American Samoa 
02  = AZ - Arizona 
04  = CA - California
05  = CO - Colorado
06  = CT - Connecticut
52  = CZ - Canal Zone
08  = DC - District of Columbia
07  = DE - Delaware
09  = FL  - Florida
10  = GA- Georgia
55  = GM - Guam
51  = HI - Hawaii
14  = IA -  Iowa
11  = ID -  Idaho
12  = IL -  Illinois
13  = IN - Indiana
15  = KS - Kansas
16  = KY - Kentucky
17  = LA - Louisiana
20  = MA - Massachusetts
19  = MD - Maryland
18  = ME - Maine
21  = MI - Michigan
22  = MN - Minnesota
24  =  MO - Missouri
23  =  MS -  Mississippi
25  =  MT -  Montana
26  =  NB -  Nebraska
32  =  NC -  North Carolina
33  =  ND  - North Dakota
28  =  NH -  New Hampshire
29  =  NJ  -  New Jersey
30  =  NM - New Mexico
27  =  NV  - Nevada
31  =  NY  - New York
34  =  OH  - Ohio
35  =  OK  - Oklahoma
36  =  OR  - Oregon
37  =  PA  - Pennsylvania
53  =  PR  - Puerto Rico
38  =  RI   - Rhode Island
39  =  SC  - South Carolina
40  =  SD  - South Dakota
41  =  TN  - Tennessee
42  =  TX  - Texas
43  =  UT  - Utah
62  =  VI   - Virgin Islands
45  =  VA -  Virginia
44  =  VT -  Vermont
46  =  WA - Washington
48  =  WI  -  Wisconsin
47  =  WV -  West Virginia
49  =  WY -  Wyoming

4  -  10		A7		ORI Code.  Originating Agency Identifier.

11 - 12		A2		Group. Group 0 is possessions;  1 - 7 are cities; 8 - 9 are
counties.  Sub-group (position 12) is blank when not used.
All populations are inclusive.  Values are:

0  = Possessions (Puerto Rico, Guam, Canal Zone, Virgin Islands, and American Samoa)
1  = All cities 250,000 or over:
1A= Cities 1,000,000 or over
1B= Cities from 500,000 thru 999,999
1C= Cities from 250,000 thru 499,999
2  =  Cities from 100,000 thru 249,000
3  =  Cities from 50,000 thru 99,000
4  =  Cities from 25,000 thru 49,999
5  =  Cities from 10,000 thru 24,999
6  =  Cities from 2,500 thru 9,999
7  =  Cities under 2,500
8  =  Non-MSA Counties:
8A= Non-MSA counties 100,000 or over
8B= Non-MSA counties from 25,000 thru 99,999
8C= Non-MSA counties from 10,000 thru 24,999
8D= Non-MSA counties under 10,000
8E= Non-MSA State Police
9  = MSA Counties:
9A= MSA counties 100,000 or over
9B= MSA counties from 25,000 thru 99,999
9C= MSA counties from 10,000 thru 24,999
9D= MSA counties under 10,000
9E= MSA State Police

13			A1		Division.  Geographic division in which the state is located (from 1 thru 9).  Possessions are coded "0".  The states comprising each division are as follows.  The divisions are listed within region:

0  =  Possessions
Div. 0:	54  American Samoa
52  Canal Zone
55  Guam
53  Puerto Rico
62  Virgin Islands

REGION I  - NORTHEAST

1  =  New  England
Div. 1:
06  Connecticut
18  Maine
20  Massachusetts
28  New Hampshire		
38  Rhode Island
44  Vermont

2  = Middle  Atlantic
Div. 2:
29  New Jersey
31  New York		
37  Pennsylvania

REGION II  -  NORTH CENTRAL

3  =  East North Central
Div. 3:
12  Illinois
13  Indiana
21  Michigan
34   Ohio
48  Wisconsin

4  =  West North Central
Div. 4:	
14  Iowa
15  Kansas
22  Minnesota
24  Missouri
26  Nebraska
33  North Dakota
40  South Dakota
  
REGION III   -   SOUTH

5  =  South Atlantic
Div. 5:	
07  Delaware
08  District of Columbia
09  Florida
10  Georgia
19  Maryland
32  North Carolina
39  South Carolina
45   Virginia
47  West Virginia
6  =  East South Central
Div. 6:	01  Alabama
16  Kentucky		
23  Mississippi
41  Tennessee

7  =  West South Central
Div. 7:	
03  Arkansas
17  Louisiana
35  Oklahoma
42  Texas

REGION  IV  -  WEST

8  =  Mountain
Div. 8:	
02  Arizona
05  Colorado
11  Idaho
25  Montana
27  Nevada			
30  New Mexico
43  Utah		
49  Wyoming


9  =  Pacific
Div. 9:	
50  Alaska
04  California
51  Hawaii			
36  Oregon
46 Washington

14  -  15		A2		Year.    Last two digits of the year the data reflects, e.g., "85" = 1985, "90" = 1990, etc.
16  -  20		A5		Sequence Number.   A five-digit number which places all cities in alphabetic order, regardless of state.  This field is blank for groups 0, 8, and 9.
21  -  22		A2		Juvenile Age.  The juvenile age limit in the state in which the agency is located.

POSITION		TYPE		DESCRIPTION

23			A1		Core City Indication.
Y = core city of MSA
N = not core city of MSA

24  -  30		A7		Covered By.   The ORI of the agency that submits crime data for the agency represented by the header. For example, a county will often submit a return which includes the crime data for a city within that county.  This field is blank	if the agency is not a "covered-by."

31			A1		Covered By Group.   This is the group of the "covered-by" ORI above.
32  -  37		A6		Last Update.   The date the heading or mailing list information was last updated (MMDDYY).
38  -  41		A4		Field Office.  The four-digit  numeric code for the FBI field office whose territory covers the agency.
42  -  43		A2		Number of Months Reported.  The highest "valued" month that was reported for the year by the submitting agency.  For example, if October was the last month submitted or is the only month submitted, "10" would be the value.  This value also can be used to stop processing once October ("10") has been processed. Again, the value does not mean that there are necessarily 10 full months reported.  It does mean that the tenth month is the last month reported on the return for the year.

44			A1		Agency Count.   Used to accumulate "agencies used" totals in various tabulations.  This field is normally "1" but will be "0" for the U.S. Park Police and all State Police agencies whose ORI code ends in "SP" (or "99" in  California).

Population Data Group (45 - 59) occurs 3 times.
45  -  53		N9		Population Data -1  - Population.   This is the	population of the City in the County below.
54  -  56		A3		Population Data - 1 - County.  This is the county in which the city is in.

POSITION		TYPE		DESCRIPTION
57  -  59		A3		Population Data - 1 - MSA.    If present, it is the code of the MSA in which it is located.
60  -  74		15		Population Data - 2 - Group.   If city resides in two counties, this is the second largest county population.
75  -  89		15		Population Data - 3 - Group.   If city resides in three counties, this is the third largest county population.

NOTE:  Adding the three populations provides the total population of the city.
90  -  98		N9		Population 1  - Last Census.
99  - 107		N9		Population 2  - Last Census
108- 116		N9		Population 3  - Last Census

These are the populations taken from the previous census. The fields correspond to the meaning of the previous three Population Data Groups.

117			A1		Population Source.   No documentation exists that reflects the year to year code changes.   This was the source for the current population.  This can be from certain commercial publications, from a special census or extra populationbased on the data from prior years or from the census. If unused, it should be blank.  The code values are 1-9, but meanings of the codes are not available.

118			A1		Follow-Up Indication.   Periodically all agencies submitting 					RETURN-A's are checked to see if they have submitted a 					return for the preceding months.  If not they are sent a "Follow-					Up" return.  This indication is used to show if this particular 					agency should be sent a "Follow-Up".

Y = Send a Follow-Up
N = Do Not Send a Follow-Up

119			A1		Special Mailing Group.   When addressing RETURN-A's,  the
tape is sorted by Zip Code so that the forms can be mailed by
geographic area.  Special Mailing Group agencies are excluded


POSITION		TYPE		DESCRIPTION

119			A1		Special Mailing Group. (continued) from this arrangement andare handled separately.  The field contains:

0  =  If not a special mailing group agency.
1  =  If the return is to be sent to another agency.
2  =  Small city (groups 5 - 7) to be sent a large city (groups 1 -
4) form.
7  =  If the agency is a "Non-Contributor", it is not sent forms.
9  =  If the agency is a Contributor but not on the mailing list, they are not sent forms.

120			A1		Special Mailing Address.   This indication is used when the first line of the mailing address is other than "Chief of Police" or "Sheriff".

Y  =  Special mailing address.
N  =  Not a special mailing address.

121 - 144		A24		Agency Name.
145 - 150		A6		Agency State Name.
151 - 180		A30		First Line of Mailing Address.
181 - 210		A30		Second Line of Mailing Address.
211 - 240		A30		Third Line of Mailing Address.
241 - 270		A30		Fourth Line of Mailing Address.
271 - 275		A5		Zip Code.
276			    A1		Old Population Group.  The population group the agency was in the previous year.
277 - 305		A29		Unused  - Blanks.

The area represented by positions 306 - 895 occurs once for each month for which a return has been received.  If there are any missing months, the corresponding area will be zeros and blanks, depending on field type.  For example, a return for October will always be in the tenth position, July will always be in 


POSITION		TYPE		DESCRIPTION

277 - 305		A29		Unused  - Blanks. (continued)  the seventh, etc.  The number of months received is located in Number of Months Reported in positions 42 - 43.

Month data in 306 - 895 occurs 12 times.

306 - 895		590		01 - January. 

Month
306 - 307		A2		Month Included In.   Used only if an agency does not submit a return, say for January, but indicates on the February return that it includes the January data. In this case, the January area would have "02" in this field with the remainder of the month data initialized to field defaults of  zeros and  blanks, if applicable.

308 - 313		A6		Date of Last Update.   The date this month area was updated, in the form of MMDDYY.
314			A1		Card 0 Type.   The type of data in column 3 of the 

RETURN-A.  The types are:

0 = Not updated.
2 = Adjustment.
4 = Not available.
5 = Normal Return.

315			A1		Card 1 Type.   Same codes as Card 0, except it is for column 4.
316			A1		Card 2 Type.   Same codes as Card 0, except it is for column 5.
317			A1		Card 3 Type.   Same codes as Card 0 , except it is for column 6.
318			A1		Card 4 Type.   Same codes as Card 0, except it is for Police Assault information on the RETURN-A.  If value is "8", the information is included but is unusable.
319			A1		Card 0 P/T.   Shows whether the data for column 3 includes the "breakdown" offenses (P), or shows only the totals (T).  Field is blank if no return has been received.
320			A1		Card 1 P/T.   As noted above but for column 4.
321			A1		Card 2 P/T.   As noted above but for column 5.
322			A1		Card 3 P/T.   As noted above but for column 6.

CARD  0
323 - 462		N140		Card 0.   The next 28 fields contain the "number of unfounded offenses" information entered from column 3 (Card 0).  All fields will be zeros for records prior to 1983.
323 - 327		N5		1 - Murder
328 - 332		N5		2 - Manslaughter
333 - 337		N5		3 - Rape Total
338 - 342		N5		4 - Rape by Force
343 - 347		N5		5 - Attempted Rape
348 - 352		N5		6 - Robbery Total
353 - 357		N5		7 - Robbery With A Gun
358 - 362		N5		8 - Robbery With a Knife (only collected 1974 and later, will bezero for any prior years)	
363 - 367		N5		9 - Robbery - Other Weapon (only collected 1974 and later, will be zero for any prior years)
368 - 372		N5		10-Strong-Arm Robbery
373 - 377		N5		11-Assault Total
378 - 382		N5		12-Assault With a Gun
383 - 387		N5		13-Assault With a Knife


POSITION		TYPE		DESCRIPTION
388 - 392		N5		14-Assault - Other Weapon
393 - 397		N5		15-Assault With Hands, Feet, etc.
398 - 402		N5		16-Simple Assault
403 - 407		N5		17-Burglary Total
408 - 412		N5		18-Burglary - Forcible Entry
413 - 417		N5		19-Burglary - No Forcible Entry
418 - 422		N5		20-Attempted Burglary
423 - 427		N5		21-Larceny Total
428 - 432		N5		22-Motor Vehicle Theft Total
433 - 437		N5		23-Auto Theft
438 - 442		N5		24-Truck,  Bus Theft
443 - 447		N5		25-Other Vehicle Theft
448 - 452		N5		26-Grand Total of All Fields
453 - 457		N5		27-Larceny Under $50.00
458 - 462		N5		28-UNUSED

CARD 1
463 - 602		N140		Card 1.   The next 28 fields contain the "Number of Actual Offenses" information entered from column 4 (Card 1). Field 27 will contain data only if the tape is for a year prior to 1974
Same field definitions as Card 0

CARD 2
603 - 742		N140		Card 2.   The next 28 fields contain the "Total Offenses Cleared by Arrest" information entered from column 5 (Card 2). Field 27 will contain data only if the tape is for a year prior to 1974.
Same field definitions as Card 0.

CARD 3
743 - 882		N140		Card 3.   The next 28 fields contain the "Number of Clearances Under 18" information entered from column 6 (Card 3).  Field 27 will contain data only if the tape is for a year prior to 1974.
Same field definitions as Card 0.

CARD 4
883 - 885		N3		Number of Officers Killed by Felonious Acts.   Information entered from Card 4, Police Assault data.
886 - 888		N3		Number of Officers Killed by Accidental or Negligent Acts.   Information entered from Card 4, Police Assault data.
889 - 895		N7		Number of Officers Assaulted.    Information entered from Card 4, Police Assault data.

E N D   O F   M O N T H

POSITION		TYPE		DESCRIPTION
896 -1485		590		02 - February.   Same format as January
1486-2075		590		03 - March.   	  Same format as January
2076-2665		590		04 - April.  	  Same format as January
2666-3255		590		05 - May.   	  Same format as January.
3256-3845		590		06 - June.   	  Same format as January.
3846-4435		590		07 - July.   	  Same format as January.
4436-5025		590		08 - August.  	  Same format as January.
5026-5615		590		09 - September. Same format as January.
5616-6205		590		10 - October.      Same format as January.
6206-6795		590		11 - November.   Same format as January.
6796-7385		590		12 - December.   Same format as January.

E N D   O F    R E C O R D
