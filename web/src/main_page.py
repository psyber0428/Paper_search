import streamlit as st
from search import run_workflow
from db_add import input_arrange

response_mode = "blocking"
user = "example_user"

st.title('論文検索')

with st.form(key='profile_form'):
    #テキストボックス
    word = st.text_input('検索ワード')

    #ボタン
    submit_btn = st.form_submit_button('検索')
    calcel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'{word}で検索中です。')
        inputs = {"input": word}
        result = run_workflow(inputs, response_mode, user)
        st.text(result)
        # a = result.split('\n')
        # for i in range(len(a)):
        #     print('//////')
        #     print(f'{i}///{a[i]}')
        # print("////////////////////////////")
        input_arrange(result, word)



    
    