from classes import *
from config import *


# Skills
WEX = Skill(name="Weakness Exploit", aff_buffs=[0.05, 0.1, 0.15, 0.2, 0.3])
AGI = Skill(name="Agitator", atk_buffs=[4, 8, 12, 16, 20], aff_buffs=[0.03, 0.05, 0.07, 0.1, 0.15], uptime=UPTIMES['AGI'])
MM = Skill(name="Maximum Might", aff_buffs=[0.1, 0.2, 0.3], uptime=UPTIMES['MM'])
MM_Fulgur = Skill(name="Maximum Might", aff_buffs=[0.1, 0.2, 0.3])
BR = Skill(name="Burst", atk_buffs=[5]) # for GS
CS = Skill(name="Counterstrike", atk_buffs=[10, 15, 25], uptime=UPTIMES['CS'])
LP = Skill(name="Latent Power", aff_buffs=[0.1, 0.2, 0.3, 0.4, 0.5], uptime=UPTIMES['LP'])
LP_Rey_I = Skill(name="Latent Power", aff_buffs=[0.1, 0.2, 0.3, 0.4, 0.5], uptime=UPTIMES['LP_Rey_I'])
LP_Rey_II = Skill(name="Latent Power", aff_buffs=[0.1, 0.2, 0.3, 0.4, 0.5], uptime=UPTIMES['LP_Rey_II'])
EE = Skill(name="Evade Extender")
FLAY = Skill(name="Flayer")
AV = Skill(name="Antivirus")
EP = Skill(name="Earplugs")
Dosha = Skill(name="Doshaguma's Might", atk_buffs=[0, 10, 10, 25], uptime=UPTIMES['Dosha'])
Ebony = Skill(name="Ebony Odogaron's Power", atk_buffs=[0, 3, 3, 10])
Fulgur = Skill(name="Fulgur Anjanath's Will", replace=[None, (MM, MM_Fulgur)])
Dahaad = Skill(name="Jin Dahaad's Revolt")
Arkveld = Skill(name="Arkveld's Hunger")
GArkveld = Skill(name="G. Arkveld's Vitality")
Udra = Skill(name="Nu Udra's Mutiny")
Rey = Skill(name="Rey Dau's Voltage", replace=[None, (LP, LP_Rey_I), (LP, LP_Rey_I), (LP, LP_Rey_II)])
Zoh = Skill(name="Zoh Shia's Pulse")
Gore = Skill(name="Gore Magala's Tyranny", uptime_buffs_lst_lst=[
    [(1, 0, 0)], 
    [(UPTIMES['Gore'], 0, 0.25), (1 - UPTIMES['Gore'], 0, 0)], # lvl 2
    [(UPTIMES['Gore'], 0, 0.25), (1 - UPTIMES['Gore'], 0, 0)], 
    [(UPTIMES['Gore'], 15, 0.25), (1 - UPTIMES['Gore'], 10, 0)], # lvl 4
]) # Assuming antivirus already taken into account


# Decorations
Tenderizer = Decoration(name="Tenderizer", lvl=3, skills={WEX: 1})
Challenger = Decoration(name="Challenger", lvl=3, skills={AGI: 1})
Mighty = Decoration(name="Mighty", lvl=2, skills={MM: 1})
Chain = Decoration(name="Chain", lvl=3, skills={BR: 1})
Counter = Decoration(name="Counter", lvl=2, skills={CS: 1})
Throttle = Decoration(name="Throttle", lvl=3, skills={LP: 1})
# Flayer = Decoration(name="Flayer", lvl=3, skills={FLAY: 1})
# Sane = Decoration(name="Sane", lvl=1, skills={AV: 1})
Earplugs = Decoration(name="Earplugs", lvl=2, skills={EP: 1})


# Armors
Doshaguma_Coil_A = Armor(name="Doshaguma Coil A", slots=[1, 0, 0], skills={Dosha: 1, LP:2}, part='coil')

Doshaguma_Mail_B = Armor(name="Doshaguma Mail B", slots=[3, 0, 0], skills={Dosha: 1, LP:1}, part='mail')
Doshaguma_Coil_B = Armor(name="Doshaguma Coil B", slots=[0, 2, 0], skills={Dosha: 1, LP:1}, part='coil')
Doshaguma_Greaves_B = Armor(name="Doshaguma Greaves B", slots=[2, 1, 0], skills={Dosha: 1}, part='greaves')

G_Doshaguma_Helm_B = Armor(name="G. Doshaguma Helm B", slots=[1, 2, 0], skills={Dosha: 1}, part='helm')
G_Doshaguma_Mail_B = Armor(name="G. Doshaguma Mail B", slots=[0, 2, 0], skills={Dosha: 1}, part='mail')
G_Doshaguma_Braces_B = Armor(name="G. Doshaguma Braces B", slots=[1, 2, 0], skills={Dosha: 1}, part='braces')

