extends Node2D

# Internal node references
onready var navigation_map = $navi_map
onready var player = $player
onready var sidekick = $sidekicker


# Performed when added to scene
func _ready():

	# Connects the whistle to creating a new path
	player.connect("WHISTLE", self, "_calculate_new_path")


# Calculates a new path and gives to sidekick
func _calculate_new_path():

	# Finds path
	var path = navigation_map.get_pathA(sidekick.position, player.position)

	# If we got a path...
	if path:
		
		# Remove the first point (it's where the sidekick is)
		path.remove(0)
		
		# Sets the sidekick's path
		sidekick.path = path