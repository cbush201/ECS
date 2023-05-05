from lark import Lark
import math

#Player Values
playerHealth = 20
energy = 1

#Enemy Values
enemyHealth = 25
enemyDamage = -2

#Equipment Values
sworddmg = -2
fireballdmg = -4
wanddmg = -1
shielddmg = -1
healdmg = 2

grammar = """
    start: action+

    action: (attack | defend) "." 

    attack: equipment_choice verb "the enemy"
    defend: equipment_choice verb "myself"

    equipment_choice: "Use the" equipment

    equipment: sword | shield | wand 

    wand: "wand" spell
    sword: "sword"
    shield: "shield"
    
    spell: "to cast" (fireball | heal)
    fireball: "fireball"
    heal: "heal"
    verb: "to attack" | "on" | "to defend"

    %import common.WS
    %ignore WS
"""

parser = Lark(grammar)

def dealdmg(target, source):
    global enemyHealth
    global playerHealth

    if "enemy" in target:
        enemyHealth += source
    elif "player" in target:
        playerHealth += source
    return

def castSpell(target, spell):
    global energy
    if (spell == "fireball"):
        if energy >= 2:
            energy -= 1
            dealdmg(target, fireballdmg)
            print("Dealt " + str(fireballdmg) + " damage to the " + target + "!")
        else:
            print("Not enough energy to cast fireball (Requires 2 Energy).")
        return
    elif(spell == "heal"):
        dealdmg(target, healdmg)
        energy += 2
        print("Healed " + target + " for " + str(healdmg) + " health! Gained 1 energy!")
        return
    return

def getAttack(listOfTraits):
    mode = listOfTraits[0]
    equip = listOfTraits[1]
    spell = listOfTraits[2]

    if mode == "attack":
        if equip == "sword":
            dealdmg("enemy", sworddmg)
        elif equip == "shield":
            dealdmg("enemy", shielddmg)
        elif equip == "wand":
            dealdmg("enemy", 0)
        if spell == "fireball":
            castSpell("enemy", "fireball")  
    elif mode == "defend":
        if equip == "sword":
            dealdmg("enemy", 1)
        elif equip == "shield":
            dealdmg("player", -shielddmg)
        elif equip == "wand":
            dealdmg("enemy", 0)
        if spell == "heal":
            castSpell("player", "heal")


#Reads the Tree
def evaluate_action(tree, mo, eq, sp):
    m = mo
    e = eq
    s = sp
    if len(tree.children) <= 0:
        return
    for child in tree.children:
        dat = child.data
        if dat == 'attack':
            m = "attack"
        elif dat == 'defend':
            m = "defend"
        elif dat == 'sword':
            e = "sword"
        elif dat == 'shield':
            e = "shield"
        elif dat == 'wand':
            e = "wand"
        elif dat == 'fireball':
            s = "fireball"
        elif dat == 'heal':
            s = "heal"
        evaluate_action(child, m, e, s)
        
    

    getAttack([m, e, s])
    return 


#Game Flow and Input Cycle
def fight_enemy():
    global energy
    global playerHealth
    global enemyHealth
    global enemyDamage

    print("\nYou've encountered an enemy! You have the first attack.")
    print("You have the following: \nWeapons       Spells\nSword         Fireball \nShield        Heal \nWand")
    while enemyHealth > 0 and playerHealth > 0:
        #Resets energy to 1 if all was expended previously
        if energy == 0:
            energy = 1

        print("\nEnter your action(s). You have " + str(energy) + " energy.")
        
        inputs = input()
        actions = inputs.split(".")

        #Will complete # of actions based on energy remaining.
        actionnum = 0
        for act in actions:
            if len(actions) == 1:
                energy += 1
                break
            if act == "":
                break
            act += "."
            if (energy > 0):
                tree = parser.parse(act)
                evaluate_action(tree, "", "", "")
                energy -= 1
                actionnum += 1
            else:
                break
                

        #Enemy damage inflicted (Additional damage based on energy expended)
        damagedealt = enemyDamage
        if math.floor(actionnum / 2) > 0:
            damagedealt *= math.ceil(actionnum / 2)
         
        dealdmg("player", damagedealt)
        print("Enemy did " + str(damagedealt) + " damage!")
        print("Current Health: " + str(playerHealth) + "\nEnemy Health: " + str(enemyHealth))

    if playerHealth <= 0:
        print("You have died!")
        return
    
    if enemyHealth <= 0:
        print("You have killed the enemy! Congratulations")
        return
    
    return

fight_enemy()