Arkvulcan_Helm_B = Armor(name="Arkvulcan Helm B", slots=[1, 1, 1], skills={Arkveld: 1}, part='helm')
Arkvulcan_Mail_B = Armor(name="Arkvulcan Mail B", slots=[0, 1, 1], skills={Arkveld: 1, WEX: 1}, part='mail')
Arkvulcan_Braces_B = Armor(name="Arkvulcan Braces B", slots=[1, 2, 0], skills={Arkveld: 1}, part='braces')
Arkvulcan_Coil_B = Armor(name="Arkvulcan Coil B", slots=[2, 0, 0], skills={Arkveld: 1, WEX: 2}, part='coil')
Arkvulcan_Greaves_B = Armor(name="Arkvulcan Greaves B", slots=[1, 0, 1], skills={Arkveld: 1}, part='greaves')

G_Arkveld_Helm_B = Armor(name="G. Arkveld Helm B", slots=[1, 0, 1], skills={GArkveld: 1, FLAY: 1}, part='helm')
G_Arkveld_Mail_B = Armor(name="G. Arkveld Mail B", slots=[0, 0, 1], skills={GArkveld: 1, FLAY: 1}, part='mail')
G_Arkveld_Braces_B = Armor(name="G. Arkveld Braces B", slots=[3, 0, 0], skills={GArkveld: 1, WEX: 2}, part='braces')
G_Arkveld_Coil_B = Armor(name="G. Arkveld Coil B", slots=[1, 1, 0], skills={GArkveld: 1, FLAY: 2}, part='coil')
G_Arkveld_Greaves_B = Armor(name="G. Arkveld Greaves B", slots=[1, 1, 0], skills={GArkveld: 1, WEX: 1}, part='greaves')

# G_Rathalos_Helm_B = Armor(name="G. Rathalos Helm B", slots=[0, 2, 0], skills={WEX: 1}, part='helm')
# G_Rathalos_Braces_B = Armor(name="G. Rathalos Braces B", slots=[2, 1, 0], skills={WEX: 1}, part='braces')

G_Fulgur_Braces_A = Armor(name="G. Fulgur Braces A", slots=[1, 0, 0], skills={Fulgur: 1, AGI: 1, MM: 1}, part='braces')
G_Fulgur_Coil_A = Armor(name="G. Fulgur Coil A", slots=[2, 0, 0], skills={Fulgur: 1, MM: 1}, part='coil')

G_Fulgur_Helm_B = Armor(name="G. Fulgur Helm B", slots=[0, 1, 0], skills={Fulgur: 1, AGI: 2}, part='helm')
G_Fulgur_Mail_B = Armor(name="G. Fulgur Mail B", slots=[2, 1, 0], skills={Fulgur: 1, MM: 1}, part='mail')
G_Fulgur_Braces_B = Armor(name="G. Fulgur Braces B", slots=[0, 2, 0], skills={Fulgur: 1, MM: 1}, part='braces')
G_Fulgur_Coil_B = Armor(name="G. Fulgur Coil B", slots=[0, 2, 0], skills={Fulgur: 1}, part='coil')
G_Fulgur_Greaves_B = Armor(name="G. Fulgur Greaves B", slots=[1, 1, 0], skills={Fulgur: 1}, part='greaves')

Dahaad_Helm_A = Armor(name="Dahaad Shardhelm A", slots=[1, 0, 0], skills={Dahaad: 1, AGI: 1, WEX: 1}, part='helm')
Dahaad_Braces_A = Armor(name="Dahaad Shardbraces A", skills={Dahaad: 1, AGI: 2}, part='braces')

Dahaad_Helm_B = Armor(name="Dahaad Shardhelm B", slots=[0, 2, 0], skills={Dahaad: 1, AGI: 1}, part='helm')
Dahaad_Mail_B = Armor(name="Dahaad Shardmail B", slots=[0, 1, 1], skills={Dahaad: 1}, part='mail')
Dahaad_Braces_B = Armor(name="Dahaad Shardbraces B", slots=[0, 0, 1], skills={Dahaad: 1, AGI: 1}, part='braces')
Dahaad_Coil_B = Armor(name="Dahaad Shardcoil B", slots=[3, 0, 0], skills={Dahaad: 1, WEX: 1}, part='coil')
Dahaad_Greaves_B = Armor(name="Dahaad Shardgreaves B", slots=[0, 1, 0], skills={Dahaad: 1, AGI: 2}, part='greaves')

G_Ebony_Braces_A = Armor(name="G. Ebony Braces A", skills={Ebony: 1, BR: 2}, part='braces')

G_Ebony_Helm_B = Armor(name="G. Ebony Helm B", slots=[0, 1, 0], skills={Ebony: 1, BR: 2}, part='helm')
G_Ebony_Mail_B = Armor(name="G. Ebony Mail B", slots=[0, 2, 0], skills={Ebony: 1, EP: 1}, part='mail')
G_Ebony_Braces_B = Armor(name="G. Ebony Braces B", slots=[1, 1, 0], skills={Ebony: 1, BR: 1}, part='braces')
G_Ebony_Coil_B = Armor(name="G. Ebony Coil B", slots=[1, 1, 0], skills={Ebony: 1, BR: 1}, part='coil')
G_Ebony_Greaves_B = Armor(name="G. Ebony Greaves B", slots=[1, 1, 0], skills={Ebony: 1, EP: 1}, part='greaves')

