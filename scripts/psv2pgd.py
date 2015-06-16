# The goal of this code is to move UCR data that has been prepared by another script into postgres.
# Nothing fancy. 


import re
from os.path import expanduser
import psycopg2 as pg
from collections import OrderedDict

home_dir = '/Volumes/black beauty/Google Drive/UCR MDM'
source_dir = home_dir + '/recoded data/'


# GENERATE VARIABLE NAMES
file_header_names = ("id", "state", "ori_code", "city_group", "division", "year", "sequence", 
  "juv_age", "core_ci", "covered_by", "ori_group", "last_update", "field_office", "num_months", 
  "agency_count", "pop1", "county1", "msa1", "pop2", "county2", "msa2", "pop3", "county3", "msa3", 
  "county1_pop", "county2_pop", "county3_pop", "pop_source", "follow_up", "special_mail_group", 
  "special_mail_addr", "agency_name", "agency_state", "address1", "address2", "address3", 
  "address4", "zip", "old_pop_group", "unused_header")
monthly_header_names = ("month_in", "date_last_update", 
  "card_0_type", "card_1_type", "card_2_type", "card_3_type", "card_4_type", 
  "card_0_pt", "card_1_pt", "card_2_pt", "card_3_pt") 
crime_card_prefixes = ("unfounded_", "actual_", "cleared_", "cleared_u18_")
cards_0123_names = ("murder", "manslaughter", "rape_total", "rape_by_force",  "rape_attempt", 
  "robbery", "robbery_gun", "robbery_knife", "robbery_othweap",  "robbery_strong_arm", 
  "assault", "assault_gun", "assault_knife", "assault_othweap", "assault_hands", "assault_simple", 
  "burglary", "burglary_forcible_entry", "burglary_no_forcible_entry", "burglary_attempt", 
  "larceny", "motor_vehicle_theft", "auto_theft", "truck_bus_theft", "other_vehicle_theft", 
  "total_all_fields", "larceny_under_50_dollars", "unused") 
cards =  tuple([prefix+offense for prefix in crime_card_prefixes for offense in cards_0123_names])
card_4_names = ("officers_killed_felony", "officers_killed_accident", "officers_assaulted")
card_names = monthly_header_names + cards + card_4_names
month_prefixes = ("jan_", "feb_", "mar_", "apr_", "may_", "jun_", "jul_", "aug_", "sep_", "oct_", "nov_", "dec_")
twelve_cards = tuple([month+cn for month in month_prefixes for cn in card_names])
field_names = file_header_names + twelve_cards


# GENERATE VARIABLE TYPES
# Smae idea, but a bit less involved as many of the types repeat. 
file_header_types = (["varchar"] * 15) + (["integer"] + (["varchar"] * 2)) * 3 + (["integer"] * 3) + (["varchar"] * 13) 
monthly_header_types = (["varchar"] * 11) 
cards_0123_types = (["integer"] * 28)
card_4_types = (["varchar"] * 3)
mt = monthly_header_types + (cards_0123_types * 4) + card_4_types # monthly field types 
field_types =  file_header_types + (mt * 12)

# create & clean up a zipped & ordered dict so that it can be used nicely in a SQL statement  
my_od = str(OrderedDict(zip(field_names, field_types)))
field_defs = re.sub("""', '""", ' ', 
    re.sub("""'\), \('""", ', ', 
    re.sub("""OrderedDict\(\[\('""", '',
    re.sub("""'\)\]\)""", '',
    my_od))))



# create our db (after dropping, if one exists)
conn = None
create_string = 'CREATE TABLE reta (' + field_defs + ')'

try:
  conn = pg.connect("dbname='ucr' user='dbraman' host='localhost' password='mander1n!'") 
  cur = conn.cursor()  
  cur.execute("DROP TABLE IF EXISTS ucr")
  cur.execute("DROP TABLE IF EXISTS reta")
  cur.execute(create_string)
  conn.commit()

except pg.DatabaseError as e:
  if conn:
    conn.rollback()
    print('rolled back')
  print('Error %s' % e)
  sys.exit(1)
    
finally:
  if conn:
    conn.close()



# set up our import function
def import_psv(import_string):
  conn = None
  try:
    conn = pg.connect("dbname='ucr' user='dbraman' host='localhost' password='mander1n!'")
    cur = conn.cursor()  
    cur.execute(import_string)
    conn.commit()
  except pg.DatabaseError as e:
    if conn:
      conn.rollback()
      print('rolled back')
    print('Error %s' % e)
  finally:  
    if conn:
      conn.close()



# cycle over all the files
for year_num in range(1960, 2011):                           # one for each year that we have data
  print('processing ' + str(year_num))
  import_string = """COPY reta FROM '""" + source_dir + """reta_""" + str(year_num) + """_data.psv' DELIMITER '|' CSV; """
  import_psv(import_string)

print("All done!")








