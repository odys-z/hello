extends StaticBody2D

signal hit


func _on_StaticBody2D_hit():
	# game win
	print('winnnnnnnn')
	emit_signal("hit")