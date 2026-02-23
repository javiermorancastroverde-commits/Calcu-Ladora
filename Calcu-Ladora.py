import streamlit as st

st.set_page_config(page_title="Calculadora de Rebajas")

st.title(" Calculadora de Rebajas")
st.write("Introduce el precio y el descuento para ver el precio final")

st.sidebar.header("Datos del producto")

precio_original = st.sidebar.number_input("Precio original (€)", min_value=0.0, value=120.00)
descuento = st.sidebar.slider("Descuento (%)", 0, 100, 30)

if st.button("Calcular precio final"):

    ahorro = precio_original * (descuento / 100)
    precio_final = precio_original - ahorro

    st.metric("Precio Final", f"{precio_final:.2f} €")
    st.success(f"Te ahorras {ahorro:.2f} €")
   
    if descuento >= 50:
        st.warning("¡DESCUENTAZO!")
        st.balloons()
