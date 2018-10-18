import math

class Camera():
	def __init__(self):
		self.PI = 3.1415
		self.angle=3
		self.speed=0.3
		self.sight=100

		self.rotate_yz=0.0
		self.rotate_xz=-90.0
		self.rad_yz=self.rotate_yz*self.PI/180.0
		self.rad_xz=self.rotate_xz*self.PI/180.0

		self.camera_x=0.0
		self.camera_y=0.0
		self.camera_z=0.0

		self.lookat_x= self.camera_x + self.sight*math.cos(self.rad_yz)*math.cos(self.rad_xz)
		self.lookat_y= self.camera_y + self.sight*math.sin(self.rad_yz)
		self.lookat_z= self.camera_z + self.sight*math.cos(self.rad_yz)*math.sin(self.rad_xz)

	def YawCamera(self,fAngle):
		self.rotate_xz=int(self.rotate_xz+fAngle)%360
		self.rad_xz=self.rotate_xz*self.PI / 180.0

		self.lookat_x = self.camera_x + self.sight*math.cos(self.rad_yz)*math.cos(self.rad_xz)
		self.lookat_y = self.camera_y + self.sight*math.sin(self.rad_yz)
		self.lookat_z = self.camera_z + self.sight*math.cos(self.rad_yz)*math.sin(self.rad_xz)

	def PitchCamera(self,fAngle):
		self.rotate_yz=int(self.rotate_yz+fAngle)%360
		self.rad_yz=self.rotate_yz*self.PI/180.0

		self.lookat_x = self.camera_x + self.sight*math.cos(self.rad_yz)*math.cos(self.rad_xz)
		self.lookat_y = self.camera_y + self.sight*math.sin(self.rad_yz)
		self.lookat_z = self.camera_z + self.sight*math.cos(self.rad_yz)*math.sin(self.rad_xz)

	def WalkStraight(self, fSpeed):
		self.camera_x =self.camera_x+fSpeed*math.cos(self.rad_yz)*math.cos(self.rad_xz)
		self.camera_y =self.camera_y+fSpeed*math.sin(self.rad_yz)
		self.camera_z =self.camera_z+fSpeed*math.cos(self.rad_yz)*math.sin(self.rad_xz)

		self.lookat_x = self.camera_x + self.sight*math.cos(self.rad_yz)*math.cos(self.rad_xz)
		self.lookat_y = self.camera_y + self.sight*math.sin(self.rad_yz)
		self.lookat_z = self.camera_z + self.sight*math.cos(self.rad_yz)*math.sin(self.rad_xz)

	def WalkTransverse(self, fSpeed):
		self.camera_x+=fSpeed*math.cos(self.rad_yz)*math.sin(self.rad_xz)
		self.camera_z-=fSpeed*math.cos(self.rad_yz)*math.cos(self.rad_xz)

		self.lookat_x = self.camera_x + self.sight*math.cos(self.rad_yz)*math.cos(self.rad_xz)
		self.lookat_y = self.camera_y + self.sight*math.sin(self.rad_yz)
		self.lookat_z = self.camera_z + self.sight*math.cos(self.rad_yz)*math.sin(self.rad_xz)



