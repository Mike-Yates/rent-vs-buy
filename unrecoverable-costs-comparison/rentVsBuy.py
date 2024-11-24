
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
