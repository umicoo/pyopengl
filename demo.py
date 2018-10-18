from camera import Camera
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window_width = 640
window_height=480

camera=Camera()

rtx=0
rty=0
global rtz
rtz=-5

def setProjection():

	

	ratio=1.0*window_width/window_height

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45,ratio, 0.01, 100)
	glViewport(0,0,window_width,window_height)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(camera.camera_x, camera.camera_y, camera.camera_z, camera.lookat_x, camera.lookat_y, camera.lookat_z, 0.0, 1.0, 0.0)

def draw():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	setProjection()
	glEnable(GL_DEPTH_TEST)
	glTranslatef(rtx,rty,rtz)
	glutWireTeapot(0.5)

	glFlush()

def SpecialKeys(key, x, y):
	if key==GLUT_KEY_UP:
		camera.PitchCamera(camera.angle)
		#camera.WalkStraight(camera.speed)
		#print('pitch')
	if key==GLUT_KEY_DOWN:
		camera.PitchCamera(-camera.angle)
		#camera.WalkStraight(-camera.speed)
	if key==GLUT_KEY_LEFT:
		camera.YawCamera(-camera.angle)
		#camera.WalkStraight(camera.speed)
	if key==GLUT_KEY_RIGHT:
		camera.YawCamera(camera.angle)
		#camera.WalkStraight(-camera.speed)
	glutPostRedisplay()

def KeyboardKeys(bkey, x, y):
	global rtz
	key=bkey.decode("utf-8")
	if key =='w':
		camera.WalkStraight(camera.speed)
		print(camera.camera_x,camera.camera_y,camera.camera_z)
	if key=='s':
		camera.WalkStraight(-camera.speed)
	if key=='a':
		camera.WalkTransverse(camera.speed)
	if key=='d':
		camera.WalkTransverse(-camera.speed)
	if key=='z':
		rtz+=1
	glutPostRedisplay()

def move():
	step=0.0002
	while rtz<0:
		z+=step
	glutPostRedisplay()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(640,480)
	glutCreateWindow("Teapot")
	glutDisplayFunc(draw)
	glutSpecialFunc(SpecialKeys)
	glutKeyboardFunc(KeyboardKeys)
	glutMainLoop()

main()
