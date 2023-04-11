import streamlit as st
import pickle as pk 
import pandas as pd
import random
from st_aggrid import AgGrid
st.set_page_config(page_title="IPL", page_icon='🏏', layout="centered",initial_sidebar_state='auto')
# Hide the "Made with Streamlit" footer
hide_streamlit_style="""
    <style>
    #MainMenu{visibility:hidden;}
    footer{visibility:hidden;}
    </style>

    """
st.markdown(hide_streamlit_style,unsafe_allow_html=True)
st.title('Cricket Win predictor')
pipe=pk.load(open('pipe7.pkl','rb'))

def Theam(Team):
    if Team =="1":
        st.write("""
        <style>
            /* The progress bars */
            .stProgress > div > div > div > div {
                background: linear-gradient(to right, red, orange);
                border-radius: 10px;
            }

            /* The text inside the progress bars */
            .stProgress > div > div > div > div > div {
                color: white;
            }
        </style>
        # """, unsafe_allow_html=True)
    elif Team =="2":
        st.write("""
        <style>
            /* The progress bars */
            .stProgress > div > div > div > div {
                background: linear-gradient(to right, #7400FB, #9B01F7);
                border-radius: 10px;
            }

            /* The text inside the progress bars */
            .stProgress > div > div > div > div > div {
                color: white;
            }
        </style>
        # """, unsafe_allow_html=True)
    elif Team =="3":
        st.write("""
        <style>
            /* The progress bars */
            .stProgress > div > div > div > div {
                background: linear-gradient(to right, #7400FB, #9B01F7);
                border-radius: 10px;
            }

            /* The text inside the progress bars */
            .stProgress > div > div > div > div > div {
                color: white;
            }
        </style>
        # """, unsafe_allow_html=True)
    elif Team =="4":
        st.write("""
        <style>
            /* The progress bars */
            .stProgress > div > div > div > div {
                background: linear-gradient(to right, Red, #9A1E06);
                border-radius: 10px;
            }

            /* The text inside the progress bars */
            .stProgress > div > div > div > div > div {
                color: white;
            }
        </style>
        # """, unsafe_allow_html=True)
    elif Team =="5":
        st.write("""
        <style>
            /* The progress bars */
            .stProgress > div > div > div > div {
                background: linear-gradient(to right, yellow, orange);
                border-radius: 10px;
            }

            /* The text inside the progress bars */
            .stProgress > div > div > div > div > div {
                color: white;
            }
        </style>
        # """, unsafe_allow_html=True)
    elif Team =="6":
        st.write("""
        <style>
            /* The progress bars */
            .stProgress > div > div > div > div {
                background: linear-gradient(to right, skyblue, lightblue);
                border-radius: 10px;
            }

            /* The text inside the progress bars */
            .stProgress > div > div > div > div > div {
                color: white;
            }
        </style>
        # """, unsafe_allow_html=True)
    elif Team =="7":
        st.write("""
        <style>
            /* The progress bars */
            .stProgress > div > div > div > div {
                background: linear-gradient(to right, #FF0275, red);
                border-radius: 10px;
            }

            /* The text inside the progress bars */
            .stProgress > div > div > div > div > div {
                color: white;
            }
        </style>
        # """, unsafe_allow_html=True)
    elif Team =="8":
        st.write("""
        <style>
            /* The progress bars */
            .stProgress > div > div > div > div {
                background: linear-gradient(to right, #02027D, #6A6AC1);
                border-radius: 10px;
            }

            /* The text inside the progress bars */
            .stProgress > div > div > div > div > div {
                color: white;
            }
        </style>
        # """, unsafe_allow_html=True)
    elif Team =="9":
        st.write("""
        <style>
            /* The progress bars */
            .stProgress > div > div > div > div {
                background: linear-gradient(to right, #02027D, #FF0299);
                border-radius: 10px;
            }

            /* The text inside the progress bars */
            .stProgress > div > div > div > div > div {
                color: white;
            }
        </style>
        # """, unsafe_allow_html=True)
    elif Team =="10":
        st.write("""
        <style>
            /* The progress bars */
            .stProgress > div > div > div > div {
                background: linear-gradient(to right, #02027D, #FF0299);
                border-radius: 10px;
            }

            /* The text inside the progress bars */
            .stProgress > div > div > div > div > div {
                color: white;
            }
        </style>
        # """, unsafe_allow_html=True)


def Balls(ball_No,n):
  return (ball_No)*10 - 4*n
with st.sidebar:
    # target=179
    col3,col4=st.columns(2)
    with col3:
        target=st.number_input("Target",step=1)
    with col4:
        Score=st.number_input('Score',step=1)
        # Score=178
    with col3:
        OverNo=st.number_input('Over',min_value=0.1,max_value=20.0,step=0.1)
        # OverNo = 18.0
        r = round(OverNo)
        Overs=Balls(OverNo,r)
    with col4:
        wickets=st.number_input('Wickets',min_value=0,max_value=10,step=1)
    # wickets=3
# if st.button('Predict'):
runs_left=target-Score
balls_left=round(120-Overs)
wickets=10-wickets
crr=Score/OverNo
rrr=(runs_left*6)/balls_left
# if rrr >=20 :
#     rrr = 100
input_df=pd.DataFrame({
      'runs_left':[runs_left], 
      'balls_left':[balls_left],
      'wickets':[wickets], 
      'total_runs_x':[target],
      'crr':[crr],
      'rrr':[rrr]
      })
# AgGrid(input_df)
result= pipe.predict_proba(input_df)
loss=result[0][0]
win=result[0][1]
#   st.write(f"# {batting_team} vs {bowling_team}")
st.write("## Winning Probability:")
# st.warning(balls_left)
Theam(str(random.randint(1,10)))
Batting_bar = st.progress(win)
st.write(str(round(win*100)),"%")
#   st.write(batting_team,"- ",str(round(win*100)),"%")
#   st.write(bowling_team,"- ",str(round(loss*100)),"%")

      