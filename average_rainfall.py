def average_rainfall():
    # Get the number of years
    num_years = int(input("How many years of rainfall data do you want to include in the average calculation: "))
    
    total_months = num_years * 12
    total_rainfall = 0
    
    # Outer loop for years
    for year in range(1, num_years + 1):
        print(f"\nYear {year}")
        
        # Inner loop for mon2ths
        for month in range(1, 13):
            rainfall = float(input(f"Enter inches of rainfall for month {month}: "))
            total_rainfall += rainfall
    
    # Calculate average rainfall
    average_rainfall = total_rainfall / total_months
    
    # Display results
    print(f"\nNumber of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")

if __name__ == "__main__":
   average_rainfall()
