
# this is the approach suggested by reddit user GameDoesntStop. it includes the leveraged investment of the house
# it does not include:
# 1. interest payment: the percentage of the loan payment that is interest decreases each month (amortization schedule) 
# 2. as the amount of house that is payed off increases, the opportunity cost of that money not being in s&p500 increases 
# 3. the house can be rented to others if desired , this is similar to a dividend 
# 4. monthly loan payments are greater than monthly rent payments. if buying a house causes a person to contribute less to their tax advantaged retirement accounts, then they incur an additional opportunity cost by missing out on this tax break 
# 5. if your down payment is below 20%, you must pay mortgage insurance, ~1% of loan


def convertToDollar(amount):
    return "${:,.2f}".format(amount)

# R = usa real estate return %
R=5.5
# S = s&p500 return %
S=10.5
# X = cost of house
X=500000
# D = Down payment percentage
D=20
# Y = interest rate on mortgage
Y=3
# P = property tax %
P=1
# M = maintenance cost percentage
M=0.5


propertyTax = P*.01/12*X
maintenance = M*.01/12*X
interest = Y*.01/12 * (X-D*.01*X)
opportunityCost_sp500 = (S*.01/12 *D*.01*X)
leveragedHousingInvestment = -(R*.01/12 * X)

result = propertyTax + maintenance + interest + opportunityCost_sp500 + leveragedHousingInvestment

print("the house costs " + convertToDollar(X) + ", you are putting " + str(D) + "% down")
print("")
print("monthly unrecoverable costs:")
print("property tax (" + str(P) + "%) is: " + convertToDollar(propertyTax))
print("Maintenance cost (" + str(M) + "%) is: " + convertToDollar(maintenance))
print("Interest cost (" + str(Y) + "%) is: " + convertToDollar(interest))
print("Opportunity cost of S&P500 (" + str(S) + "%) is: " + convertToDollar(opportunityCost_sp500))
print("Leveraged housing investment (" + str(R) + "%) is: " + convertToDollar(leveragedHousingInvestment))
print("")
print("Total monthly unrecoverable cost: " + convertToDollar(result))


# thoughts: from playing around with this script, it seems that its pretty much always optimal to go with renting over buying, even dudring times 
# of extreme interest rates. my intuitiont tells me that the variables not being accounted for (see top of this file) are throwing calculations off 
# -> hence, I will switch to trying to look at the two investment options on a 30 year horizon. 