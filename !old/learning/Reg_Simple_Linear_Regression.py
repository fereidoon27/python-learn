import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

df = pd.read_csv('E:\\0current\\repository\machine_learning_with_python_jadi\\FuelConsumption.csv')
# print(df.head(3))
# print(df.describe())
cdf = df[ ['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS'] ]
viz = cdf[ ['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB'] ]

# viz.hist()
# df.hist()
# plt.show()

# print (cdf['CYLINDERS']) # equal with : print (cdf.CYLINDERS)
print ('cdf["CYLINDERS"].values is : ==>', cdf['CYLINDERS'].values)


# plt.scatter (cdf['CYLINDERS'] , cdf['CO2EMISSIONS'], color = 'red')
# plt.show()

# plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
# plt.show()

# plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS,  color='blue')
# plt.xlabel("FUELCONSUMPTION_COMB")
# plt.ylabel("Emission")
# plt.show()

msk = np.random.rand(len(cdf)) < 0.8
# print(msk)
train = cdf[msk]
test = cdf[~msk]
# print('train is : \n' , train)


## 2 scatter in one chart
# plt.scatter(test.ENGINESIZE, test.CO2EMISSIONS,  color='red')
# plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
# plt.xlabel("Engine size")
# plt.ylabel("Emission")
# plt.show()


from sklearn import linear_model
regr = linear_model.LinearRegression()

## error will ocure if 2 line below runnig !!!!!!!
# train_x = np.asanyarray(train.ENGINESIZE)
# train_y = np.asanyarray(train.CO2EMISSIONS)
## cdf["CYLINDERS"].values == np.asanyarray(cdf.CYLINDERS) 
# print( cdf["CYLINDERS"].values, '\n\n',np.asanyarray(cdf.CYLINDERS))

train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])

## what is the type realy ?? :)
# print ('type(train_y) is ' , type(train_y))
# print ('type(train is) ' ,type(train))
# print ('type(train[["CO2EMISSIONS"]]) is ' ,type(train[['CO2EMISSIONS']]))
# print ('type train.CO2EMISSIONS is ' ,type(train.CO2EMISSIONS))
# print ('type(train["CO2EMISSIONS"]) is ' ,type(train['CO2EMISSIONS']))


regr.fit (train_x, train_y)

# The coefficients
print ('Coefficients: ', regr.coef_)
print ('Intercept: ', regr.intercept_)

plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue' )
plt.plot(train_x, regr.coef_[0][0] * train_x + regr.intercept_[0],  '-r' )
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()



from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_ = regr.predict(test_x)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y , test_y_) )






