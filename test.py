"""load and save spacy model"""
import spacy
import en_core_web_sm

nlp = en_core_web_sm.load()
nlp.to_disk('spacy_md_model/')
