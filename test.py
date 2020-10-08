"""load and save spacy model"""
import spacy
import en_core_web_md

nlp = en_core_web_md.load()
nlp.to_disk('spacy_md_model/')
