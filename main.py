hero = sprites.create(assets.image("""mc"""), SpriteKind.player)
hero.y = 120
info.set_score(0)
scene.set_background_image(img("""
    d11111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222ddddddddddddddddddddddddddffffffffffffffffffffffffff
    .11111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222ddddddddddddddddddddddddddffffffffffffffffffffffffff
    .11111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222ddddddddddddddddddddddddddffffffffffffffffffffffffff
    .11111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222ddddddddddddddddddddddddddddddddddffffffffffffffffff
    .11111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222ddddddddddddddddddddddddddddddddddddffffffffffffffff
    .11111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222ddddddddddddddddddddddddddddddddddddffffffffffffffff
    .11111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222ddddddddddddddddddddddddddddddddddddffffffffffffffff
    .11111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222ddddddddddddddddddddddddddddddddddddffffffffffffffff
    .11111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222dddddddddddddddddddddddddddddddddddddfffffffffffffff
    .11111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222ddddddddddddddddddddddddddddddddddddddffffffffffffff
    .11111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    .11111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    .11111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    .11111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    .1111111111111111111111111111111111111111111111111111111111111111111111112222fffffdfd22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222ffffffff22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222fffffdfd22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222ffffffff22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99ffdfd22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99fffff22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99ffdfd22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99ffffd22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99ffdfd22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99fffff22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99ffdfd22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222ffffffff22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222fffffdfd22222222dddddddddddddddddddddddddddddddddddddddddddddfffffddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222ffffffff22222222dddddddddddddddddddddddddddddddddddddddddddddfffffddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222fffffdfd22222222dddddddddddddddddddddddddddddddddddddddddddddffffffffffffffffffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddddddffffffffffffffffffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddddddffffffffffffffffffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddddddffffffffffffffffffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddddddffffffffffffffffffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddddddffffffffffffffffffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddddddffffffffffffffffffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddddddffffffffffffffffffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddddddfffffddddddddddfffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddddddfffffddddddddddfffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222fffffdfd22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222ffffffff22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222fffffdfd22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222ffffffff22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99ffdfd22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99fffff22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99ffdfd22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99ffffd22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99ffdfd22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99fffff22222222ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99ffdfd22222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222ffffffff22222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222fffffdfd22222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddfffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222ffffffff22222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    11111111111111111111111111111111111111111111111111111111111111111111111112222fffffdfd22222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddddfff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddfffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddfffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddfffffffffffddddddddddfffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddffffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222fffffdfd22222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddffffffff
    11111111111111111111111111111111111111111111111111111111111111111111111112222ffffffff22222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfff5555f
    11111111111111111111111111111111111111111111111111111111111111111111111112222fffffdfd22222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfff5555f
    11111111111111111111111111111111111111111111111111111111111111111111111112222ffffffff22222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfff5555f
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99ffdfd22222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfff5555f
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99fffff22222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfff5555f
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99ffdfd22222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfff5555f
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99ffffd22222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfff5555f
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99ffdfd22222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfff5555f
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99fffff22222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfff5555f
    11111111111111111111111111111111111111111111111111111111111111111111111112222f99ffdfd22222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfff5555f
    11111111111111111111111111111111111111111111111111111111111111111111111112222ffffffff22222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfff5555f
    11111111111111111111111111111111111111111111111111111111111111111111111112222fffffdfd22222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfff5555f
    11111111111111111111111111111111111111111111111111111111111111111111111112222ffffffff22222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfff5555f
    11111111111111111111111111111111111111111111111111111111111111111111111112222fffffdfd22222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfff5555f
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfff5555f
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfff5555f
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfff5555f
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfff5555f
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222ddddddddddddddddddddddddddddddddddddddddddddfff5555f
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222ddddddddddddddddddddddddddddddddddddddddddddfff5555f
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222ddddddddddddddddddddddddddddddddddddddddddddfff5555f
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222ddddddddddddddddddddddddddddddddddddddddddddfff5555f
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222ddddddddddddddddddddddddddddddddddddddddddddfff5555f
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222ddddddddddddddddddddddddddddddddddddddddddddfff5555f
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222ddddddddddddddddddddddddddddddddddddddddddddfff5555f
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222dddddddddddddddddddddddddddddddddddffffffffffff5555f
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222dddddddddddddddddddddddddddddddddddfffffffffffffffff
    111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222dddddddddddddddddddddddddddddddddddfffffffffffffffff
"""))
# restaurant = game.askForString("what is the name of your burger restaurant called?")
# whatyouprepare = game.askForString("What else do you prepare besides burgers at your burger restaurant?")

# message = "Usually, when working your job at " + restaurant
# message2 = " , you are just flipping burgers and preparing " + whatyouprepare
# message3 = ". At " + restaurant + ", there are always some rowdy customers every here and there." 
# message4 = "However, " + restaurant + " just fired more than half of their staff, slowing down meal-prep speeds."
# message5 = "Now, your customers have become increasingly rowdy and have resulted to commiting violence against the staff."
# message6 = "Fend off the rowdy customers in a food fight to avoid getting thrown into the frier by crazy customers."
# hero.say_text(message, 8000)
# pause(3000)
# hero.say_text(message2, 10000)
# pause(3000)
# hero.say_text(message3, 11000)
# pause(3000)
# hero.say_text(message4, 12000)
# pause(3000)
# hero.say_text(message5, 12000)
# pause(3000)
# hero.say_text(message6, 12000)
# pause(8000)

hero.set_position(100, 60)

def on_update_interval():
    customer = sprites.create(assets.image("""customer"""), SpriteKind.enemy)
    customer.set_position(randint(2, 75), randint(20, 100))
game.on_update_interval(2700, on_update_interval)




controller.move_sprite(hero)

def on_event_pressed():
    burger = sprites.create_projectile_from_sprite(assets.image("""burger"""), hero, -40, 0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_event_pressed)


def on_overlap(sprite, otherSprite):
    sprites.destroy(otherSprite)
    sprites.destroy(sprite)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_overlap)
    
def on_update_interval2():
    for cust in sprites.all_of_kind(SpriteKind.enemy):
        water = sprites.create(assets.image("""water"""), SpriteKind.food)
        water.set_position(cust.x, cust.y)
        water.set_velocity(40, 0)
game.on_update_interval(2300, on_update_interval2)

def on_overlap2(sprite, otherSprite):
    sprites.destroy(otherSprite)
    sprites.destroy(sprite)
    game.game_over(False)
sprites.on_overlap(SpriteKind.food, SpriteKind.player, on_overlap2)

def on_update():
    if info.score() == 10:
        game.game_over(True)
game.on_update(on_update)
    