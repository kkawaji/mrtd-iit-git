# -*- coding: utf-8 -*-
"""
Calendar Problem
--
In this tutorial the goal is to develop an algorithm that can predict the day of the week, give a date.
--
First, try to focus on developing one for just the year 2020.
"""
def calc_this_year(m,d):
    #assume all dates are for 2020
    #since the refence is 1/1/2020, we will define the days of the week as an array beginning with that day
    days = ["Wednedsay", "Thursday", "Friday", "Saturday", "Sunday", "Monday","Tuesday"]
    
    #here we can define each month as a change to the reference date
    mon1 = [0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6] # for example, february is represented with a 3 because 2/1 is 3 days ahead of 1/1
    
    #lets also define a final day being how much has the date changed from 1/1 in days of the week
    final_day = 0
    
    #now we can simply add the days + months value and find the remainder when divided by 7
    final_day = mon1[m-1] + d - 1 # we use m-1 because the reference of the array begins with 0\
    # also subtract by 1 to get the correct index for the day, if the date is 1/1, this will get 0 + 1 - 1 = 0 and the days[0] = Wednesday
    
    final_day = final_day%7 # calculate the remainder that will correspond to the index of the days array
    
    #finally print the day of the week
    return days[final_day]
    
"""
Now try this exercise again, but consider different years.
You will still need to use a similar approach for the month and day, but 
factor how much each year adjusts the day and consider leap years as well as 
century years. Leap years will add a day in february, but century years are 
the same as normal years unless divisible by 400, therefore 2000 was a leap year

The following code will consider dates from future and past.
"""
def calc_day(month,day,year):
    #reference, January 1, 2020 is a Wednesday.
    dow = ["Wednedsay", "Thursday", "Friday", "Saturday", "Sunday", "Monday","Tuesday"]
    #initialize count, similary to final_day
    count = 0
    #consider if the year is future past or present (2020)
    #depending on the year a list of years is created to carefully check each one if it is categorized as a leap year or not
    if year > 2020:
        yr_list = list(range(2020,year+1))
    elif year < 2020:
        yr_list = list(range(year,2021))
    else:
        yr_list = 0
    #next the year lists will go through the for loop to adjust the day change 1 by 1
    #***note there is a difference for future and past years
    #past years will require subtracting days of the week rather than adding
    if year < 2020:
        for y in range(len(yr_list)-1):
            if yr_list[y]%4 == 0:
                count = count - 2
            elif yr_list[y]%4 != 0:
                count = count - 1
            elif yr_list[y]%100 == 0:
                count = count + 1
    elif year > 2020:
        for y in range(len(yr_list)-1):
            if yr_list[y]%4 == 0:
                count = count + 2
            elif yr_list[y]%4 != 0 or year%400 == 0:
                count = count + 1
            elif yr_list[y]%100 == 0:
                count = count - 1
    elif year == 2020:
        count = 0     
    #now we consider the month depending on the classification of the year 
    if year%4 != 0 or year%100 == 0:
        mon = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    elif year%4 == 0 and year%100 !=0:
        mon = [0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
    #finally, take the sum of the count from the years, the change of the month and the day and subtract by 1 for the correct index
    fin_count = count + mon[month-1] + day - 1
    fin_count = fin_count%7
    
    return dow[fin_count]
    
    
