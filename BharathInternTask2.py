#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install googletrans==4.0.0-rc1')


# In[13]:


from googletrans import Translator
translator = Translator(service_urls=['translate.google.com'])

def translate_text(text, source_lang, target_lang):
    try:
        translation = translator.translate(text, src=source_lang, dest=target_lang)
        return translation.text
    except Exception as e:
        print("Translation Error:", str(e))
        return None

# Example usage
source_text = "Hello, This is Rakshitha"
source_language = "en"
target_language = "telugu"

translated_text = translate_text(source_text, source_language, target_language)
print("Translated text:", translated_text)


# In[ ]:




