def main():
    amount_due=50

    while amount_due>0:
        print(f"Amount Due:{amount_due}")
        insert=int(input("Insert Coin: "))

        if insert in [25,10,5]:
            amount_due-=insert
        else :
            print("Something worng")
            
            break

        if amount_due<=0:
           print(f"change Owed: {abs(amount_due)}")    

main()        
