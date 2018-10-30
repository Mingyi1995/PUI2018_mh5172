*Citibike Project review by fb55*

*Hypothesis Formulation* Please review carefully

your Null hypiothesis should be the opposite of your idea or theory. If you suspect that younger people are more likely to commute then your H0 should be that they are less or equally likely to. 

People younger than 30-years-old are *more likely than others to choose biking for commuting* 
you should add here: "assuming that weekday citibike usage is more likely to be related to commuting than weekend citibike usare I will compare the fraction of users under and over 30 in weekdays and weekends."


Correct NULL HYPOTHESIS:
The proportion of people younger than 30-years-old biking on weekdays is the **same or LOWER** than the proportion of people older than 30-years-old biking on weekdays

You copied and pasted a lot of lines from my code but I am not sure you understand them. YOur measurables sould be frations, and they should be compared between younger and older population
You did not define your symbols. Assuming that y is the users <30 yo
your formula for the Null hypothesis 

```
H0: y_weekdays / y_anyDay <= o_weekdays / o_anydays
```

or 

```
H0: y_weekend / y_anyDay >= o_weekend / o_anyDay
```

*Data preparation* Please redo this

your data does not support the investigation yet. You need to
1) separate the population > 30 from < 30
2) aggregate the day by day of the week putting together Saturdays and Sundays, and 
3) separately aggregate all days (Mon-Sun). 
4) then take the ratio for each age group of the two aggregate counts (Y_weekends / Y old, and O_weekends / O _old) 

this data would support the testing of the null

the relative final (or single in your case) plot could be a histogram with 2 bins, one for old one for young showing the fraction of weekend and the total rides count

*Test*

Because you are choosing to compare proportions you can use the same tests you used in the "Hard to Employ" exercise: chisquare for proportions or z test

Please review your hypothesis and reprocess your data before you can proceed to the next phase (implementing the test)


