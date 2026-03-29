# Main generic mechanics. 
default stat_1 = 0 
default stat_2 = 0 

label stat_check: 
    $ stat_1 = round(max(0, min(stat_1, 100)), 1)
    $ stat_2 = round(max(0, min(stat_2, 100)), 1)         # Cap for core stats
return 

# Relationship flags
default flag_a = 0 
default flag_b = 0  
default flag_c = 0 
default flag_d = 0 

# Flag checks for relationships
label flag_check: 
  $ flag_a = round(max(0, min(flag_a, 80)), 1)
  $ flag_b = round(max(0, min(flag_b, 80)), 1)
  $ flag_c = round(max(0, min(flag_c, 80)), 1) 
  $ flag d = round(max(0, min(flag_d, 80)), 1)
return
