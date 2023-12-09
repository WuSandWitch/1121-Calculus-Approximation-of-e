import streamlit as st
import pandas as pd
import json


def get_data(approximation:str,filename="data.json") -> pd.DataFrame:

    with open(filename,"r") as f:
        raw_data = json.load(f)

    data = filter(lambda x : x["Approximation"]==approximation,raw_data["data"])

    df = pd.json_normalize(data, 
                    meta=["precision",
                        "Approximation",
                        "e_value",
                        "n",
                        "time"])

    return df

st.title("Approximations of e")
st.write("## Approximation 1")
st.latex(r"ln \, e = \int_1^{e}\frac{1}{t} dt= 1")
st.subheader("Time chart")
st.line_chart(get_data("Approximation1"), x="precision", y="time")  

st.subheader("n value chart")
st.line_chart(get_data("Approximation1"), x="precision", y="n") 

st.write("## Approximation 2")
st.latex(r"e = \lim_{\delta \to 0}(1+\delta)^\frac{1}{\delta} = \lim_{n \to \infty}(1 + \frac{1}{n})^n")

st.subheader("Time chart")
st.line_chart(get_data("Approximation2"), x="precision", y="time")  

st.subheader("n value chart")
st.line_chart(get_data("Approximation2"), x="precision", y="n") 


st.write("## Approximation 3")
st.latex(r"e = \Sigma_{n=0}^{\infty} \frac{1}{n!}")

st.subheader("Time chart")
st.line_chart(get_data("Approximation3"), x="precision", y="time")  

st.subheader("n value chart")
st.line_chart(get_data("Approximation3"), x="precision", y="n") 
