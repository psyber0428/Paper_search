import streamlit as st
from db_candidate import candidate
from db_candidate import select_output
st.title('データベース検索')

with st.form(key='profile_form'):
    #セレクトボックス
    select_word = st.selectbox(
        '過去の検索ワード',
        candidate())  

    #ボタン
    submit_btn = st.form_submit_button('検索')
    calcel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        selected = select_output(select_word)
        for i in selected:
            for j in i:
                st.text(j)         
            st.text('\n')