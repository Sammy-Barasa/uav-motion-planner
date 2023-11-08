# from RRT_3D_class import RRT3d, env3d
from PathCalculator.rrt_algo_api import RRT3d, env3d
import matplotlib.pyplot as plt
nmax = 5000

#goal region
xg=5
yg=5
zg=5
epsilon=5
xgmin=xg-epsilon
xgmax=xg+epsilon
ygmin=yg-epsilon
ygmax=yg+epsilon
zgmin=zg-epsilon
zgmax=zg+epsilon


#extend step size
dmax = 5
#start the root of the tree
nstart =(100,100,100) 

#specify vertices for rectangular obstacles (each object has four vertices)
#obstacles known a priori
# vx= [40,40,60,60,70,70,80,80,40,40,60,60]
# vy= [52,100,100,52,40,60,60,40, 0,48,48, 0]

vx= [40,40,60,60,70,70,80,80,40,40,60,60]
vy= [52,100,100,52,40,60,60,40,0,48,48, 0]
vz = [0,100,0,60,50,80]
#hidden obstacle
hvx= [15,15,25,25,25,25,35,35]
hvy= [15,30,30,15,40,60,60,40]


#create an RRT tree with a start node
G=RRT3d(nstart,xgmin=xgmin,xgmax=xgmax,ygmin=ygmin,ygmax=ygmax,zgmin=zgmin,zgmax=zgmax,xg=xg,yg=yg,zg=zg,dmax=dmax,nmax=nmax)


#environment instance
# E=env3d(vx,vy,vz,0,4900,0,3100,0,3000)
E=env3d(vx,vy,vz,0,100,0,100,0,100,hvx=hvx,hvy=hvy,G=G,xgmin=xgmin,xgmax=xgmax,ygmin=ygmin,ygmax=ygmax,zgmin=zgmin,zgmax=zgmax)
G.set_E(E)
G.set_G(G)


#draw setup
fig = plt.figure()
# ax = fig.gca(projection='3d')
ax=fig.add_subplot(111, projection='3d')


#--------------------------------------Functions------------------------------------------
#draw trees and environment
def draw ():
	#draw 
	
	#goal region
	gx=[xgmin,xgmin,xgmax,xgmax,xgmin]
	gy=[ygmin,ygmax,ygmax,ygmin,ygmin]
	E.cubedraw(gx,gy,xg-epsilon,xg+epsilon,'g')
		
	#draw tree
	G.showtree('0.45')
		 
	#draw path
	G.showpath('ro-')
	G.showtpath('g*-')
	ans = G.returnpath()
		 
	#draw obstacles
	num = int(len(E.x)/4)
	for i in range(1,num+1):
		obx=[E.x[4*(i-1)],E.x[4*(i-1)+1],E.x[4*(i-1)+2],E.x[4*(i-1)+3],E.x[4*(i-1)]]
		oby=[E.y[4*(i-1)],E.y[4*(i-1)+1],E.y[4*(i-1)+2],E.y[4*(i-1)+3],E.y[4*(i-1)]]
		E.cubedraw(obx,oby,E.zmin,E.zmax,'k')
	
		
	#draw  hidden obstacles (if they exist)
	obs_num = int(len(hvx)/4)
	for i in range(1,obs_num+1):
		obsx=[hvx[4*(i-1)],hvx[4*(i-1)+1],hvx[4*(i-1)+2],hvx[4*(i-1)+3],hvx[4*(i-1)]]
		obsy=[hvy[4*(i-1)],hvy[4*(i-1)+1],hvy[4*(i-1)+2],hvy[4*(i-1)+3],hvy[4*(i-1)]]
		E.cubedraw(obx,oby,E.zmin,E.zmax,'k--')
	plt.show()


#--------------------------------------RRT Implementation---------------------------------
def main():
	
	#balance between extending and biasing	
	for i in range(0,nmax):
		if i%10!=0: G.expand()
		else: G.bias()
	#check if sample is in goal, if so STOP!		
		if E.ingoal()==1:
			print('found')
			break
	G.path_to_goal()
	G.prun()
	test_ans=G.returnpath()
	print("test_ans: ",test_ans)
	return test_ans
		
	#display initial plan under limited sensing
	# draw()
	
	

	
	
# run main when RRT is called
if __name__ == '__main__':
    main()
	# run_rtt_api()