# Udra_Mail_A = Armor(name="Udra Miremail A", slots=[2, 0, 0], skills={Udra: 1, BR: 1}, part='mail')
# Udra_Braces_A = Armor(name="Udra Mirebraces A", slots=[0, 1, 0], skills={Udra: 1, CS: 2}, part='braces')

# Udra_Helm_B = Armor(name="Udra Mirehelm B", slots=[0, 2, 0], skills={Udra: 1, CS: 1}, part='helm')
# Udra_Braces_B = Armor(name="Udra Mirebraces B", slots=[1, 0, 1], skills={Udra: 1, CS: 1}, part='braces')
# Udra_Greaves_B = Armor(name="Udra Miregreaves B", slots=[1, 0, 1], skills={Udra: 1, BR: 1}, part='greaves')

# Dragonking_A = Armor(name="Dragonking Eyepatch A", skills={CS: 3}, part='helm')

Blango_Mail_B = Armor(name="Blango Mail B", slots=[0, 1, 0], skills={AGI: 2}, part='mail')
Blango_Coil_B = Armor(name="Blango Coil B", slots=[2, 0, 0], skills={AGI: 2}, part='coil')
Blango_Greaves_B = Armor(name="Blango Greaves B", slots=[0, 2, 0], skills={AGI: 1}, part='greaves')

Rey_Greaves_A = Armor(name="Rey Sandgreaves A", slots=[0, 0, 1], skills={Rey: 1, MM: 1, LP: 1}, part='greaves')

Rey_Helm_B = Armor(name="Rey Sandhelm B", slots=[0, 0, 1], skills={Rey: 1, LP: 1, EE: 1}, part='helm')
Rey_Braces_B = Armor(name="Rey Sandbraces B", slots=[0, 0, 1], skills={Rey: 1, LP: 2}, part='braces')
Rey_Greaves_B = Armor(name="Rey Sandgreaves B", slots=[2, 0, 1], skills={Rey: 1, LP: 1}, part='greaves')

# Azuz_Helm_A = Armor(name="Azuz Headdress A", slots=[0, 1, 0], skills={MM: 2}, part='helm')

Numinous_Mail_A = Armor(name="Numinous Shroud A", slots=[1, 0, 0], skills={Zoh: 1, AGI: 2, CS: 1}, part='mail')
Numinous_Greaves_A = Armor(name="Numinous Greaves A", slots=[1, 1, 0], skills={Zoh: 1, CS: 2}, part='greaves')

Numinous_Helm_B = Armor(name="Numinous Crown B", slots=[1, 1, 1], skills={Zoh: 1, AGI: 1}, part='helm')
Numinous_Mail_B = Armor(name="Numinous Shroud B", slots=[0, 0, 1], skills={Zoh: 1, AGI: 2}, part='mail')
Numinous_Coil_B = Armor(name="Numinous Overlay B", slots=[0, 1, 0], skills={Zoh: 1, AGI: 2}, part='coil')
Numinous_Greaves_B = Armor(name="Numinous Greaves B", slots=[0, 1, 1], skills={Zoh: 1, CS: 1}, part='greaves')

Gore_Mail_A = Armor(name="Gore Mail A", slots=[0, 0, 1], skills={Gore: 1, AV: 1}, part='mail')

Gore_Helm_B = Armor(name="Gore Helm B", slots=[1, 0, 1], skills={Gore: 1}, part='helm')
Gore_Braces_B = Armor(name="Gore Vambraces B", slots=[0, 2, 0], skills={Gore: 1}, part='braces')
Gore_Coil_B = Armor(name="Gore Coil B", slots=[0, 1, 1], skills={Gore: 1}, part='coil')
Gore_Greaves_B = Armor(name="Gore Greaves B", slots=[2, 0, 1], skills={Gore: 1, AV: 1}, part='greaves')

Rey_Helm_Y = Armor(name="Rey Sandhelm Y", slots=[0, 0, 1], skills={Rey: 1, MM: 1, WEX: 1}, part='helm')
Rey_Mail_Y = Armor(name="Rey Sandmail Y", slots=[1, 0, 0], skills={Rey: 1, LP: 3}, part='mail')
Rey_Braces_Y = Armor(name="Rey Sandbraces Y", slots=[0, 0, 2], skills={Rey: 1, EE: 2}, part='braces')
Rey_Coil_Y = Armor(name="Rey Sandcoil Y", skills={Rey: 1, MM: 2, LP: 2}, part='coil')


# Charms
Challenger_Charm_II = Armor(name="Challenger Charm II", skills={AGI: 2}, part='charm')
Exploiter_Charm_II = Armor(name="Exploiter Charm II", skills={WEX: 2}, part='charm')
Mighty_Charm_II = Armor(name="Mighty Charm II", skills={MM: 2}, part='charm')
Chain_Charm_II = Armor(name="Chain Charm II", skills={BR: 2}, part='charm')
Counter_Charm_III = Armor(name="Counter Charm III", skills={CS: 3}, part='charm')
Earplugs_Charm_II = Armor(name="Earplugs Charm II", skills={EP: 2}, part='charm')
