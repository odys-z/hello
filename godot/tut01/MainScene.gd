extends Node

export (PackedScene) var Mob
var score

func _ready():
    randomize()
	
func game_over():
	$Scoretime.stop()
	$Mobtime.stop()
	$BGM.stop()
	$DownSound.play()
	$HUD.show_message("Game Over")

func new_game():
	score = 0
	$Player.start($StartPosition.position)
	$Startime.start()
	$BGM.play()

func _on_Stratime_timeout():
    $Mobtime.start()
    $Scoretime.start()

func _on_Scoretimre_timeout():
    score += 1

func _on_Mobtime_timeout():
	# Choose a random location on Path2D.
	$MobPath/MobSpawnLoc.set_offset(randi())
	# Create a Mob instance and add it to the scene.
	var mob = Mob.instance()
	add_child(mob)
	# Set the mob's direction perpendicular to the path direction.
	var direction = $MobPath/MobSpawnLoc.rotation + PI / 2
	# Set the mob's position to a random location.
	mob.position = $MobPath/MobSpawnLoc.position
	# Add some randomness to the direction.
	direction += rand_range(-PI / 4, PI / 4)
	mob.rotation = direction
	# Choose the velocity.
	print(mob, mob.position, mob.rotation)
	mob.set_linear_velocity(Vector2(rand_range(mob.min_speed, mob.max_speed), 0).rotated(direction))
	# mob.move_and_slide(Vector2(rand_range(mob.min_speed, mob.max_speed), 0).rotated(direction))

func start_game():
	$HUD.update_score(score)
	$HUD.show_message("Get Ready")
	new_game()
	



