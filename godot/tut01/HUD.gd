extends CanvasLayer

signal start_game

export var b = 0
# Declare member variables here. Examples:
# var a = 2
# var b = "text"

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

func show_message(text):
    $Hello.text = text
    $Hello.show()
    # $Hello.start()
	
func show_game_over():
    show_message("Game Over")
    yield($Timer, "timeout")
    $StartButton.show()
    $Hello.text = "Dodge the\nCreeps!"
    $Hello.show()

func update_score(score):
    $Hello.text = str(score)

func _on_StartButton_pressed():
    $StartButton.hide()
    emit_signal("start_game")

func _on_Timer_timeout():
    # $Hello.hide()
	show_message("Hello Ody!")

	