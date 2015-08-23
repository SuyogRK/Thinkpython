r = 5 
pi = 3.14
vol_sphere = (4 * pi * r**3) /3
print vol_sphere
print "\n"




book_price = 24.95
discount = 40
copies_amount = 60
shipping_cost = 3 + ((copies_amount - 1) * 0.75)
book_cost = book_price -((discount * book_price) / 100)

total_cost = copies_amount* book_cost + shipping_cost

wholesale_price = total_cost / copies_amount
print "copies amount", copies_amount
print "shipping cost", shipping_cost
print "book cost", book_cost
print "total cost", total_cost
print "wholesale price", wholesale_price
print "\n"




leave_time = 6*60 + 52
print "leave time in minutes", leave_time
easy_pace = 8 + 15/60.0
print "easy pace in minutes",easy_pace
tempo_pace = 7  + 12/60.0
print "tempo pace in seconds", tempo_pace
run_total = easy_pace + 3 * tempo_pace + easy_pace
print "total time run",run_total ,"minutes"
time_arrived = leave_time + run_total
print "time arrived is",time_arrived
time_hour = int(time_arrived/60)
time_min = (time_arrived/60 -time_hour)* 60
time_sec= (time_min -int(time_min))*60

print "time arrived " , time_hour,"hours",int(time_min),"minutes",time_sec,"seconds"