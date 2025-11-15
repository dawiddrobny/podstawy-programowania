facebook = True
twitter = False
instagram = True

if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):
    print("You are a good influencer!")
else:
    print("You are not a good influencer!")
