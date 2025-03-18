from MHWildsArmorOptimizer.classes import *


# Skills
WEX = Skill(name="Weakness Exploit", aff_buffs=[0.05, 0.1, 0.15, 0.2, 0.3])
AGI = Skill(name="Agitator", atk_buffs=[4, 8, 12, 16, 20], aff_buffs=[0.03, 0.05, 0.07, 0.1, 0.15], uptime=0.8)
MM = Skill(name="Maximum Might", aff_buffs=[0.1, 0.2, 0.3])
BR = Skill(name="Burst", atk_buffs=[5])
CS = Skill(name="Counterstrike", atk_buffs=[10, 15, 25], uptime=0.5)
LP = Skill(name="Latent Power", uptime=0.5)
Dosha = Skill(name="Doshaguma's Might", atk_buffs=[0, 10, 10, 25])
Ebony = Skill(name="Ebony Odogaron's Power", atk_buffs=[0, 3, 3, 10])
Fulgar = Skill(name="Fulgur Anjanath's Will")
Dahaad = Skill(name="Jin Dahaad's Revolt")
Gore = Skill(name="Gore Magala's Tyranny")
Arkveld = Skill(name="Arkveld's Hunger")
GArkveld = Skill(name="G. Arkveld's Vitality")


# Decorations
Tenderizer = Decoration(name="Tenderizer", lvl=3, skills={WEX: 1})
Challenger = Decoration(name="Challenger", lvl=3, skills={AGI: 1})
Mighty = Decoration(name="Mighty", lvl=2, skills={MM: 1})
Chain = Decoration(name="Chain", lvl=3, skills={BR: 1})


# Armors
Doshaguma_Mail_B = Armor(name="Doshaguma Mail B", slots=[3, 0, 0], skills={Dosha: 1}, part='mail')
Doshaguma_Coil_B = Armor(name="Doshaguma Coil B", slots=[0, 2, 0], skills={Dosha: 1}, part='coil')
Doshaguma_Greaves_B = Armor(name="Doshaguma Greaves B", slots=[2, 1, 0], skills={Dosha: 1}, part='greaves')

G_Doshaguma_Helm_B = Armor(name="G. Doshaguma Helm B", slots=[1, 2, 0], skills={Dosha: 1}, part='helm')
G_Doshaguma_Mail_B = Armor(name="G. Doshaguma Mail B", slots=[0, 2, 0], skills={Dosha: 1}, part='mail')
G_Doshaguma_Braces_B = Armor(name="G. Doshaguma Braces B", slots=[1, 2, 0], skills={Dosha: 1}, part='braces')

Arkvulcan_Helm_B = Armor(name="Arkvulcan Helm B", slots=[1, 1, 1], skills={Arkveld: 1}, part='helm')
Arkvulcan_Mail_B = Armor(name="Arkvulcan Mail B", slots=[0, 1, 1], skills={Arkveld: 1, WEX: 1}, part='mail')
Arkvulcan_Braces_B = Armor(name="Arkvulcan Braces B", slots=[1, 2, 0], skills={Arkveld: 1}, part='braces')
Arkvulcan_Coil_B = Armor(name="Arkvulcan Coil B", slots=[2, 0, 0], skills={Arkveld: 1, WEX: 2}, part='coil')
Arkvulcan_Greaves_B = Armor(name="Arkvulcan Greaves B", slots=[1, 0, 1], skills={Arkveld: 1}, part='greaves')

G_Arkveld_Helm_B = Armor(name="G. Arkveld Helm B", slots=[1, 0, 1], skills={GArkveld: 1}, part='helm')
G_Arkveld_Mail_B = Armor(name="G. Arkveld Mail B", slots=[0, 0, 1], skills={GArkveld: 1}, part='mail')
G_Arkveld_Braces_B = Armor(name="G. Arkveld Braces B", slots=[3, 0, 0], skills={GArkveld: 1, WEX: 2}, part='braces')
G_Arkveld_Coil_B = Armor(name="G. Arkveld Coil B", slots=[1, 1, 0], skills={GArkveld: 1}, part='coil')
G_Arkveld_Greaves_B = Armor(name="G. Arkveld Greaves B", slots=[1, 1, 0], skills={GArkveld: 1, WEX: 1}, part='greaves')

G_Rathalos_Helm_B = Armor(name="G. Rathalos Helm B", slots=[0, 2, 0], skills={WEX: 1}, part='helm')
G_Rathalos_Braces_B = Armor(name="G. Rathalos Braces B", slots=[2, 1, 0], skills={WEX: 1}, part='braces')

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
G_Ebony_Mail_B = Armor(name="G. Ebony Mail B", slots=[0, 2, 0], skills={Ebony: 1}, part='mail')
G_Ebony_Braces_B = Armor(name="G. Ebony Braces B", slots=[1, 1, 0], skills={Ebony: 1, BR: 1}, part='braces')
G_Ebony_Coil_B = Armor(name="G. Ebony Coil B", slots=[1, 1, 0], skills={Ebony: 1, BR: 1}, part='coil')
G_Ebony_Greaves_B = Armor(name="G. Ebony Greaves B", slots=[1, 1, 0], skills={Ebony: 1}, part='greaves')


# Charms
Challenger_Charm_II = Armor(name="Challenger Charm II", skills={AGI: 2}, part='charm')
Exploiter_Charm_II = Armor(name="Exploiter Charm II", skills={WEX: 2}, part='charm')
Mighty_Charm_II = Armor(name="Mighty Charm II", skills={MM: 2}, part='charm')
Chain_Charm_II = Armor(name="Chain Charm II", skills={BR: 2}, part='charm')
Counter_Charm_III = Armor(name="Counter Charm III", skills={CS: 3}, part='charm')
