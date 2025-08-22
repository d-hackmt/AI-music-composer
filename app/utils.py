# utility functions for generating music


# library import

import music21      # for handling music theory  
import numpy as np  # handling audio signal data
import io           # for temporary storage of generated music , inmemory / cache 
from scipy.io.wavfile import write as write_wav   # converting numpy array into audio
from synthesizer import Synthesizer,Waveform      # generating audio wavs / sin wavs from music 21 input

def note_to_frequencies(note_list):
    
    """ 
        Converts your musical notes
        into frequencies
    
    """
    
    # storing freqencies
    freqs=[]
    
    
    # to generate your notes into freq
    
    # for each note in note list
    
    for note_str in note_list:
        try:
            note=music21.note.Note(note_str)   # creating note obj from  music21
            freqs.append(note.pitch.frequency)
        except:
            continue

    return freqs


# 

def generate_wav_bytes_from_notes_freq(notes_freq):
    
    """ 
        Generating wav audio from note frequencies
        with the help of Synthesizer.
        
        using sine wave and 1 oscillator
        with sample rate 44100 
    
    """
    
    synth = Synthesizer(osc1_waveform=Waveform.sine , osc1_volume=1.0 , use_osc2=False)
    
    # audio quality of your file
    
    sample_rate = 44100 

    # each freq to sine way 
    
    audio = np.concatenate([synth.generate_constant_wave(freq , 0.5) for freq in notes_freq ]) 

    # to store audio file in a temperory file 
    
    buffer = io.BytesIO()
    write_wav(buffer,sample_rate,audio.astype(np.float32))

    # return buffer value
    
    return buffer.getvalue()




