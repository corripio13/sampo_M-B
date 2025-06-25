from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed.
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4)]),

("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
("looters", "Looters", icon_axeman|carries_goods(8), 0, fac_outlaws, bandit_personality, [(trp_looter,3,50)] ),
# Ryan END
("manhunters", "Manhunters", icon_gray_knight, 0, fac_manhunters, soldier_personality, [(trp_slaver_chief,1,1),(trp_slave_crusher,1,10),(trp_slave_hunter,2,20),(trp_slave_driver,2,20),(trp_manhunter,4,49)] ),
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),
("steppe_bandits", "Steppe Bandits", icon_khergit|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_steppe_bandit3,1,4),(trp_steppe_bandit2,2,12),(trp_steppe_bandit,5,84)] ),
("taiga_bandits", "Tundra Bandits", icon_axeman|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_taiga_bandit3,1,4),(trp_taiga_bandit2,2,12),(trp_taiga_bandit,5,84)] ),
("desert_bandits", "Desert Bandits", icon_vaegir_knight|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_desert_bandit3,1,4),(trp_desert_bandit2,2,12),(trp_desert_bandit,5,84)] ),
("forest_bandits", "Forest Bandits", icon_axeman|carries_goods(2), 0, fac_forest_bandits, bandit_personality, [(trp_forest_bandit3,1,4),(trp_forest_bandit2,2,12),(trp_forest_bandit,5,84)] ),
("mountain_bandits", "Mountain Bandits", icon_axeman|carries_goods(2), 0, fac_mountain_bandits, bandit_personality, [(trp_mountain_bandit3,1,4),(trp_mountain_bandit2,2,12),(trp_mountain_bandit,5,84)] ),
("sea_raiders", "Weerlingr Raiders", icon_axeman|carries_goods(2), 0, fac_sea_raiders, bandit_personality, [(trp_sea_raider3,1,4),(trp_sea_raider2,2,12),(trp_sea_raider,5,84)] ),
#wulf Tocan
("sea_raiders_ships", "Weerlingr Raiders", icon_ship|pf_is_ship|carries_goods(10), 0, fac_sea_raiders, bandit_personality, [(trp_sea_raider3,1,2),(trp_sea_raider2,2,5),(trp_sea_raider,47,93)] ),
#wulf end
("pirates_ships", "Pirates", icon_ship|pf_is_ship|carries_goods(10), 0, fac_outlaws, bandit_personality, [(trp_pirate,50,150)] ),

("mercenary_warband", "Mercenary Warband", icon_vaegir_knight|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_mercenary_swordsman,7,8),(trp_mercenary_horseman,4,6),(trp_mercenary_axeman,4,6),(trp_mercenary_crossbowman,7,8),(trp_mercenary_axe_thrower,4,6),(trp_mercenary_horsearcher,4,6)] ),
("mercenary_warband_2", "Mercenary Warband", icon_vaegir_knight|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_mercenary_swordsman,7,8),(trp_mercenary_cavalry,4,6),(trp_mercenary_archer,7,8),(trp_mercenary_spear_thrower,4,6),(trp_mercenary_spearman,4,6),(trp_mercenary_horsearcher,4,6)] ),

