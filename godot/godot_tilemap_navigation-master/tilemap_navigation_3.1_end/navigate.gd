extends Node2D

onready var nav : Navigation2D = $Navigation2D

# var path : PoolVector2Array
var goal : Vector2
export var speed := 250

var dots = []
const midot = preload("res://Midot.tscn")
const endot = preload("res://Endot.tscn")

func _input(event: InputEvent):
	if event is InputEventMouseButton:
		if event.button_index == BUTTON_LEFT and event.pressed:
			goal = event.position
			var path = nav.get_simple_path($Sprite.position, goal, false)
			# $Line2D.points = PoolVector2Array(path)
			# $Line2D.show()
			createPath(PoolVector2Array(path))
			
func _process(delta: float) -> void:
	"""
	if !path:
		$Line2D.hide()
		return
	if path.size() > 0:
		var d: float = $Sprite.position.distance_to(path[0])
		if d > 10:
			$Sprite.position = $Sprite.position.linear_interpolate(path[0], (speed * delta)/d)
		else:
			path.remove(0)
	"""
	
	if dots.size() > 0:
		var d: float = $Sprite.position.distance_to(dots[0].position)
		if d > 10:
			$Sprite.position = $Sprite.position.linear_interpolate(dots[0].position, (speed * delta)/d)
		else:
			dots.remove(0)		

func createPath(points):
	if !points:
		for dot in dots:
			dot.hide()
		dots.clear()
	
	if points.size() > 0:
		for point in points:
			var dot = endot.instance()
			dot.position = point
			dot.show()
			dots.append(dot)
	