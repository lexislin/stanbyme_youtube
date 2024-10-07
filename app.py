import pandas as pd
import streamlit as st
from collections import Counter

# Load video details
video_details_file = 'video_details_preview.xlsx'
channel_details_file = 'channel_details_preview.xlsx'

# Read data
video_df = pd.read_excel(video_details_file)
channel_df = pd.read_excel(channel_details_file)

# Function to calculate tag frequencies
def calculate_tag_frequencies(df):
    tags_list = df['tags'].dropna().tolist()  # Drop NaN values
    tags_flat = [tag.strip() for tags in tags_list for tag in tags.split(',')]  # Flatten and strip whitespace
    tag_counts = Counter(tags_flat)
    return tag_counts

# Streamlit app
st.title("Video and Channel Insights")

# Display video details
st.subheader("Video Details")
st.dataframe(video_df)

# Display channel details
st.subheader("Channel Details")
st.dataframe(channel_df)

# Calculate and display tag frequencies
st.subheader("Tag Frequencies")
tag_counts = calculate_tag_frequencies(video_df)

if tag_counts:
    # Get the 20 most common tags
    top_tags = tag_counts.most_common(20)
    tag_df = pd.DataFrame(top_tags, columns=['Tag', 'Frequency'])

    # Sort the DataFrame by frequency in descending order
    tag_df = tag_df.sort_values(by='Frequency', ascending=False)

    # Display the bar chart using Streamlit's built-in function
    st.bar_chart(tag_df.set_index('Tag'))

    # Display the counts above the bars
    for i in range(len(tag_df)):
        st.text(f"{tag_df['Tag'].iloc[i]}: {tag_df['Frequency'].iloc[i]}")
else:
    st.write("No tags available.")
