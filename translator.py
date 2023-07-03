"""Module providingFunction translator python version."""
from deep_translator import MyMemoryTranslator

# translate Englist text to French text
def english_to_french(text):
    """Function English to French python version."""
    return MyMemoryTranslator(source='english', target='french').translate(text)

# translate French text to English text
def french_to_english(text):
    """Function French to English python version."""
    return MyMemoryTranslator(source='french', target='english').translate(text)
