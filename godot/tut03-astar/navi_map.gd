extends TileMap


## Variables to be set when the node is ready


# Reference to a new AStar navigation grid node
onready var astar = AStar.new()

# Used to find the centre of a tile
onready var half_cell_size = cell_size / 2

# All tiles that can be used for pathfinding
onready var traversable_tiles = get_used_cells()
""" [
(0, 0), (1, 0), (2, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0), (15, 0), 
(0, 1), (2, 1), (3, 1), (4, 1), (8, 1), (15, 1), 
(0, 2), (1, 2), (2, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2), (13, 2), (14, 2), (15, 2),
(0, 3), (8, 3), (13, 3), (14, 3), (15, 3), 
(0, 4), (1, 4), (2, 4), (7, 4), (8, 4), (9, 4), (13, 4), (15, 4), 
(0, 5), (2, 5), (5, 5), (6, 5), (7, 5), (9, 5), (13, 5), (14, 5), (15, 5), 
(0, 6), (1, 6), (2, 6), (5, 6), (7, 6), (8, 6), (9, 6), (15, 6), 
(0, 7), (2, 7), (5, 7), (8, 7), (15, 7), 
(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (8, 8), (9, 8), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (15, 8)]
"""

# The bounds of the rectangle containing all used tiles on this tilemap
onready var used_rect = get_used_rect()


func _ready():

	# This would hide the navigation_map upon loading, but we'll keep
	# it commented for this demo - uncomment for your game, most likely
	# visible = false

	print(traversable_tiles)
	# Add all tiles to the navigation grid
	_add_traversable_tiles(traversable_tiles)

	# Connects all added tiles
	_connect_traversable_tiles(traversable_tiles)


## Private functions


# Adds tiles to the A* grid but does not connect them
# ie. They will exist on the grid, but you cannot find a path yet
func _add_traversable_tiles(traversable_tiles):

	# Loop over all tiles
	for tile in traversable_tiles:

		# Determine the ID of the tile
		var id = _get_id_for_point(tile)

		# Add the tile to the AStar navigation
		# NOTE: We use Vector3 as AStar is, internally, 3D. We just don't use Z.
		astar.add_point(id, Vector3(tile.x, tile.y, 0))


# Connects all tiles on the A* grid with their surrounding tiles
func _connect_traversable_tiles(traversable_tiles):

	# Loop over all tiles
	for tile in traversable_tiles:

		# Determine the ID of the tile
		var id = _get_id_for_point(tile)

		# Loops used to search around player (range(3) returns 0, 1, and 2)
		for x in range(3):
			for y in range(3):

				# Determines target, converting range variable to -1, 0, and 1
				var target = tile + Vector2(x - 1, y - 1)

				# Determines target ID
				var target_id = _get_id_for_point(target)

				# Do not connect if point is same or point does not exist on astar
				if tile == target or not astar.has_point(target_id):
					continue

				# Connect points
				astar.connect_points(id, target_id, true)


# Determines a unique ID for a given point on the map
func _get_id_for_point(point):

	# Offset position of tile with the bounds of the tilemap
	# This prevents ID's of less than 0, if points are behind (0, 0)
	var x = point.x - used_rect.position.x
	var y = point.y - used_rect.position.y

	# Returns the unique ID for the point on the map
	return x + y * used_rect.size.x


## Public functions

# Returns a path from start to end
# These are real positions, not cell coordinates
func get_pathA(start, end):

	# Convert positions to cell coordinates
	var start_tile = world_to_map(start)
	var end_tile = world_to_map(end)

	# Determines IDs
	var start_id = _get_id_for_point(start_tile)
	var end_id = _get_id_for_point(end_tile)

	# Return null if navigation is impossible
	if not astar.has_point(start_id) or not astar.has_point(end_id):
		return null

	# Otherwise, find the map
	var path_map = astar.get_point_path(start_id, end_id)

	# Convert Vector3 array (remember, AStar is 3D) to real world points
	var path_world = []
	for point in path_map:
		var point_world = map_to_world(Vector2(point.x, point.y)) + half_cell_size
		path_world.append(point_world)
	return path_world