hero = sprites.create(assets.image("""mc"""), SpriteKind.player)
hero.y = 120

restaurant = game.askForString("what is the name of your burger restaurant called?")
whatyouprepare = game.askForString("What else do you prepare besides burgers at your burger restaurant?")

message = "Usually, when working your job at " + restaurant
message2 = " , you are just flipping burgers and preparing " + whatyouprepare
message3 = ". At " + restaurant + ", there are always some rowdy customers every here and there." 
message4 = "However, " + restaurant + " just fired more than half of their staff, slowing down meal-prep speeds."
message5 = "Now, your customers have become increasingly rowdy and have resulted to commiting violence against the staff."
message6 = "Fend off the rowdy customers in a food fight to avoid getting thrown into the frier by crazy customers."
hero.say_text(message, 8000)
pause(3000)
hero.say_text(message2, 10000)
pause(3000)
hero.say_text(message3, 11000)
pause(3000)
hero.say_text(message4, 12000)
pause(3000)
hero.say_text(message5, 12000)
pause(3000)
hero.say_text(message6, 12000)
pause(8000)

hero.set_position(100, 60)

customer = sprites.create(assets.image("""customer"""), SpriteKind.enemy)
customer.set_position(50, randint(20, 100))

burger = sprites.create(assets.image("""burger"""), SpriteKind.projectile)
burger.set_scale(.5, ScaleAnchor.MIDDLE)

controller.move_sprite(hero)

