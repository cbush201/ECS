# ECS (Enemy Combat Simulator)
Text-Based RPG Combat using Lark Grammar in Python 3

(1)
  The language I am parsing is the foundations of an english-based RPG combat system that uses regular sentence structure to configure how the player can attack. The grammar consists of 3 different "weapon types", all of which have different properties regarding player damage, mitigation, and even healing. The player can cast spells, mitigate damage and deal it with the 3 base weapons provided. The grammar was created with the intention of making it scalable and easy to upgrade if more features are desired.

(2) 
  An interesting concept to note would be the energy system I implemented. The player has a certain "energy limit" they can view at the start of their turn, which describes how many of their inputted actions will occur. If the player has 1 energy, only one action will happen, but if they have 3, they can chain together 3 attacks in one turn. All of this happens without the program crashing so you can put in more lines than you have energy and it will only execute the amount it can handle. Also, some spells can cost more energy and doing nothing on a turn grants an additional energy because of rest! 

(3)
  In all command lines on VSCode, the program runs seamlessly by typing _python ecs.py_
However, after testing on GitBash on Desktop, the program begins running correctly, and then seems to freeze after the first input is accepted.
I am not sure why this issue is happening.

(4)
How the program runs is up to the user, as the system is dynamic and can be played millions of ways. The structure of commands currently is:
  
Use the "sword/shield/wand" (wand can be followed with "to cast heal/fireball") "to attack/on/to defend" "myself/the enemy".
    
    Some example sentences are:
      Use the sword on the enemy.
      Use the wand to cast heal on myself.
      Use the wand to cast fireball on the enemy.
      Use the shield to attack the enemy.
      Use the shield to defend myself.
      
The most important rule to follow is to keep the U at the start uppercase and to have a period at the end of the sentence. The Program works by separating commands    using the periods so it is important to the function. The program does allow for self-inflicted damage, but there is no benefit to it. It could be used later for      some macabre systems but for now it will only lead to death.

