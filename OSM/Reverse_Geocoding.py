import pandas, os 
import numpy as np
import time

####### read the data from excel where you the Lat-Long(geo-coordinates) information for which you want to fetch the address using Nominatim API
####### I am doing this exercise for commercial venues so I have used these three columns, you can choose to use your own data columns. 
####### Please note that only Latitude and Longitude is compulsory to run this program
df = pandas.read_excel(Input_filename, encoding='utf-8')
df =df[['Commercial_Venue_ID','Longitude','Latitude']]

####### libraries for reverse geocoding
import geopy
from geopy.geocoders import Nominatim


####### function to fetch the addresses based upon Lat-Long(geo-coordinates) information
def getaddress(latlng, language="cn"):
        ####### introduced some time lapse here so that the default one call/second condition of Nominatim API is met. In my case i'm using 400 miliseconds wait time
        time.sleep(.400)
        try:
            global Road, Residential, Street, Complete_Address,Suburb,Neighbourhood,City_district,District,Quarter,Houses,Subdivision,County,Local_administrative_area,County_code,Town,Village,City,State_District,State,PostalCode,Country
            geolocator = Nominatim(user_agent="my-application")
            location = geolocator.reverse(latlng, language=language, timeout=5)
            data = location.raw
            Complete_Address = location
            Road = data['address'].get('road')
            Region = data['address'].get('region')
            Residential = data['address'].get('residential')
            Street = data['address'].get('street')
            Suburb = data['address'].get('suburb')
            Neighbourhood = data['address'].get('neighbourhood')
            City_district = data['address'].get('city_district')
            District = data['address'].get('district')
            Quarter = data['address'].get('quarter')
            Houses = data['address'].get('houses')
            Subdivision = data['address'].get('subdivision')
            County = data['address'].get('county')
            Local_administrative_area = data['address'].get('local_administrative_area')
            County_code = data['address'].get('county_code')
            City = data['address'].get('city')
            Town = data['address'].get('town')
            Village = data['address'].get('village')
            State_District = data['address'].get('state_district')
            State = data['address'].get('state')
            Country = data['address'].get('country')
            PostalCode =data['address'].get('postcode')
            if Region ==None:
               Region = ""
            if Road ==None:
               Road = ""
            if Residential ==None:
               Residential = ""
            if Street ==None:
               Street = ""
            if Complete_Address ==None:
               Complete_Address = ""
            if Suburb ==None:
               Suburb = ""
            if City ==None:
               City = ""
            if State_District ==None:
               State_District = ""
            if State ==None:
               State = ""
            if Country ==None:
               Country = ""
            if PostalCode ==None:
               PostalCode = ""
            if Neighbourhood ==None:
               Neighbourhood = ""
            if County ==None:
               County = ""
            if City_district ==None:
               City_district = ""
            if District ==None:
               District = ""
            if Quarter ==None:
               Quarter = ""
            if Houses ==None:
               Houses = ""
            if Subdivision ==None:
               Subdivision = ""
            if Local_administrative_area ==None:
               Local_administrative_area = ""
            if County_code ==None:
               County_code = ""
            if Town ==None:
               Town = ""
            if Village ==None:
               Village = ""

        except:
            Complete_Address =""
            Region =""
            Road = ""
            Residential =""
            Street = ""
            Neighbourhood= ""
            City_district =""
            District =""
            Quarter =""
            Houses =""
            Subdivision =""
            County =""
            Local_administrative_area= ""
            County_code =""
            Town =""
            Village =""
            Suburb =""
            City = ""
            State_District = ""
            State = ""
            Country = ""
            PostalCode = ""
        return pandas.Series([Complete_Address,Region,Road,Residential,Street,Suburb,Neighbourhood,City_district,District,Quarter,Houses,Subdivision,County,Local_administrative_area,County_code,Town,Village,City,State_District,State,PostalCode,Country],index=['Complete_Address','Region','Road','Residential','Street','Suburb','Neighbourhood','City_district','District','Quarter','Houses','Subdivision','County','Local_administrative_area','County_code','Town','Village','City','State_District','State','PostalCode','Country'])



#######Combine latitude and longitude to create a key to be passed on to the reverse gecodoing function created above
df['Lat_Long_Combined'] = df['Longitude'].astype(str)+','+df['Latitude'].astype(str)
df[['Complete_Address','Region','Road','Residential','Street','Suburb','Neighbourhood','City_district','District','Quarter','Houses','Subdivision','County','Local_administrative_area','County_code','Town','Village','City','State_District','State','PostalCode','Country']]= df['Lat_Long_Combined'].apply(lambda x: getaddress(x) if x != None else None)

####### pass the path along with the file name of the excel where you want to right the data
df.to_excel(Ouput_filename, sheet_name="sheet1", index=False)