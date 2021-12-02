import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from CotizacionCripto import CotizacionCripto
from KrakenAPIConnector import KrakenAPIConnector
from datetime import datetime, timedelta

# seteamos el layout
st.set_page_config(layout="wide", page_icon="favicon.png", page_title='Análisis de criptomonedas',
                   initial_sidebar_state='auto')
# headers

st.write('''# Análisis de criptomonedas con Python''')
st.write('---')

# body con columnas para los filtros
col1, col2, col3, col4 = st.columns(4)
today = datetime.utcnow().date()
previous_day = today - timedelta(days=1)
start_date = today - timedelta(days=90)
with col1:
    fecha_inicio = st.date_input("Selecciona la fecha de inicio: ", value=start_date, min_value=datetime(2019, 1, 1),
                                 max_value=previous_day)

# Se obtienen las posibles cotizaciones disponibles en KRAKEN y se colocan en un select
kraken = KrakenAPIConnector()
pares_disponibles = kraken.get_pairs()
default_idx = pares_disponibles.index("XBT/USD")
with col2:
    cripto_seleccionada = st.selectbox('Selecciona el par de criptomonedas:',
                                       pares_disponibles, index=default_idx)

# Selección de intervalos de tiempo de velas:
with col3:
    vela_seleccionada = st.selectbox('Intervalo de velas:', kraken.intervalo_velas, index=3)

# Selección de intervalos de vwap:
with col4:
    vwap_seleccionado = st.number_input('Intervalo de VWAP:', value=10, min_value=1, max_value=50)

# reformateamos la fecha desde el datepicket
fecha_inicio_REFORMAT = fecha_inicio.strftime("%d-%m-%Y")
fecha_inicio_dt = datetime.strptime(fecha_inicio_REFORMAT, "%d-%m-%Y")

# Se instancia el objeto cripto
par_cripto = CotizacionCripto(cripto_seleccionada, vela_seleccionada, fecha_inicio_dt, vwap_seleccionado)

try:
    data_crypto = par_cripto.obtener_cotizacion()
except (HTTPError, KrakenAPIError, CallRateLimitError) as err:
    st.warning(err)

# se crea una grilla de graficos para las velas y volumen
fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                    vertical_spacing=0.03, subplot_titles=(cripto_seleccionada, 'Volumen'),
                    row_width=[0.2, 0.7])

# Se crea el grafico de velas
candlestick = go.Candlestick(
    x=data_crypto.index,
    open=data_crypto['open'],
    high=data_crypto['high'],
    low=data_crypto['low'],
    close=data_crypto['close']
)
fig.add_trace(candlestick, row=1, col=1)

# se añade el volumen en un segundo grafico de barras
fig.add_trace(go.Bar(x=data_crypto.index, y=data_crypto['volume'], showlegend=False), row=2, col=1)

# Se añade la linea del VWAP
# Personalizacion de opciones del grafico
fig.update_layout(
    xaxis_rangeslider_visible=False,

    yaxis_title=par_cripto.base,
    showlegend=False,
    height=600

)
fig.add_trace(go.Scatter(x=data_crypto.index, y=data_crypto['indicador_vwap'],
                         mode='lines',
                         line=dict(color='#3d9df3', width=4),
                         name='VWAP'))
# Se inserta el grafico a la pagina
st.plotly_chart(fig, use_container_width=True, height=600)
