### Background
Week 1 of the Metis Data Science Bootcamp is in the books! Our first project was a group one, in which we were tasked with mining NYC MTA Turnstile data to recommend optimal deployment of a Tech organization's volunteers. The organization wished to maximize mailing list sign-ups, promote their upcoming gala, and solicit potential donors. We were free to use other datasets.

### Team Members

I need to start off by recognizing my team: Brenner Heintz, Hiranya Kumar, and Luke Tibbott. Our collective ideas, feedback, and efforts made a better final product than I would have been able to produce on my own. It was a pleasure to work with them.

### Data:
- [MTA Turnstile Data](http://web.mta.info/developers/turnstile.html)
- 

### MTA Data Cleaning

We started off by downloading one dataset from the [MTA website](link) and importing it into python using a csv reader. A scan of the dataframe revealed an issue with the naming of the 'EXITS' column (it contained extra whitespace -- easily removed with `str.strip()`. This may seem like a small detail, but I mention it because review of imported data is an essential part of data munging. 

The entry and exit data are given as a series of counter values every 4 hours, *usually* (but not always...see below) at 0:00, 4:00, 8:00, etc. Thus, to get the actual number of entries and exits, we needed to calculate the difference between consecutive rows for a given station's turnstile. 

-IMAGE OF RAW DATA?

Anytime you apply a function to a dataframe, it's a good idea to check that it performed as intended. Reviewing the basic stats of the resulting 'ENTRY_DIFFS' column (or examining a distribution of the values) revealed some very large and some negative values. Examining the large-magnitude differences revealed that they appeared to be due to a resetting of the counter:

-IMAGE OF COUNTER RESET

We chose to filter these outliers out of our dataset. (One of our instructors later mentioned that some turnstile's counters appeared to be counting down instead of up -- so one could simply invert their negative numbers and obtain reasonable data. There are always choices like this to be made in cleaning data.)

### EDA

Now we have entries and exits per 4-hour time period for each turnstile. Where to go next?
- Compute total traffic (entries + exits)
- Group by Station
- Sum over day
- Group by weekday 
