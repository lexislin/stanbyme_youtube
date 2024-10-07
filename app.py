import streamlit as st
import pandas as pd

# Load data from Excel files
video_details = pd.read_excel('video_details_preview.xlsx')
channel_details = pd.read_excel('channel_details_preview.xlsx')

# Set the title of the app
st.title("YouTube Analysis Dashboard")

# Sidebar for navigation
st.sidebar.header("Navigation")
options = st.sidebar.radio("Select a view:", ("Video Details", "Channel Details"))

# Display video details
if options == "Video Details":
    st.subheader("Video Details")
    
    # Show the video details table
    st.dataframe(video_details)

    # Optionally, visualize some statistics
    st.write("## Statistics")
    st.write("Total Videos:", video_details.shape[0])
    st.write("Total Views:", video_details['viewCount'].sum())
    st.write("Average Likes:", video_details['likeCount'].mean())
    st.write("Average Comments:", video_details['commentCount'].mean())

# Display channel details
if options == "Channel Details":
    st.subheader("Channel Details")
    
    # Show the channel details table
    st.dataframe(channel_details)

    # Optionally, visualize some statistics
    st.write("## Statistics")
    st.write("Total Channels:", channel_details.shape[0])
    st.write("Total Subscribers:", channel_details['subscriberCount'].sum())
    st.write("Average Views per Channel:", channel_details['viewCount'].mean())
    st.write("Average Videos per Channel:", channel_details['videoCount'].mean())

# Run the app
if __name__ == "__main__":
    st.write("Please select a view from the sidebar.")
