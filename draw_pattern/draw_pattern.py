import turtle

def draw_square(secondary_turtle):
	for i in range(4):
		secondary_turtle.forward(100)
		secondary_turtle.rt(90)
 
	
		

def	art():
	main_turtle = turtle.Turtle()
	window = turtle.Screen()
	window.bgcolor("black")
	main_turtle.color("cyan" , "yellow")
	main_turtle.shape("turtle")
	main_turtle.speed(10)

	for i in range(36):
		draw_square(main_turtle)
		main_turtle.rt(10)

	window.exitonclick()
art()



	












