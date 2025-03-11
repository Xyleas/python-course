country_name = "Australia"
population = 25000000
landlocked = False
border_size = 60000.256

health = 100
damage = 20
heal = 50
buff = 1.5
curse = 2

health = health - damage
print(health)

health = health + heal
print(health)

health = health * 1.5
health = health / 2

# We can also...

health += heal
health -= damage
health *= buff
health /= curse

print(health)