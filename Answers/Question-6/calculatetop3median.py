
import pandas as pd

def calculatetop3median(data):
    
    """
    Calcualte the top 3 country respect to their median
    
    
    Args:
    data (pd.DataFrame): The DataFrame containing the vaccination data.
    
    Returns:
    An object which holds top 3 data
        
    """
    
    # group the data by country and calculate the median daily vaccinations
    grouped = round(data.groupby('country')['daily_vaccinations'].median())
    
    # sort the data by median daily vaccinations and get the top-3 countries
    top_3 = grouped.sort_values(ascending=False).head(3)
    return top_3

def fiilmissingdata(data):
    
    """
    Fills the missing data (impute) in daily_vaccinations column per country with the 
    minimum daily vaccination number of relevant countries. If a country does not have 
    any valid vaccination number yet, it fills it with “0” (zero).
    
    Args:
    data (pd.DataFrame): The DataFrame containing the vaccination data.
    
    Returns:
    pd.DataFrame: The DataFrame with missing values in the daily_vaccinations column filled.
    """
    
    #extract columns to process easily
    vaccaines = data['daily_vaccinations']
    countries = data['country']
    
    #variables to hold temporary values to be changed
    index = 0
    min_values = {}
    
    
    #get the minimum vaccaine values for each country
    
    for i in data['country']:
        if str(vaccaines[index]) != 'nan':
    
            if i in min_values:
                if vaccaines[index] < min_values[i]:
                    min_values[i] = vaccaines[index]
    
            else:
                min_values[i] = vaccaines[index]
    
        index = index+1
    
    #check if there is a country which only consist of nan values and give them to hold 0
    
    for i in data['country']:
        if i in min_values:
    
            continue
        else:
            
            min_values[i] = 0
    
    index = 0
    
    
    #change nan values to minumum values of each country
    for i in vaccaines:
        if str(i) == 'nan':
            data.loc[index, "daily_vaccinations"] = min_values[str(
                countries[index])]
    
    print(data)
    return data


#upload csv file to dataframe to process
data = pd.read_csv('country_vaccination_stats.csv')


# Fill missing values in the daily_vaccinations column
data = fiilmissingdata(data)

# Print the filled DataFrame
print(data)

top_3=calculatetop3median(data)

# print the top-3 countries and their median daily vaccinations
print(top_3)
