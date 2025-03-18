# #extract file from zip file
# import zipfile
# zip_ref = zipfile.ZipFile('retailorders.zip') 
# zip_ref.extractall() # extract file to dir
# zip_ref.close() # close file
# import pandas as pd
# df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
# df['Ship Mode'].unique()
# #rename columns names ..make them lower case and replace space with underscore
# df.rename(columns={'Order Id':'order_id', 'City':'city'})
# df.columns=df.columns.str.lower()
# df.columns=df.columns.str.replace(' ','_')
# df.head(5)
# #derive new columns discount , sale price and profit
# df['discount']=df['list_price']*df['discount_percent']*.01
# df['sale_price']= df['list_price']-df['discount']
# df['profit']=df['sale_price']-df['cost_price']
# #convert order date from object data type to datetime
# df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")
# #drop cost price list price and discount percent columns
# df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)
# #load the data into sql server using replace option
# import sqlalchemy as sal
# engine = sal.create_engine('mssql://LAPTOP-CSQBLOSN\SQLEXPRESS/Viraj?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
# conn=engine.connect()
# #load the data into sql server using append option
# df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')


# s1 = {1,20,3,40,5,60}
# print(s1)
# squared_set = set()

# for i in s1 :
#     if i % 2 == 0 :
#         squared_set.add(i**2)
# # print(squared_set)

# squared_set = {i**2 for i in s1 if i % 2 == 0 }
# print(squared_set)

# s1 = {1,2.5,3+4j,True,"mop"}
# s2 ={i for i in s1 if type(i)== str}
# print(s2)

# s1 ={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
# s2 = {i ** 2 for i in s1 if i % 3 == 0}
# s3 = {i ** 3 for i in s1 if i % 4 == 0}
# print(s1)
# print(s2)
# print(s3)
# s4 = {i** 3 for i in s1 if i > 5 and i % 5 == 0}
# s5 = {i** 3 for i in s1 if i > 5 if  i % 5 == 0}
# print(s4)
# print(s5)
# s6 = {'*' if i % 2 ==0 else i for i in s1}
# print(s6)
# even_set= set()
# even_set = {i**2  for i in s1 if i % 2 == 0}
# print(even_set)