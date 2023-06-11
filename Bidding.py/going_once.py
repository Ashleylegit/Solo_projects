maxBid = int(input())

while(True):
    bid = int(input())
    if bid > maxBid:
        break

print("Sold:", bid)