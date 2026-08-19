import streamlit as st
import pandas as pd
import json
import plotly.express as px

# Set up the page layout
st.set_page_config(page_title="AI Review Analytics", layout="wide")
st.title("📊 AI-Powered Customer Review Analytics")
st.markdown("Extracting aspect-based sentiment from unstructured text using local LLMs.")

# Load the data
@st.cache_data
def load_data():
    df = pd.read_csv('processed_ai_insights.csv')
    
    # Unpack the JSON strings into a list of dictionaries
    aspect_list = []
    for index, row in df.iterrows():
        try:
            aspects = json.loads(row['extracted_aspects'])
            for aspect, sentiment in aspects.items():
                aspect_list.append({
                    'Aspect': aspect.lower(),
                    'Sentiment': sentiment,
                    'Original_Rating': row['rating']
                })
        except:
            continue
            
    return df, pd.DataFrame(aspect_list)

df_raw, df_aspects = load_data()

# Create layout columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top Extracted Aspects")
    # Count the most frequently mentioned aspects
    top_aspects = df_aspects['Aspect'].value_counts().head(10).reset_index()
    top_aspects.columns = ['Aspect', 'Count']
    
    fig = px.bar(top_aspects, x='Count', y='Aspect', orientation='h', title="Most Discussed Features")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Sentiment Breakdown")
    # Show sentiment distribution
    sentiment_counts = df_aspects['Sentiment'].value_counts().reset_index()
    sentiment_counts.columns = ['Sentiment', 'Count']
    
    fig2 = px.pie(sentiment_counts, values='Count', names='Sentiment', title="Overall Aspect Sentiment")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Raw AI Insights")
st.dataframe(df_raw.head(50))