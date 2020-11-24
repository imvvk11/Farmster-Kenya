from django.core.management import BaseCommand

from farmster_server.models.choices import CROP_TYPE
from farmster_server.models.crop import Crop


class Command(BaseCommand):
    def handle(self, *args, **options):
        items = ["tangerine.png   ",
                 "cashew.png      ",
                 "cassava.png     ",
                 "chicken.png     ",
                 "chilli.png      ",
                 "coconut.png     ",
                 "coffee.png      ",
                 "cotton.png      ",
                 "cucumber.png    ",
                 "eggplant.png    ",
                 "garlic.png      ",
                 "ginger.png      ",
                 "grapes.png      ",
                 "green_pepper.png",
                 "honey.png       ",
                 "irish_potato.png",
                 "lemon.png       ",
                 "mango.png       ",
                 "maze.png        ",
                 "milk.png        ",
                 "millet.png      ",
                 "olives.png      ",
                 "onion.png       ",
                 "orange.png      ",
                 "palm_oil.png    ",
                 "papaya.png      ",
                 "pea.png         ",
                 "peach.png       ",
                 "peanuts.png     ",
                 "pineapple.png   ",
                 "pumpkin.png     ",
                 "rapeseed.png    ",
                 "rice.png        ",
                 "rubber.png      ",
                 "sesame_seeds.png",
                 "soybeans.png    ",
                 "strawberry.png  ",
                 "sugar_beet.png  ",
                 "sugar_cane.png  ",
                 "sunflower.png   ",
                 "sweet_potato.png",
                 "tea.png         ",
                 "tobacco.png     ",
                 "tomato.png      ",
                 "watermelon.png  ",
                 "wax.png         ",
                 "wheat.png       ",
                 "yam.png         "]

        for item in items:
            trimmed = item.strip()
            no_ext = trimmed.replace('.png', '')
            result = str.join(" ", [x.capitalize() for x in no_ext.split('_')])
            Crop.objects.create(name=result,
                                image_url="https://farmster.mixinsoftware.com/media/files/" + trimmed,
                                type=CROP_TYPE.VEGETABLE)
