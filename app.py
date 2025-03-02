import streamlit as st

def convert_units(value, from_unit, to_unit, conversion_dict):
    if from_unit in conversion_dict and to_unit in conversion_dict:
        return value * conversion_dict[to_unit] / conversion_dict[from_unit]
    return None

st.set_page_config(page_title="Unit Converter", page_icon="🔄")

st.markdown("""
    <style>
        .big-title {
            font-size: 36px !important;
            font-weight: bold;
            text-align: center;
            color: #4CAF50;
        }
        .stApp {
            background-color: #f5f5f5;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 18px;
            color: #555;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<p class='big-title'>🔄 Unit Converter App 🔄</p>", unsafe_allow_html=True)

conversion_type = st.selectbox("🌍 Select conversion type", ["📏 Length", "⚖️ Weight", "🌡️ Temperature"])

if conversion_type == "📏 Length":
    units = {"Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Millimeter": 0.001, "Mile": 1609.34, "Yard": 0.9144, "Foot": 0.3048, "Inch": 0.0254}
    value = st.number_input("🔢 Enter value")
    from_unit = st.selectbox("🔄 From", list(units.keys()))
    to_unit = st.selectbox("🔄 To", list(units.keys()))
    result = convert_units(value, from_unit, to_unit, units)
    if result is not None:
        st.success(f"✅ Converted Value: {result} {to_unit}")

elif conversion_type == "⚖️ Weight":
    units = {"Kilogram": 1, "Gram": 0.001, "Pound": 0.453592, "Ounce": 0.0283495}
    value = st.number_input("🔢 Enter value")
    from_unit = st.selectbox("🔄 From", list(units.keys()))
    to_unit = st.selectbox("🔄 To", list(units.keys()))
    result = convert_units(value, from_unit, to_unit, units)
    if result is not None:
        st.success(f"✅ Converted Value: {result} {to_unit}")

elif conversion_type == "🌡️ Temperature":
    value = st.number_input("🔢 Enter temperature value")
    from_unit = st.selectbox("🔄 From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("🔄 To", ["Celsius", "Fahrenheit", "Kelvin"])
    
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        result = value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        result = (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        result = value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        result = (value - 273.15) * 9/5 + 32
    else:
        result = value
    
    st.success(f"✅ Converted Value: {result} {to_unit}")

st.markdown("<p class='footer'>✨ Created by: Rimsha Ansari ✨</p>", unsafe_allow_html=True)
