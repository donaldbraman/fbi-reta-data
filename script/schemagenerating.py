


home_dir = 'D:/SUMMER/RA/FBI_RETA_DATA-2015-06-04'
source_dir = home_dir + '/recoded-data/'

a=open(source_dir+'schema.txt','w')

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

file_header_types = (["STRING"] * 15) + (["INTEGER"] + (["STRING"] * 2)) * 3 + (["INTEGER"] * 3) + (["STRING"] * 13) 
monthly_header_types = (["STRING"] * 11) 
cards_0123_types = (["INTEGER"] * 28)
card_4_types = (["STRING"] * 3)
mt = monthly_header_types + (cards_0123_types * 4) + card_4_types # monthly field types 
field_types =  file_header_types + (mt * 12)

lines=('{        \n',  '    \'fields\': [\n')

for i in range(0,1551):
  lines=lines+tuple('    {\'name\':\'%s\', \'type\':\'%s\'},\n' %(field_names[i],field_types[i]))

lineslastline=lines+tuple('    {\'name\':\'%s\', \'type\':\'%s\'}\n' %(field_names[1551],field_types[1551]))
linesending=('    ]\n','} ')

finishedlines=lineslastline+linesending
a.writelines(finishedlines)
a.close()
