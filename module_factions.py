from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0xFF033E), #0x888888 -> 0xFF033E
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  # ("dark_knights","{!}Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []), ## Tocan Invasion ##

  ("culture_1",  "{!}culture_1", 0, 0.9, [], []),
  ("culture_2",  "{!}culture_2", 0, 0.9, [], []),
  ("culture_3",  "{!}culture_3", 0, 0.9, [], []),
  ("culture_4",  "{!}culture_4", 0, 0.9, [], []),
  ("culture_5",  "{!}culture_5", 0, 0.9, [], []),
  ("culture_6",  "{!}culture_6", 0, 0.9, [], []),
  ("culture_7",  "{!}culture_7", 0, 0.9, [], []), ## Tocan Player Faction
  ("culture_dark_knights",  "{!}culture_dark_knights", 0, 0.9, [], []), ## Tocan Invasion ##
  ("culture_8",  "{!}culture_8", 0, 0.9, [], []),
  ("culture_9",  "{!}culture_9", 0, 0.9, [], []),
  ("culture_10",  "{!}culture_10", 0, 0.9, [], []),
  ("culture_11",  "{!}culture_11", 0, 0.9, [], []),
  ("culture_12",  "{!}culture_12", 0, 0.9, [], []),
  ("culture_13",  "{!}culture_13", 0, 0.9, [], []),
  ("culture_14",  "{!}culture_14", 0, 0.9, [], []),
  ("culture_15",  "{!}culture_15", 0, 0.9, [], []),
  ("culture_16",  "{!}culture_16", 0, 0.9, [], []),

#  ("swadian_caravans","Swadian Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
#  ("vaegir_caravans","Vaegir Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),

  ("player_faction","Player Faction",0, 0.9, [], []),
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("player_faction",1.00),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xFF4433), #changed name so that can tell difference if shows up on map
  ("kingdom_1",  "Kingdom of Saarisenmaa", 0, 0.9, [("outlaws",-0.05),("sea_raiders",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xEE7744),
  ("kingdom_2",  "Kingdom of Peltomaa",    0, 0.9, [("outlaws",-0.05),("sea_raiders",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xC8FF91), #Tocan: was 0xCCBB99 in cc 0x9696FF
  ("kingdom_3",  "Kingdom of Vuorjoenlehdo", 0, 0.9, [("outlaws",-0.05),("sea_raiders",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC99FF),
  ("kingdom_4",  "Kingdom of Amigulth",    0, 0.9, [("outlaws",-0.05),("sea_raiders",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x33DDDD),
  ("kingdom_5",  "Kingdom of Talorgulth",  0, 0.9, [("outlaws",-0.05),("sea_raiders",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x33DD33),
  ("kingdom_6",  "Kivimiehiaa Clans",  0, 0.9, [("outlaws",-0.05),("sea_raiders",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xDDDD33),
  ("kingdom_7",  "Kiklapplandr Tribes",  0, 0.9, [("outlaws",-0.05),("sea_raiders",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x3066DB),
  ("dark_knights","Njerpez Clans", max_player_rating(-40), 0.5,[("commoners",-0.9),("player_faction",-0.4),("player_supporters_faction",-0.4)], [], 0x9696FF), ## Tocan Invasion ## 0x9696FF /// kingdom 8
  ("kingdom_9",  "Beormandr Tribes",  0, 0.9, [("outlaws",-0.05),("sea_raiders",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x813E3B),
  ("kingdom_10",  "Principality of the Parunsohna",  0, 0.9, [("outlaws",-0.05),("sea_raiders",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xF38A84),
  ("kingdom_11",  "Kingdom of Dohraviaj",  0, 0.9, [("outlaws",-0.05),("sea_raiders",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xA3A1FF),
  ("kingdom_12",  "Kingdom of Bezdonijos",  0, 0.9, [("outlaws",-0.05),("sea_raiders",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xE39B2B),
  ("kingdom_13",  "Kingdom of Kurshis",  0, 0.9, [("outlaws",-0.05),("sea_raiders",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x2B726B),
  ("kingdom_14",  "Frithdom of Heodenasland",  0, 0.9, [("outlaws",-0.05),("sea_raiders",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xD7573A),
  ("kingdom_15",  "Witan of the Saenskaland",  0, 0.9, [("outlaws",-0.05),("sea_raiders",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xD7573A),
  ("kingdom_16",  "Witan of the Jryvaj",  0, 0.9, [("outlaws",-0.05),("sea_raiders",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xD7573A),

##  ("kingdom_1_rebels",  "Swadian rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_2_rebels",  "Vaegir rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_3_rebels",  "Khergit rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_4_rebels",  "Nord rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_5_rebels",  "Rhodok rebels",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),

  ("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),
  ("black_khergits","{!}Black Khergits", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.02),("kingdom_2",-0.02)], []),

##  ("rebel_peasants","Rebel Peasants", 0, 0.5,[("vaegirs",-0.5),("player_faction",0.0)], []),

  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("deserters",-0.6),("mountain_bandits",-0.6),("forest_bandits",-0.6),("player_faction",0.0)], []), ## Tocan: added bandit relations
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0xFF033E),
  ("mountain_bandits","Mountain Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0xFF033E),
  ("forest_bandits","Forest Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0xFF033E),

  ("mercs_celts","Fianna Albiorix", 0, 0.5,[("outlaws",-0.6)], [], 0x0000FF),
  ("mercs_vikings","Jomsweerlingr", 0, 0.5,[("manhunters",-0.6)], [], 0x0E470E),
  ("mercs_chuds","Tjuudjit Mercenaries", 0, 0.5,[("outlaws",-0.6)], [], 0x6FA8DC),
  ("adventurers","Adventurers", 0, 0.5,[("outlaws",-0.6),("mercs_celts",-0.6),("mercs_vikings",-0.6),("mercs_chuds",-0.6)], [], 0x4B4B4B),

  ("guild_frith","Frith Guild", 0, 0.5,[("outlaws",-0.6),("deserters",-0.6),("mountain_bandits",-0.6),("forest_bandits",-0.6),("player_faction",0.0)], []),

  ("sea_raiders","Weerlingr", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x71C7FF), #0x888888 -> 0xFF033E

  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("peasant_rebels","{!}Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
]

##diplomacy start+ Define these for convenience
dplmc_factions_begin = 1 #As mentioned in the notes above, this is hardcoded and shouldn't be altered.  Deliberately excludes "no faction".
dplmc_non_generic_factions_begin = [x[0] for x in enumerate(factions) if x[1][0] == "merchants"][0] + 1
dplmc_factions_end   = len(factions)
##diplomacy end+

# modmerger_start version=201 type=4
try:
    component_name = "factions"
    var_set = { "factions":factions,"default_kingdom_relations":default_kingdom_relations, }
    from modmerger import modmerge
    modmerge(var_set, component_name)
except:
    raise
# modmerger_end
