from gtts import gTTS as OriginalgTTS


class gTTS(OriginalgTTS):
    def __init__(self, text, _unused, lang):
        super().__init__(text=text, lang=lang)
