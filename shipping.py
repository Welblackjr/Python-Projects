weight = 4.8 

#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20

elif weight <= 6:
  #more calulations
  cost_ground = weight * 3.0 + 20

elif weight <= 10:
  cost_ground = weight * 4.0 + 20
else:
  cost_ground = weight * 4.75 + 20

print(cost_ground)

cost_ground_premium = 125.00

print ("Ground Shipping Premium $", cost_ground_premium)

#Drone Cost /////////////

if weight <= 2:
  cost_drone = weight * 4.50

if weight <= 6: 
  cost_drone = weight * 9

if weight <= 10:
  cost_drone = weight * 12.50

else: 
  cost_drone = weight * 14.50

cost_drone = "{:.2f}".format(cost_drone)
print("Drone Shipping Price: $" + str(cost_drone) + "\n")

cost_ground = float(cost_ground)
cost_ground_premium = int(cost_ground_premium)
cost_drone = float(cost_drone)

#If Ground cost is less than Premium cost and Drone cost

if cost_ground < cost_ground_premium and cost_ground < cost_drone:
  print("Ground Shipping is the cheapest option.")

#If Premium cost is less than Drone and Ground cost
elif cost_ground_premium < cost_ground and cost_ground_premium < cost_drone: 
  print("Premium Shipping is the cheapest option.")

elif cost_drone < cost_ground and cost_drone < cost_ground_premium:
  print("Drone Shipping is the cheapest option.")
else:
  print("It is your choice to make.")