from modeltranslation.translator import translator, TranslationOptions

from farmster_server.models.crop import Crop


class CropTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Crop, CropTranslationOptions)
