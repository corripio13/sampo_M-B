from header_map_icons import *
from module_constants import *
from header_operations import *
from header_triggers import *
from ID_sounds import *

####################################################################################################################
#  Each map icon record contains the following fields:
#  1) Map icon id: used for referencing map icons in other files.
#     The prefix icon_ is automatically added before each map icon id.
#  2) Map icon flags. See header_map icons.py for a list of available flags
#  3) Mesh name.
#  4) Scale. 
#  5) Sound.
#  6) Offset x position for the flag icon.
#  7) Offset y position for the flag icon.
#  8) Offset z position for the flag icon.
####################################################################################################################

banner_scale = 0.3
avatar_scale = 0.15

map_icons = [
  ("player",0,"player", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0),
  ("player_horseman",0,"player_horseman", avatar_scale, snd_gallop, 0.15, 0.173, 0),
  ("gray_knight",0,"knight_a", avatar_scale, snd_gallop, 0.15, 0.173, 0),
  ("vaegir_knight",0,"knight_b", avatar_scale, snd_gallop, 0.15, 0.173, 0),
  ("flagbearer_a",0,"flagbearer_a", avatar_scale, snd_gallop, 0.15, 0.173, 0),
  ("flagbearer_b",0,"flagbearer_b", avatar_scale, snd_gallop, 0.15, 0.173, 0),
  ("peasant",0,"peasant_a", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  ("khergit",0,"khergit_horseman", avatar_scale,snd_gallop, 0.15, 0.173, 0),
  ("khergit_horseman_b",0,"khergit_horseman_b", avatar_scale,snd_gallop, 0.15, 0.173, 0),
  ("axeman",0,"bandit_a", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  ("woman",0,"woman_a", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  ("woman_b",0,"woman_b", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  ("town",mcn_no_shadow,"map_town_a", 0.35,0),
  ("town_steppe",mcn_no_shadow,"map_town_steppe_a", 0.35,0),
  ("town_desert",mcn_no_shadow,"map_town_desert_a", 0.35,0),
  ("village_a",mcn_no_shadow,"map_village_a", 0.45, 0),
  ("village_b",mcn_no_shadow,"map_village_b", 0.45, 0),
  ("village_c",mcn_no_shadow,"map_village_c", 0.45, 0),
  ("village_burnt_a",mcn_no_shadow,"map_village_burnt_a", 0.45, 0),
  ("village_deserted_a",mcn_no_shadow,"map_village_deserted_a", 0.45, 0),
  ("village_burnt_b",mcn_no_shadow,"map_village_burnt_b", 0.45, 0),
  ("village_deserted_b",mcn_no_shadow,"map_village_deserted_b", 0.45, 0),
  ("village_burnt_c",mcn_no_shadow,"map_village_burnt_c", 0.45, 0),
  ("village_deserted_c",mcn_no_shadow,"map_village_deserted_c", 0.45, 0),
  ("village_snow_a",mcn_no_shadow,"map_village_snow_a", 0.45, 0),
  ("village_snow_burnt_a",mcn_no_shadow,"map_village_snow_burnt_a", 0.45, 0),
  ("village_snow_deserted_a",mcn_no_shadow,"map_village_snow_deserted_a", 0.45, 0),


  ("camp",mcn_no_shadow,"camp_tent", 0.13, 0),
  ("ship",mcn_no_shadow,"boat_sail_on", 0.23, snd_footstep_grass, 0.0, 0.05, 0),
  ("ship_on_land",mcn_no_shadow,"boat_sail_off", 0.23, 0),

  ("castle_a",mcn_no_shadow,"map_castle_a", 0.35,0),
  ("castle_b",mcn_no_shadow,"map_castle_b", 0.35,0),
  ("castle_c",mcn_no_shadow,"map_castle_c", 0.35,0),
  ("castle_d",mcn_no_shadow,"map_castle_d", 0.35,0),
  ("town_snow",mcn_no_shadow,"map_town_snow_a", 0.35,0),


  ("castle_snow_a",mcn_no_shadow,"map_castle_snow_a", 0.35,0),
  ("castle_snow_b",mcn_no_shadow,"map_castle_snow_b", 0.35,0),
  ("mule",0,"icon_mule", 0.2,snd_footstep_grass, 0.15, 0.173, 0),
  ("cattle",0,"icon_cow", 0.2,snd_footstep_grass, 0.15, 0.173, 0),
  ("training_ground",mcn_no_shadow,"training", 0.35,0),

  ("bridge_a",mcn_no_shadow,"map_river_bridge_a", 1.27,0),
  ("bridge_b",mcn_no_shadow,"map_river_bridge_b", 0.7,0),
  ("bridge_snow_a",mcn_no_shadow,"map_river_bridge_snow_a", 1.27,0),

  ("custom_banner_01",0,"custom_map_banner_01", banner_scale, 0,
   [
     (ti_on_init_map_icon,
      [
        (store_trigger_param_1, ":party_no"),
        (party_get_slot, ":leader_troop", ":party_no", slot_town_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_map_icon_set_tableau_material, "tableau_custom_banner_square", ":leader_troop"),
        (try_end),
        ]),
     ]),
  ("custom_banner_02",0,"custom_map_banner_02", banner_scale, 0,
   [
     (ti_on_init_map_icon,
      [
        (store_trigger_param_1, ":party_no"),
        (party_get_slot, ":leader_troop", ":party_no", slot_town_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_map_icon_set_tableau_material, "tableau_custom_banner_short", ":leader_troop"),
        (try_end),
        ]),
     ]),
  ("custom_banner_03",0,"custom_map_banner_03", banner_scale, 0,
   [
     (ti_on_init_map_icon,
      [
        (store_trigger_param_1, ":party_no"),
        (party_get_slot, ":leader_troop", ":party_no", slot_town_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_map_icon_set_tableau_material, "tableau_custom_banner_tall", ":leader_troop"),
        (try_end),
        ]),
     ]),

  # Banners
  ("banner_01",0,"map_flag_01", banner_scale,0),
  ("banner_02",0,"map_flag_02", banner_scale,0),
  ("banner_03",0,"map_flag_03", banner_scale,0),
  ("banner_04",0,"map_flag_04", banner_scale,0),
  ("banner_05",0,"map_flag_05", banner_scale,0),
  ("banner_06",0,"map_flag_06", banner_scale,0),
  ("banner_07",0,"map_flag_07", banner_scale,0),
  ("banner_08",0,"map_flag_08", banner_scale,0),
  ("banner_09",0,"map_flag_09", banner_scale,0),
  ("banner_10",0,"map_flag_10", banner_scale,0),
  ("banner_11",0,"map_flag_11", banner_scale,0),
  ("banner_12",0,"map_flag_12", banner_scale,0),
  ("banner_13",0,"map_flag_13", banner_scale,0),
  ("banner_14",0,"map_flag_14", banner_scale,0),
  ("banner_15",0,"map_flag_f21", banner_scale,0),
  ("banner_16",0,"map_flag_16", banner_scale,0),
  ("banner_17",0,"map_flag_17", banner_scale,0),
  ("banner_18",0,"map_flag_18", banner_scale,0),
  ("banner_19",0,"map_flag_19", banner_scale,0),
  ("banner_20",0,"map_flag_20", banner_scale,0),
  ("banner_21",0,"map_flag_21", banner_scale,0),
  ("banner_22",0,"map_flag_22", banner_scale,0),
  ("banner_23",0,"map_flag_23", banner_scale,0),
  ("banner_24",0,"map_flag_24", banner_scale,0),
  ("banner_25",0,"map_flag_25", banner_scale,0),
  ("banner_26",0,"map_flag_26", banner_scale,0),
  ("banner_27",0,"map_flag_27", banner_scale,0),
  ("banner_28",0,"map_flag_28", banner_scale,0),
  ("banner_29",0,"map_flag_29", banner_scale,0),
  ("banner_30",0,"map_flag_30", banner_scale,0),
  ("banner_31",0,"map_flag_31", banner_scale,0),
  ("banner_32",0,"map_flag_32", banner_scale,0),
  ("banner_33",0,"map_flag_33", banner_scale,0),
  ("banner_34",0,"map_flag_34", banner_scale,0),
  ("banner_35",0,"map_flag_35", banner_scale,0),
  ("banner_36",0,"map_flag_36", banner_scale,0),
  ("banner_37",0,"map_flag_37", banner_scale,0),
  ("banner_38",0,"map_flag_38", banner_scale,0),
  ("banner_39",0,"map_flag_39", banner_scale,0),
  ("banner_40",0,"map_flag_40", banner_scale,0),
  ("banner_41",0,"map_flag_41", banner_scale,0),
  ("banner_42",0,"map_flag_42", banner_scale,0),
  ("banner_43",0,"map_flag_43", banner_scale,0),
  ("banner_44",0,"map_flag_44", banner_scale,0),
  ("banner_45",0,"map_flag_45", banner_scale,0),
  ("banner_46",0,"map_flag_46", banner_scale,0),
  ("banner_47",0,"map_flag_47", banner_scale,0),
  ("banner_48",0,"map_flag_48", banner_scale,0),
  ("banner_49",0,"map_flag_49", banner_scale,0),
  ("banner_50",0,"map_flag_50", banner_scale,0),
  ("banner_51",0,"map_flag_51", banner_scale,0),
  ("banner_52",0,"map_flag_52", banner_scale,0),
  ("banner_53",0,"map_flag_53", banner_scale,0),
  ("banner_54",0,"map_flag_54", banner_scale,0),
  ("banner_55",0,"map_flag_55", banner_scale,0),
  ("banner_56",0,"map_flag_56", banner_scale,0),
  ("banner_57",0,"map_flag_57", banner_scale,0),
  ("banner_58",0,"map_flag_58", banner_scale,0),
  ("banner_59",0,"map_flag_59", banner_scale,0),
  ("banner_60",0,"map_flag_60", banner_scale,0),
  ("banner_61",0,"map_flag_61", banner_scale,0),
  ("banner_62",0,"map_flag_62", banner_scale,0),
  ("banner_63",0,"map_flag_63", banner_scale,0),
  ("banner_64",0,"map_flag_d01", banner_scale,0),
  ("banner_65",0,"map_flag_d02", banner_scale,0),
  ("banner_66",0,"map_flag_d03", banner_scale,0),
  ("banner_67",0,"map_flag_d04", banner_scale,0),
  ("banner_68",0,"map_flag_d05", banner_scale,0),
  ("banner_69",0,"map_flag_d06", banner_scale,0),
  ("banner_70",0,"map_flag_d07", banner_scale,0),
  ("banner_71",0,"map_flag_d08", banner_scale,0),
  ("banner_72",0,"map_flag_d09", banner_scale,0),
  ("banner_73",0,"map_flag_d10", banner_scale,0),
  ("banner_74",0,"map_flag_d11", banner_scale,0),
  ("banner_75",0,"map_flag_d12", banner_scale,0),
  ("banner_76",0,"map_flag_d13", banner_scale,0),
  ("banner_77",0,"map_flag_d14", banner_scale,0),
  ("banner_78",0,"map_flag_d15", banner_scale,0),
  ("banner_79",0,"map_flag_d16", banner_scale,0),
  ("banner_80",0,"map_flag_d17", banner_scale,0),
  ("banner_81",0,"map_flag_d18", banner_scale,0),
  ("banner_82",0,"map_flag_d19", banner_scale,0),
  ("banner_83",0,"map_flag_d20", banner_scale,0),
  ("banner_84",0,"map_flag_d21", banner_scale,0),
  ("banner_85",0,"map_flag_e01", banner_scale,0),
  ("banner_86",0,"map_flag_e02", banner_scale,0),
  ("banner_87",0,"map_flag_e03", banner_scale,0),
  ("banner_88",0,"map_flag_e04", banner_scale,0),
  ("banner_89",0,"map_flag_e05", banner_scale,0),
  ("banner_90",0,"map_flag_e06", banner_scale,0),
  ("banner_91",0,"map_flag_e07", banner_scale,0),
  ("banner_92",0,"map_flag_e08", banner_scale,0),
  ("banner_93",0,"map_flag_e09", banner_scale,0),
  ("banner_94",0,"map_flag_e10", banner_scale,0),
  ("banner_95",0,"map_flag_e11", banner_scale,0),
  ("banner_96",0,"map_flag_e12", banner_scale,0),
  ("banner_97",0,"map_flag_e13", banner_scale,0),
  ("banner_98",0,"map_flag_e14", banner_scale,0),
  ("banner_99",0,"map_flag_e15", banner_scale,0),
  ("banner_100",0,"map_flag_e16", banner_scale,0),
  ("banner_101",0,"map_flag_e17", banner_scale,0),
  ("banner_102",0,"map_flag_e18", banner_scale,0),
  ("banner_103",0,"map_flag_e19", banner_scale,0),
  ("banner_104",0,"map_flag_e20", banner_scale,0),
  ("banner_105",0,"map_flag_e21", banner_scale,0),

  ("banner_106",0,"map_flag_f01", banner_scale,0),
  ("banner_107",0,"map_flag_f02", banner_scale,0),
  ("banner_108",0,"map_flag_f03", banner_scale,0),
  ("banner_109",0,"map_flag_f04", banner_scale,0),
  ("banner_110",0,"map_flag_f05", banner_scale,0),
  ("banner_111",0,"map_flag_f06", banner_scale,0),
  ("banner_112",0,"map_flag_f07", banner_scale,0),
  ("banner_113",0,"map_flag_f08", banner_scale,0),
  ("banner_114",0,"map_flag_f09", banner_scale,0),
  ("banner_115",0,"map_flag_f10", banner_scale,0),
  ("banner_116",0,"map_flag_f11", banner_scale,0),
  ("banner_117",0,"map_flag_f12", banner_scale,0),
  ("banner_118",0,"map_flag_f13", banner_scale,0),
  ("banner_119",0,"map_flag_f14", banner_scale,0),
  ("banner_120",0,"map_flag_f15", banner_scale,0),
  ("banner_121",0,"map_flag_f16", banner_scale,0),
  ("banner_122",0,"map_flag_f17", banner_scale,0),
  ("banner_123",0,"map_flag_f18", banner_scale,0),
  ("banner_124",0,"map_flag_f19", banner_scale,0),
  ("banner_125",0,"map_flag_f20", banner_scale,0),

  ("banner_126",0,"map_flag_f01", banner_scale,0),
  ("banner_127",0,"map_flag_f02", banner_scale,0),
  ("banner_128",0,"map_flag_f03", banner_scale,0),
  ("banner_129",0,"map_flag_f04", banner_scale,0),
  ("banner_130",0,"map_flag_f05", banner_scale,0),
  ("banner_131",0,"map_flag_f06", banner_scale,0),
  ("banner_132",0,"map_flag_f07", banner_scale,0),
  ("banner_133",0,"map_flag_f08", banner_scale,0),
  ("banner_134",0,"map_flag_f09", banner_scale,0),
  ("banner_135",0,"map_flag_f10", banner_scale,0),
  
  ("map_flag_kingdom_a",0,"map_flag_kingdom_a", banner_scale,0),
  ("map_flag_kingdom_b",0,"map_flag_kingdom_b", banner_scale,0),
  ("map_flag_kingdom_c",0,"map_flag_kingdom_c", banner_scale,0),
  ("map_flag_kingdom_d",0,"map_flag_kingdom_d", banner_scale,0),
  ("map_flag_kingdom_e",0,"map_flag_kingdom_e", banner_scale,0),
  ("map_flag_kingdom_f",0,"map_flag_kingdom_f", banner_scale,0),
  ("map_flag_kingdom_dk",0,"map_flag_kingdom_dk", banner_scale,0),  ## Tocan Invasion ##
  ("banner_136",0,"map_flag_15", banner_scale,0),
  ("bandit_lair",mcn_no_shadow,"map_bandit_lair", 0.45, 0),
  
#-## Outposts begin Tocan
  ("outpost",mcn_no_shadow,"outpost", 0.22,0),
  ("fort_a",mcn_no_shadow,"map_fort_a", 0.22,0),
#-## Outposts end

# LAV MODIFICATIONS START (SIEGE CAMP ICON MINI-MOD)
  ("castle_besieged", mcn_no_shadow, "castle_a_spike_siege_combined", 0.65, 0),
# LAV MODIFICATIONS END (SIEGE CAMP ICON MINI-MOD)
]

# modmerger_start version=201 type=2
try:
    component_name = "map_icons"
    var_set = { "map_icons" : map_icons }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
