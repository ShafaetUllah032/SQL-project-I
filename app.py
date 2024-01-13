import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

from dbhelper import DB
db = DB()


st.sidebar.title ('Flight Analytics')

user_option=st.sidebar.selectbox('menu',['select one','Check Flight','Analytics'])

if user_option == 'Check Flight':
    st.title('Check Flight')
    col1,col2 = st.columns(2)
    with col1:
        city=db.fetch_city_names()
        source_city=st.selectbox('Source',sorted(city))
    with col2:
        city=db.fetch_city_names()
        destination_city=st.selectbox('destination',sorted(city,reverse=True))

    if st.button('Search'):
        details=db.fetch_all_flights(source_city, destination_city)
        st.dataframe(details)


elif user_option=='Analytics':
    st.title('Analytics')
    airline, frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.header("Pie chart")
    st.plotly_chart(fig)

    city, frequency1 = db.busy_airport()
    fig = px.bar(
        x=city,
        y=frequency1
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    date, frequency2 = db.daily_frequency()

    print(len(date))
    print(len(frequency2))
    fig = px.line(
        x=date,
        y=frequency2
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


else:
    st.title("""The Flight Analytics platform is a comprehensive system designed to provide insights""")