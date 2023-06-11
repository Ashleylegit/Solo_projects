maxBid = int(input())

while(True):
    bid = int(input())
    if bid > maxBid:
        break

print("Sold:", bid)
#This code is designed to do a bidding process