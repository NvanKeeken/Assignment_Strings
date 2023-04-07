# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1 of assignment Strings 

# football players that scored
Gullit = "Ruud Gullit"
van_Basten = "Marco van Basten"

# minute that a goal was scored
goal_0 = 32
goal_1 = 54

# report of who scored when 
scorers= Gullit +" "+ str(goal_0)+", " + van_Basten +" "+ str(goal_1)
report = f"{Gullit} scored in the {goal_0}nd minute\n{van_Basten} scored in the {goal_1}th minute"
print(report)

#Part 2 of assignment Strings
player = "Hans van Breukelen"
first_name = player[:player.find(" ")]
last_name_len = len(player[player.find("van"):]) 
name_short = player[0] + ". "+ player[player.find("van"):]
chant = ((first_name+"! ")*(len(first_name)-1)) +(first_name +"!")

# Check if chant does not end with a space 
good_chant = chant[len(chant)-1] != " " 