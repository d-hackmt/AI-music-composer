import os
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


# class responsible for generating music
class MusicLLM:
    
    # temperature is a hyperparameter , never keep it to 1
    # temperature = creativity
    
    def __init__(self , temperature=0.7):
        self.llm = ChatGroq(
            temperature=temperature,
            groq_api_key = os.getenv("GROQ_API_KEY"),
            model_name="llama-3.3-70b-versatile"
        )
    
    def generate_melody(self,user_input):
        
        """
            
            This function will be reponsible for generating melody
            
            melody : a sequence of notes / list of notes
            
            Based on user input , a melody will be generated 
            
            
        """
        
        prompt = ChatPromptTemplate.from_template(
            """Generate a melody based on this input: {input}. 
            Represent it as a space seperated notes (eg., C4 D4 E4)"""
        )
        
        # chaining prompt with LLM
        
        chain = prompt | self.llm
        # strip will eleminate the white spaces
        return chain.invoke({"input" : user_input}).content.strip()
    
    def generate_harmony(self,melody):
        
        """
            This function will be reponsible for generating harmony
            
            harmony : a sequence of chords / flow of the melody
            
            restructuring / orgainizing our notes into a perfect music
            
            Based on melody , a harmony will be generated 
            
        """
        
        prompt = ChatPromptTemplate.from_template(
            """Create harmony chords for this melody: {melody}. 
                Format: C4-E4-G4 F4-A4-C5"""
        )

        # chaining 
        chain = prompt | self.llm
        # strip will eleminate the white spaces
        return chain.invoke({"melody" : melody }).content.strip() 
        
        
    
    def generate_rythm(self,melody):
        
        """
            This function will be reponsible for generating ryhtm
            
            ryhtm : beats to the sequence of chords / harmony
            
            Based on melody , the ryhtm will be generated 
            
        """
        
        
        prompt = ChatPromptTemplate.from_template(
            """Suggest rhythm durations (in beats) for this melody: {melody}. 
                Format: 1.0 0.5 0.5 2.0"""
        )

        chain = prompt | self.llm
        return chain.invoke({"melody" : melody }).content.strip()
    
    def adapt_style(self,style,melody,harmony,rhythm):
        
        
        """
            This function will be style the music 
            
            types of styles : sad , happy , uplifting , jazz 
            
            Melody , harmony and the ryhtm will be generated 
            on the basis of the style 
            
        """
        
        prompt = ChatPromptTemplate.from_template(
            """Adapt to {style} style:
            \n Melody: {melody}
            \nHarmony: {harmony}
            \n Rhythm: {rhythm}
            \nOutput single string summary"""
        )

        # chaining
        chain = prompt | self.llm

        # return the chain 
        
        return chain.invoke({
            "style" : style,
            "melody" : melody,
            "harmony" : harmony,
            "rhythm" :rhythm
        }).content.strip()
