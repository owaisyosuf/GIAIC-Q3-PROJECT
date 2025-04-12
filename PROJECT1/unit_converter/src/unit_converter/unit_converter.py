
import streamlit as st

def convert_unit(value, unit_from , unit_to):
  conversions={
    "meter_kilometer":0.001,
    "kilometer_meter":1000,
    "gram_kilogram":0.001,
    "kilogram_gram":1000 
  }

  key = f"{unit_from}_{unit_to}"

  if key in conversions:
    conversion=conversions[key]
    return value*conversion
  else:
    "conversion not supported"
  
  st.title("unit Converter")

  value=st.number_input("enter the value :")

  unit_from=st.selectbox("convert from:", ["meter", "kilometer" , "gram", "kilogram"])

  unit_to = st.selectbox("convert to :" , ["meter" , 'kilometer' , " gram " , "kilogram"])

  if st.button ("convert"):
    result= convert_unit(value , unit_from, unit_to)
    st.write(f"converted value: {result}")