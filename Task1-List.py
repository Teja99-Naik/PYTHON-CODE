
# Justice League List
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Number of members
print("Number of members:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("Updated team:", justice_league)

# 3. Make Wonder Woman the leader
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Wonder Woman as leader:", justice_league)

# 4. Separate Aquaman and Flash
justice_league.remove("Green Lantern")  # To move
justice_league.insert(justice_league.index("Flash"), "Green Lantern")
print("Conflict resolved:", justice_league)

# 5. Replace team with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New team:", justice_league)

# 6. Sort alphabetically and find new leader
justice_league.sort()
print("Sorted team:", justice_league)
print("New leader:", justice_league[0])