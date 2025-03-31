team = {'name': 'shahre_khodro', 'result':  'wwwldwwwdwlllddwdwlwlwwdldddl'}
	
win_msg = f"win: {team['result'].count('w')}".ljust(10)
lose_msg = f"lost: {team['result'].count('l')}".ljust(10)
draw_msg = f"draw: {team['result'].count('d')}".ljust(10)
team_name = f'name: {team["name"]}'.ljust(20)
# print (type(win_msg))
print(team_name + win_msg + draw_msg + lose_msg)
print(team_name , win_msg , draw_msg , lose_msg)
a='11'
b='22'
print (a+b)
print (a,b)
