extends Sprite

# Speed at which the sidekick will move
const MOVEMENT_SPEED = 96

# How close the sidekick must be to a point in the
# path before moving on to the next one
const POINT_RADIUS = 5

# Path that the sidekick must follow - undefined by default
var path


# Performed on each step
func _process(delta):

	# Only do stuff if we have a current path
	if path:

		# The next point is the first member of the path array
		var target = path[0]

		# Determine direction in which sidekick must move
		var direction = (target - position).normalized()

		# Move sidekick
		position += direction * MOVEMENT_SPEED * delta

		# If we have reached the point...
		if position.distance_to(target) < POINT_RADIUS:

			# Remove first path point
			path.remove(0)

			# If we have no points left, remove path
			if path.size() == 0:
				path = null

