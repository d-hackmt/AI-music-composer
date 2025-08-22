import streamlit as st
from app.main import MusicLLM
from app.utils import *
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

# streamlit config

st.set_page_config(page_title="AI Music Composer",layout="centered")
st.title("AI MUSIC COMPOSER")
st.markdown("Lets make some beats yo !! Just describe the style and content")


# input boxes

music_input = st.text_input("Describe you taste man")
# style = st.selectbox("Choose a style" , ["House" , "Lofi" , "Techno" , "Afro" , "Psychedelic" , "EDM" , "Hip-Hop" , "Trap" , "Dubstep"])
style = st.selectbox("Choose a style" , ["Happy" , "Sad" , "Jazz" , "Extreme"])

# trigger workflow
# check if user has passed anything or not
if st.button("Generate Music") and music_input:
    
    # created out object for generating music class
    generator = MusicLLM()
    
    # loading spiner
    with st.spinner("Generating music"):
        
        # passing inputs 
        
        melody = generator.generate_melody(music_input)
        harmony = generator.generate_harmony(melody)
        rhythm = generator.generate_rythm(melody)
        composition = generator.adapt_style(style,melody,harmony,rhythm)


        # generating melody
        melody_notes = melody.split() # splitting the notes 
        # eg : [E4 , E5 , E6]
        
        # notes to frequencies
        melody_freqs = note_to_frequencies(melody_notes)

        # generating harmony
        harmony_chords = harmony.split() # spliiting the harmony , the structured melody    
        harmony_notes=[]
        for chord in harmony_chords:
            harmony_notes.extend(chord.split('-'))

        # structured notes to frequencies
        harmony_freqs = note_to_frequencies(harmony_notes)

        # concatenating all
        all_freqs = melody_freqs+harmony_freqs

        # generating audio out of our frequencies
        wav_bytes = generate_wav_bytes_from_notes_freq(all_freqs)
    

    st.audio(BytesIO(wav_bytes), format='audio/wav')

    st.success("Music generated sucesfully....")

    with st.expander("Composition Summary"):
        # display the music generated from byte memory
        st.text(composition)
    


