import pandas as pd
import numpy as np
from datetime import datetime as dt
import category_encoders as ce

# read csv data
df = pd.read_csv('SelectedFinal.csv',low_memory=False)

# encode booking dates
checkin = pd.to_datetime(df['booking_check_in'])
df['checkin_day'] = checkin.dt.day
df['checkin_month'] = checkin.dt.month
df['checkin_year'] = checkin.dt.year

checkout = pd.to_datetime(df['booking_check_out'])
df['checkout_day'] = checkout.dt.day
df['checkout_month'] = checkout.dt.month
df['checkout_year'] = checkout.dt.year

dates = df[['checkin_day', 'checkin_month', 'checkin_year', 'checkout_day', 'checkout_month', 'checkout_year']]
#checkout = df['booking_check_out'].dt.date
# encode IDs in ordinal
ids = ce.OrdinalEncoder(cols=['listing_id','unit_id','property_id','area_id'])
ids = ids.fit_transform(df)
ids = ids[['listing_id','unit_id','property_id','area_id']]

# encode property
pType = pd.get_dummies(df.property_type,prefix= "type")
pDesign = pd.get_dummies(df.property_design, prefix='design')

#encode earnings
earnings = df['usd']

# concatinate all df
cproperty = pd.concat([pType,pDesign],axis='columns')

dummies = pd.concat([dates,ids,cproperty,earnings],axis='columns')
#print(dummies)
# dump to csv
dummies.to_csv('finis.csv')