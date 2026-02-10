#A loop can loop can also be used to literate through a list , tuple , string or even dictionary ...

name ="Victoria"

for letter in name:
    if letter =="t":
        print("The is letter t")
    else:
        print(letter)

print("________________")
#below is a list of counties
counties = [ "Nairobi", "Mombasa", "Nakuru","Eldoret","Kajiado", "Machakos","Meru","Embu"]
print(counties)

for county in counties:
    print(county)
search = input("enter county to search")

found = False
for county in counties:
    if county == search:
        found = True 
        break #stop checking once found



print("________________")
if "Meru" in counties:
    print("found")
else:
    print("not found")

print("________________")
#the for can akso be used to literate through a dictionary 
player={
    "name" : "Mbappe",
    "age" :25,
    "teams" : ["PSG", "Monanco" , "France"],
    "nationality" : "French"
}
for key in player:
    print(key)
for values in player:
    print(player[values])
#print (player["name"])

print("----------------")
#  loop thru the teams the player has played for
#print(player["teams"])
 
for team in player["teams"]:
    print(team)
