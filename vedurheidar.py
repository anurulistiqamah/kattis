wind_speed = int(input())
road_count = int(input())

for _ in range(road_count):
    name, speed = input().split()
    if int(speed) < wind_speed: print(name, 'lokud')
    else: print(name, 'opin')