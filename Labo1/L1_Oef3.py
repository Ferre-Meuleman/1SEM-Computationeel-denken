time = int(input("Give a certan amount of seconds: "))

Days = time // 86400
Mod = time % 86400

Hours = Mod // 3600
Mod = Mod % 3600

Minutes = Mod // 60
Mod = Mod % 60

Seconds = Mod 

print(f"Days: {Days}\nHours: {Hours}\nMinutses: {Minutes}\nSeconds: {Seconds}")