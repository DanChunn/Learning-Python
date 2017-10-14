import pandas as pd

# Fix import by including index_col
passengers = pd.read_csv('titanic.csv', index_col=0)

#Use double brackets to return DataFrame object
#Single for series objects
print(passengers[["Survived"]])

#Use loc, iloc for cross sections of tables
#Cross section of 10 first rows and 2 columns
newTable = passengers.loc[:10,["Survived", "Age"]]
print(newTable)

#iloc uses indexing
print(newTable.iloc[:5, [0]])