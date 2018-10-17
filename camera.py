class Camera:
	def __init__():
		PI = 3.1415
		angle=3
		speed=0.3
		sight=100

		rotate_yz=0.0
		rotate_xz=-90.0
		rad_yz=rotate_yz*PI/180.0
		rad_xz=rotate_xz*PI/180.0

		camera_x=0.0
		camera_y=0.0
		camera_z=0.0

		lookat_x= camera_x + sight*cos(rad_yz)*cos(rad_xz)
		lookat_y= camera_y + sight*sin(rad_yz)
		lookat_z= camera_z + sight*cos(rad_yz)*sin(rad_xa)

	def YawCamera(fAngle):
		rotate_xz=int(rotate_xz+fAngle)%360
		rad_xz=rotate_xz*PI / 180.0

		lookat_x = camera_x + sight*cos(rad_yz)*cos(rad_xz)
		lookat_y = camera_y + sight*sin(rad_yz)
		lookat_z = camera_z + sight*cos(rad_yz)*sin(rad_xz)

	def PitchCamera(fAngle):
		rotate_xz=int(rotate_yz+fAngle)%360
		rad_yz=rotate_yz*PI/180.0

		lookat_x = camera_x + sight*cos(rad_yz)*cos(rad_xz)
		lookat_y = camera_y + sight*sin(rad_yz)
		lookat_z = camera_z + sight*cos(rad_yz)*sin(rad_xz)



