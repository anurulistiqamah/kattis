n = int(input())
winner = []
uw = []

for i in range(n):
    team = input()
    univ, t = team.split()
    if univ not in uw and len(winner)<12:
        winner.append(team)
        uw.append(univ)

print("\n".join(winner))