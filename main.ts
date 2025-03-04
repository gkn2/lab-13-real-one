let hero = sprites.create(assets.image`mc`, SpriteKind.Player)
hero.y = 120
let restaurant = game.askForString("what is the name of your burger restaurant called?")
let whatyouprepare = game.askForString("What else do you prepare besides burgers at your burger restaurant?")
let message = "Usually, when working your job at " + restaurant
let message2 = " , you are just flipping burgers and preparing " + whatyouprepare
let message3 = ". At " + restaurant + ", there are always some rowdy customers every here and there."
let message4 = "However, " + restaurant + " just fired more than half of their staff, slowing down meal-prep speeds."
let message5 = "Now, your customers have become increasingly rowdy and have resulted to commiting violence against the staff."
let message6 = "Fend off the rowdy customers in a food fight to avoid getting thrown into the frier by crazy customers."
hero.sayText(message, 8000)
pause(3000)
hero.sayText(message2, 10000)
pause(3000)
hero.sayText(message3, 11000)
pause(3000)
hero.sayText(message4, 12000)
pause(3000)
hero.sayText(message5, 12000)
pause(3000)
hero.sayText(message6, 12000)
pause(8000)
hero.setPosition(100, 60)
let customer = sprites.create(assets.image`customer`, SpriteKind.Enemy)
let burger = sprites.create(assets.image`burger`, SpriteKind.Projectile)
burger.setScale(.5, ScaleAnchor.Middle)
controller.moveSprite(hero)
