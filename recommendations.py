def main():

    difficulty=input("Difficulty or casual?")
    players=input("Multiplayer or Single-player?")

    if difficulty=="Difficulty":
      if players=="Multiplayer":
         recommend("poker")
      elif players=="Single-palyer":
         recommend("klondlike")
      else:
         print("Enter a valid number of players")

    elif difficulty=="Casual":
    
    
      if players=="Multiplayer":
         recommend("Hearts")
      elif players=="Single-player":
         recommend("clock")
    else:
       print("Enter a valid difficulty") 

def recommend(game):
    print("you might like", game)

main()