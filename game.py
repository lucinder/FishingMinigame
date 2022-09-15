embed
-title "It's Fishin' Time!"
{{r1=roll("1d100")}}
{{r2=(roll("1d10000")-1)/10000.0}}
{{r3=roll("1d100")}}
Rolling 3d100: {{r1}}, {{floor(100.0*r2)+1}}, {{r3}}
<drac2>
wminimizer = 30.0
lminimizer = 10.0
invnorm = load_json(get_gvar("9769d7c8-cd08-4f48-83fc-d4d67fe8d1d0"))
fishdb = load_json(get_gvar("468de876-7b3a-414e-bdff-5de7669c1913"))
c_p = []
c_e = []
c_w = []
c_c = []
c_r = []
c_f = []
u_p = []
u_e = []
u_w = []
u_c = []
u_r = []
u_f = []
r_p = []
r_e = []
r_w = []
r_c = []
r_r = []
r_f = []
l_p = []
l_e = []
l_w = []
l_c = []
l_r = []
l_f = []
for fish in fishdb:
   lists = {
      "polar" : { "Common" : c_p, "Uncommon" : u_p, "Rare" : r_p, "Legendary" : l_p },
      "east" : { "Common" : c_e, "Uncommon" : u_e, "Rare" : r_e, "Legendary" : l_e },
      "west" : { "Common" : c_w, "Uncommon" : u_w, "Rare" : r_w, "Legendary" : l_w },
      "central" : { "Common" : c_c, "Uncommon" : u_c, "Rare" : r_c, "Legendary" : l_c },
      "reef" : { "Common" : c_r, "Uncommon" : u_r, "Rare" : r_r, "Legendary" : l_r },
      "freshwater" : { "Common" : c_f, "Uncommon" : u_f, "Rare" : r_f, "Legendary" : l_f }
   }
   for biome in fish["biomes"]:
      lists[biome][fish["rarity"]].append(fish)
def getWeight(fish, n):
   weight = fish["avgwgt"]
   maxweight = fish["maxwgt"]
   zscore = invnorm[str(n)]
   if(zscore >= 0):
      return weight + zscore*((maxweight-weight)/2.0)
   return weight + (zscore*((maxweight-weight)/2.0))/wminimizer
def getLength(fish, n):
   length = fish["avglen"]
   maxlength = fish["maxlen"]
   zscore = invnorm[str(n)]
   if(zscore >= 0):
      return length + zscore*((maxlength-length)/2.0)
   return length + (zscore*((maxlength-length)/2.0))/lminimizer
def rarityToIndex(rarity):
   if(rarity>96):
      return 0
   elif(rarity>88):
      return 1
   elif(rarity>66):
      return 2
   return 3
def getfish(area, fishrarity, fishno):
   if(not(area in ["polar","west","east","central","freshwater","reef"])):
      return "Error: invalid location argument."
   fishlist = {
       'west': (l_w, r_w, u_w, c_w),
       'east': (l_e, r_e, u_e, c_e),
       'polar': (l_p, r_p, u_p, c_p),
       'central': (l_c, r_c, u_c, c_c),
       'reef': (l_r, r_r, u_r, c_r),
       'freshwater': (l_f, r_f, u_f, c_f)
   }[area][rarityToIndex(fishrarity)]
   return fishlist[int(len(fishlist)*fishno)]
def printfishdetails(fish):
   if(fish == "Error: invalid location argument."):
      return fish
   out = ""
   out += "You caught a **" + fish["name"] + "**!\n"
   fishwgt = getWeight(fish,r3)
   fishlen = getLength(fish,r3)
   if(fishwgt >= 1000):
      out += "Weight: " + round(fishwgt/1000.0,2) + " kg.\n"
   else:
      out += "Weight: " + round(fishwgt,2) + " g.\n"
   if(fishlen >= 100):
      out += "Length: " + round(fishlen/100.0,2) + " m.\n"
   else:
      out += "Length: " + round(fishlen,2) + " cm.\n"
   if(r1 > 96):
      out += "*Legendary catch!*\n"
   if(r3 > 97):
      out += "*World Record catch!*\n"
   return out;
</drac2>
{{fishresult = getfish(f'%1%', r1, r2)}}
-f "Fishing Results|{{printfishdetails(fishresult)}}"
-thumb {{fishresult["image"] if not(fishresult == "Error: invalid location argument.") else ""}}
-footer "Fishin' With The Boys: an Avrae fishing minigame by Lucinder"
