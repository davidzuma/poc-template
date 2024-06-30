import streamlit as st


LOGO = "/Users/davidzumaquero/Github/davidzuma/poc-template/{{cookiecutter.directory_name}}/data/berlin_chess_bike.png"
st.set_page_config(page_title="{{cookiecutter.project_name}}", page_icon=":material/airline_seat_flat_angled:")
st.logo(LOGO)
page_1= st.Page("pages/page_1.py", title="Page 1", icon=":material/add_circle:")
page_2 = st.Page("pages/page_2.py", title="Page 2", icon=":material/airline_seat_flat_angled:")


pg = st.navigation([page_1, page_2])


pg.run()
