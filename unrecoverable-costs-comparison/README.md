see the python script to play with the numbers.. 


R = usa real estate returns
S = s&p500 returns
X = cost of house
D = Down payment percentage
Y = interest rate on mortgage
n = number of years for loan 
P = property tax
M = maintenance cost
r = monthly rent cost 

1) unrecoverable-costs-comparison
inspired by Ben Felix's video: https://www.youtube.com/watch?v=Uwl3-jBNEd4 "Renting vs. Buying a Home: The 5% Rule"
compare the monthly unrecoverable costs of renting and buying: the cost a person pays with no associated residual value
RENT: easy, it’s whatever your monthly rent is. 
BUY: more complicated.. composed of 
a. P = property taxes, generally 1% 
b. M = maintenance cost (the cost it takes to maintain current quality of house - addressing wear and tear)
c. monthly interest payment on loan: Y/12 * (X-D*X).  this does not take into account the amortization process, see caveats.
the opportunity cost of putting money into housing market versus stock market. See section below 
** Opportunity Cost
d. the person puts D% down to buy house. 1) BAD because the down payment could’ve been invested in the s&p500 instead, which historically outperforms the housing market.  2) GOOD because the entire value of the house will compound each year, not just the down payment; it’s a leveraged investment 
-> the opportunity cost is the difference between these values
1) if the down payment (D*X) was put in s&p500, it’s monthly return would have been: (S/12 *D*X)
2) the house is worth X and will increase R percent a year, the monthly return is: R/12 * X
total Opportunity cost is: (S/12 *D*X) - (R/12 * X)

-> Conclusion 
monthly unrecoverable cost of buying a house is 
P/12*X + M/12*X + Y/12 * (X-D*X) + (S/12 *D*X) - (R/12 * X)

ISSUES WITH THIS APPROACH
The following are not captured by the equation 
interest payment: the percentage of the loan payment that is interest decreases each month (amortization schedule) 
as the amount of house that is payed off increases, the opportunity cost of that money not being in s&p500 increases 
the house can be rented to others if desired , this is similar to a dividend 
monthly loan payments are greater than monthly rent payments. if buying a house causes a person to contribute less to their tax advantaged retirement accounts, then they incur an additional opportunity cost by missing out on this tax break 
if your down payment is below 20%, you must pay mortgage insurance, ~1% of loan