#Braganca
("braganca_party", "Rodrigo de Braganca's Party", icon_axeman|carries_goods(8), 0, fac_outlaws, bandit_personality, [(trp_quick_battle_troop_1,1,1),(trp_mercenary_swordsman,100,100),(trp_mercenary_spearman,100,100),(trp_mercenary_crossbowman,199,199),(trp_mercenary_spear_thrower,50,50),(trp_mercenary_axeman,50,50)] ),
("braganca_bandits", "Rodrigo de Braganca's Bandits", icon_axeman|carries_goods(8), 0, fac_outlaws, bandit_personality, [(trp_mercenary_swordsman,13,13),(trp_mercenary_spearman,5,5),(trp_mercenary_crossbowman,13,13),(trp_mercenary_spear_thrower,9,9),(trp_mercenary_axeman,5,5),(trp_mercenary_axe_thrower,5,5)] ),
#Usiatra
("usiatra_party", "Usiatra's Party", icon_vaegir_knight|carries_goods(8), 0, fac_outlaws, bandit_personality, [(trp_quick_battle_troop_2,1,1),(trp_desert_bandit3,30,30),(trp_desert_bandit2,60,60),(trp_desert_bandit,109,109)] ),
("usiatra_bandits", "Usiatra's Bandits", icon_vaegir_knight|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_desert_bandit3,5,5),(trp_desert_bandit2,15,15),(trp_desert_bandit,30,30)] ),
#Sverre
("sverre_party", "Sverre's Party", icon_axeman|carries_goods(8), 0, fac_sea_raiders, bandit_personality, [(trp_quick_battle_troop_5,1,1),(trp_sea_raider3,30,30),(trp_sea_raider2,60,60),(trp_sea_raider,109,109)] ),
("sverre_bandits", "Sverre's Weerlingr Raiders", icon_axeman|carries_goods(2), 0, fac_sea_raiders, bandit_personality, [(trp_sea_raider3,5,5),(trp_sea_raider2,15,15),(trp_sea_raider,30,30)] ),
#Aethrod
("aethrod_party", "Aethrod's Party", icon_axeman|carries_goods(8), 0, fac_outlaws, bandit_personality, [(trp_quick_battle_troop_9,1,1),(trp_taiga_bandit3,30,30),(trp_taiga_bandit2,60,60),(trp_taiga_bandit,109,109)] ),
("aethrod_bandits", "Aethrod's Bandits", icon_axeman|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_taiga_bandit3,5,5),(trp_taiga_bandit2,15,15),(trp_taiga_bandit,30,30)] ),
#Zaira
("zaira_party", "Zaira's Party", icon_vaegir_knight|carries_goods(8), 0, fac_outlaws, bandit_personality, [(trp_quick_battle_troop_10,1,1),(trp_desert_bandit3,30,30),(trp_desert_bandit2,60,60),(trp_desert_bandit,109,109)] ),
("zaira_bandits", "Zaira's Bandits", icon_vaegir_knight|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_desert_bandit3,5,5),(trp_desert_bandit2,15,15),(trp_desert_bandit,30,30)] ),
#Miura Tang
("tang_party", "Miura Tang's Party", icon_vaegir_knight|carries_goods(8), 0, fac_outlaws, bandit_personality, [(trp_miura_tang,1,1),(trp_samurai_bandits,199,199)] ),

#Warbands
("hegen_party", "Hegen's Party", icon_gray_knight|carries_goods(8)|pf_show_faction, 0, fac_kingdom_1, soldier_personality, [(trp_quick_battle_troop_3,1,1),(trp_swadian_sergeant,25,25),(trp_swadian_sharpshooter,24,24),(trp_swadian_knight,25,25),(trp_swadian_veteran_archer,25,25)] ),
("konrad_party", "Konrad's Band", icon_gray_knight|carries_goods(8), 0, fac_manhunters, soldier_personality, [(trp_quick_battle_troop_4,1,1),(trp_mercenary_swordsman,20,20),(trp_mercenary_axeman,20,20),(trp_mercenary_spear_thrower,20,20),(trp_mercenary_archer,20,20),(trp_mercenary_axe_thrower,19,19)] ),
("borislav_party", "Borislav's Band", icon_gray_knight|carries_goods(8), 0, fac_manhunters, soldier_personality, [(trp_quick_battle_troop_6,1,1),(trp_mercenary_swordsman,20,20),(trp_mercenary_spearman,19,19),(trp_mercenary_archer,20,20),(trp_mercenary_spear_thrower,20,20),(trp_mercenary_axe_thrower,20,20)] ),
("stavros_party", "Stavros Manhunters", icon_gray_knight|carries_goods(8), 0, fac_manhunters, soldier_personality, [(trp_quick_battle_troop_7,1,1),(trp_mercenary_swordsman,20,20),(trp_mercenary_spearman,19,19),(trp_mercenary_crossbowman,20,20),(trp_mercenary_axe_thrower,20,20),(trp_mercenary_axeman,20,20)] ),
("gamara_party", "Gamara's Band", icon_gray_knight|carries_goods(8), 0, fac_manhunters, soldier_personality, [(trp_quick_battle_troop_8,1,1),(trp_mercenary_swordsman,20,20),(trp_mercenary_spearman,19,19),(trp_mercenary_archer,20,20),(trp_mercenary_axeman,20,20),(trp_mercenary_spear_thrower,20,20)] ),

