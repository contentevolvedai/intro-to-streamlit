import streamlit as st
import openai
import os

openai.api_key = st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]


def generate_scene(tone, writing_style, word_count, scene_description):
    messages = [
        {
            "role": "user",
            "content": "Instructions: You are an expert creative writer. I am going to give you a description of a "
                       "scene enclosed in three asterisks (e.g. '***') and I want you to write a scene based off of "
                       "that description. Write it with more showing, emotional, conversational instead of telling. "
                       "Be creative. Showing is about using description and action to help the reader experience the "
                       "story. Telling is when the author summarizes or uses exposition to simply tell the reader "
                       "what is happening. Do not explain to me what showing and telling are. Just write the scene. "
                       "Do not use the same words repeatedly. This is important!"},
        {"role": "user", "content": f"Writing Style: {writing_style}"},
        {"role": "user", "content": f"Tone: {tone}."},
        {"role": "user", "content": f"Output length should be no less than {str(word_count)} words."},
        {"role": "user", "content": f"Scene Description: *** {scene_description} ***"}
    ]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    result = ""
    for choice in response.choices:
        result += choice.message.content

    print(result)
    return result


# Main Page Header
st.title("Creative Writing Scene Generator")

# Drop down for different tones.
# Try and think of your own. Remember they are different from writing styles.
# Tones can change over time during a story, but the writing style
# Generally stays the same
tone = st.selectbox(
    "Select a tone:",
    [
        "Friendly",
        "Professional",
        "Conversational",
        "Excited",
        "Authoritative",
        "Humorous",
        "Educational",
        "Straightforward",
        "Witty",
        "Relatable",
        "Emotional",
        "Adventurous",
    ],
)

# Drop down for different tones.
writing_style = st.selectbox(
    "Select writing style:",
    [
        "Minimalist",
        "Retro",
        "Futuristic",
        "Classic",
        "Whimsical",
        "Bold",
        "Casual",
        "Fun",
        "High-end",
        "Edgy",
        "Clean",
        "Vibrant",
        "Dramatic",
        "Professional",
        "Simple",
        "Creative",
        "Dynamic",
        "Hip",
    ],
)

# Slider determining the length of output.
word_count = st.slider(
    "Select length:", min_value=300, max_value=1000, step=100, value=650
)

# Text area box describing what you want the story to be about
scene_description = st.text_area(
    "Enter details describing the scene:",
    help="What do you want the story to be about?")

# A button that kicks off the generation process
submit_button = st.button("Generate Scene")

# If submit button is clicked...
if submit_button:
    # Empty out previous output
    message = st.empty()

    # Show a busy message
    message.text("Generating story...")

    # Call our generation function
    scene = generate_scene(tone, writing_style, word_count, scene_description)

    # Write Output
    message.text("")
    st.write(scene)

    # Provide a way to download output
    st.download_button(
        label="Download scene",
        data=scene,
        file_name="Scene.txt",
        mime="text/txt",
    )
