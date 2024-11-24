
# this is the approach suggested by Ben Felix. it includes the leveraged investment of the house
# it does not include:
# 0. does not take into account the fact that the entire value of the house will compound each year, not just the down payment; it’s a leveraged investment
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

result = propertyTax + maintenance + interest + opportunityCost_sp500

print("the house costs " + convertToDollar(X) + ", you are putting " + str(D) + "% down")
print("")
print("monthly unrecoverable costs:")
print("property tax (" + str(P) + "%) is: " + convertToDollar(propertyTax))
print("Maintenance cost (" + str(M) + "%) is: " + convertToDollar(maintenance))
print("Interest cost (" + str(Y) + "%) is: " + convertToDollar(interest))
print("Opportunity cost of S&P500 (" + str(S) + "%) is: " + convertToDollar(opportunityCost_sp500))
print("")
print("Total monthly unrecoverable cost: " + convertToDollar(result))