("deserters", "Deserters", icon_vaegir_knight|carries_goods(3), 0, fac_deserters, bandit_personality, [] ),

("merchant_caravan","Merchant Caravan",icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
("troublesome_bandits", "Troublesome Bandits", icon_axeman|carries_goods(9)|pf_quest_party, 0, fac_outlaws, bandit_personality, [(trp_bandit,14,100)] ),
("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8)]),

("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,30,50)]),
("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
##Floris addon seatrade Tocan
("sea_traders", "Royal Traders", icon_ship|pf_is_ship|carries_goods(50)|pf_show_faction, 0, fac_commoners, merchant_personality, [(trp_ship_captain,1,1),(trp_mercenary_swordsman,10,30),(trp_mercenary_crossbowman,5,15),(trp_mercenary_archer,5,15),(trp_mercenary_spearman,5,15),(trp_mercenary_axeman,5,15)] ),
("ship","Ship",icon_ship|pf_is_ship|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_ship_captain,1,1)]),
##Floris addon seatrade end Tocan

("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_watchman,4,20)]),

("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),

# Reinforcements
# each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
# less-modernised templates are generally includes 7-14 troops in total,
# med-modernised templates are generally includes 5-10 troops in total,
# high-modernised templates are generally includes 3-5 troops in total

## Tocan + ##
# These are the possible reinforcements your player faction lords can hire
("player_supporters_faction_reinforcements_a", "{!}psf_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_custom_peasant,5,10),(trp_custom_army_recruit,2,4)]),
("player_supporters_faction_reinforcements_b", "{!}psf_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_custom_infantry,3,6),(trp_custom_crossbow_militia,2,4)]),
("player_supporters_faction_reinforcements_c", "{!}psf_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_custom_squire,2,4),(trp_custom_crossbowman,1,2)]),
## Tocan - ##

("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_recruit,5,10),(trp_swadian_militia,2,4)]),
("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_footman,3,6),(trp_swadian_skirmisher,2,4)]),
("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,1,3),(trp_swadian_crossbowman,1,1),(trp_swadian_archer,1,1)]),

("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_recruit,5,10),(trp_vaegir_footman,2,4)]),
("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,2,4),(trp_vaegir_skirmisher,2,4),(trp_vaegir_footman,1,2)]),
("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,2,3),(trp_vaegir_infantry,1,2)]),

("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_tribesman,3,5),(trp_khergit_skirmisher,4,9)]),
("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,2,4),(trp_khergit_horse_archer,2,4),(trp_khergit_skirmisher,1,2)]),
("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,2,4),(trp_khergit_veteran_horse_archer,2,3)]),

("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_footman,5,10),(trp_nord_recruit,2,4)]),
("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_huntsman,2,5),(trp_nord_archer,2,3),(trp_nord_footman,1,2)]),
("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_warrior,3,5)]),

("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_tribesman,5,10),(trp_rhodok_spearman,2,4)]),
("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_crossbowman,3,6),(trp_rhodok_trained_crossbowman,2,4)]),
("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_veteran_spearman,2,3),(trp_rhodok_veteran_crossbowman,1,2)]),

("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sarranid_recruit,5,10),(trp_sarranid_footman,2,4)]),
("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sarranid_skirmisher,2,4),(trp_sarranid_veteran_footman,2,3),(trp_sarranid_footman,1,3)]),
("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sarranid_horseman,3,5)]),

## Tocan Invasion+ ##
 ("dark_knights_reinforcements_a", "{!}dark_knights_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_dark_knight,4,5),(trp_dark_sergeant,5,6),(trp_dark_marksman,6,7)] ),
 ("dark_knights_reinforcements_b", "{!}dark_knights_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_dark_knight,2,3),(trp_dark_sergeant,3,4),(trp_dark_marksman,5,6)] ),
 ("dark_knights_reinforcements_c", "{!}dark_knights_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_dark_knight,1,2),(trp_dark_sergeant,2,3),(trp_dark_marksman,2,3)] ),
# ("dark_knights_reinforcements_a", "{!}dark_knights_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_dark_knight,8,10),(trp_dark_sergeant,10,12),(trp_dark_marksman,12,14)] ),
# ("dark_knights_reinforcements_b", "{!}dark_knights_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_dark_knight,5,7),(trp_dark_sergeant,7,9),(trp_dark_marksman,10,12)] ),
# ("dark_knights_reinforcements_c", "{!}dark_knights_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_dark_knight,2,4),(trp_dark_sergeant,4,6),(trp_dark_marksman,5,7)] ),

("njerpezit_2", "Large Wandering Njerpezit", icon_vaegir_knight|carries_goods(8), 0, fac_dark_knights, bandit_personality, [(trp_desert_bandit3,30,30),(trp_desert_bandit2,60,60),(trp_desert_bandit,109,109)] ),
("njerpezit_1", "Small Wandering Njerpezit", icon_vaegir_knight|carries_goods(2), 0, fac_dark_knights, bandit_personality, [(trp_desert_bandit3,5,5),(trp_desert_bandit2,15,15),(trp_desert_bandit,30,30)] ),

## Tocan Invasion- ##

("steppe_bandit_lair", "Steppe Bandit Lair", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_steppe_bandit3,1,2),(trp_steppe_bandit2,1,5),(trp_steppe_bandit,13,43)] ),
("taiga_bandit_lair", "Tundra Bandit Lair", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_taiga_bandit3,1,2),(trp_taiga_bandit2,1,5),(trp_taiga_bandit,13,43)] ),
("desert_bandit_lair", "Desert Bandit Lair", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_desert_bandit3,1,2),(trp_desert_bandit2,1,5),(trp_desert_bandit,13,43)] ),
("forest_bandit_lair", "Forest Bandit Camp", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_forest_bandit3,1,2),(trp_forest_bandit2,1,5),(trp_forest_bandit,13,43)] ),
("mountain_bandit_lair", "Mountain Bandit Hideout", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_mountain_bandit3,1,2),(trp_mountain_bandit2,1,5),(trp_mountain_bandit,13,43)] ),
("sea_raider_lair", "Weerling Raider Landing", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_sea_raider3,1,2),(trp_sea_raider2,1,5),(trp_sea_raider,13,43)] ),
("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),

("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,50)]),

("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),

##diplomacy begin
("dplmc_spouse","Your spouse",icon_woman|pf_civilian|pf_show_faction,0,fac_neutral,merchant_personality,[]),

("dplmc_gift_caravan","Your Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
#recruiter kit begin
("dplmc_recruiter","Recruiter",icon_gray_knight|pf_show_faction,0,fac_neutral,merchant_personality,[(trp_dplmc_recruiter,1,1)]),
#recruiter kit end
##diplomacy end
]
# modmerger_start version=201 type=2
try:
    component_name = "party_templates"
    var_set = { "party_templates" : party_templates }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
