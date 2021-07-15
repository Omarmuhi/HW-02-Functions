Enter_miles_driven: 150
Enter_gallons_of_gas_used: 15
Enter_cost_per_gallon: 3

Miles_Per_Gallon: 10.0
Total_Gas_Cost: 45.0
Cost_Per_Mile: 0.3
#reading inputs
miles_driven=float(input('Enter miles driven:\t\t\t'))
gallons_gas_used=float(input('Enter gallons of gas used:\t'))
cost_per_gallon=float(input('Enter cost per gallon:\t\t'))
print() #line break

#finding miles_per_gallon, rounding to 1 decimal place
miles_per_gallon=round(miles_driven/gallons_gas_used,1)
#finding total_gas_cost, rounding to 1 decimal place
total_gas_cost=round(gallons_gas_used*cost_per_gallon,1)
#finding cost_per_mile, rounding to 1 decimal place
cost_per_mile=round(total_gas_cost/miles_driven,1)

#displayiing everything as per the given output format
print('Miles Per Gallon:\t',miles_per_gallon)
print('Total Gas Cost:\t\t',total_gas_cost)
print('Cost Per Mile:\t\t',cost_per_mile)

