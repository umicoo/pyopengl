import Camera
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window_width = 640
window_height=480

def setProjection():
	ratio=1.0*window_width/window_height

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45,ratio, 0.01, 100)
	glViewport(0,0,window_width,window_height)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt()


def main():
	glutInit()
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(640,480)
	glutCreateWindow("Teapot")
	glutDisplayFunc(display)
	glutSpecialFunc(SpecialKeys)
	glutMainLoop()