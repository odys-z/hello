extends Sprite

# Speed at which player moves
const MOVEMENT_SPEED = Vector2(128, 128)

# Signal the sidekick should come to the player
signal WHISTLE


# Performed on each step
func _process(delta):

	# Calculate movement
	var velocity = Vector2(0, 0)
	if Input.is_action_pressed("ui_left"):
		velocity.x = -1
	if Input.is_action_pressed("ui_right"):
		velocity.x = 1
	if Input.is_action_pressed("ui_up"):
		velocity.y = -1
	if Input.is_action_pressed("ui_down"):
		velocity.y = 1

	# Actually move player
	position += velocity * MOVEMENT_SPEED * delta

	# If pressing space, whistle
	if Input.is_action_just_pressed("ui_accept"):
		emit_signal("WHISTLE")