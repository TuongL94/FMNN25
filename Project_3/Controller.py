"""
@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""


from mpi4py import MPI
from scipy import *
from Node import NodeType,Node
from Interface import Interface
from MeshWithSolve import Mesh
#import os

#def include(filename):
#    if os.path.exists(filename): 
#        exec(compile(open(filename).read()))
from plot import plotWholeRoom

#include('plot.py')

def doCalculation(stepsize=0.05,numbIter=10,omega=0.8,):
    '''
    do the calculation of the heat distribution
    stepsize=distance to the next node
    numberIter=number of iterationsteps
    omega=relaxation-parameter
    returns a mesh with the distribution of the temperature
    '''
    #arrRooms==array with the dimensions of the room
    arrRooms=array([[1,1],[2,1],[1,1]])
    #arrInterfaceTypes==types of the interfaces you are using (need always contain two values!)
    arrInterfaceTypesRec=array([[None,NodeType.NEUMANN],[NodeType.DIRICHLET,NodeType.DIRICHLET],[NodeType.NEUMANN,None]])
    arrInterfaceTypesSend=array([[None,NodeType.DIRICHLET],[NodeType.NEUMANN,NodeType.NEUMANN],[NodeType.DIRICHLET,None]])
    numberRooms=len(arrRooms)
    comm=MPI.COMM_WORLD
    myRoomNumber=comm.Get_rank()
    np=comm.size
    #case to less cpu's
    if np<numberRooms:
        #case if there are not enough cpu's to split it up in that way we are doing it
        raise Exception('We need more CPU`s for doing the calculation!')
    #case too much cpus (just end the processes on cpu's with higher rank)
    if myRoomNumber>numberRooms:
        return None
    #do initialization of the rooms and the borders
    if myRoomNumber==0:
        from initRoom1 import initRoom1        
        #include('initRoom1.py')
        mesh=initRoom1()
    if myRoomNumber==1:
        from initRoom2 import initRoom2
        #include('initRoom2.py')
        mesh=initRoom2()
    if myRoomNumber==2:
        from initRoom3 import initRoom3
        #include('initRoom3.py')
        mesh=initRoom3()
    
    
    #do the initialization of the interfaces
    interfaces=array([None,None])
    #just initialize my interfaces
    #rooms on the left side
    if(myRoomNumber!=0):
        if myRoomNumber%2!=0:
            #odd rooms have the interface on the bottom (use floor, because you need more the edges as well!)
            indices=[(j,0) for j in range(math.floor(mesh.y_res/2),mesh.y_res)]
            interfaces[0]=Interface(mesh,indices)
        else:
            #even rooms on the top (have the whole border as an interface)
            indices=[(j,0) for j in range(0,mesh.y_res)]
            interfaces[0]=Interface(mesh,indices)
    #rooms on the right side
    if(myRoomNumber!=numberRooms-1):
        if myRoomNumber%2!=0:
            #odd rooms have the interface on the top (use round, because you need more the edges as well!)
            indices=[(j,mesh.x_res-1) for j in range(0,round(mesh.y_res/2)+1)]
            interfaces[1]=Interface(mesh,indices)
        else:
            #even rooms on the bottom (have the whole border as an interface)
            indices=[(j,mesh.x_res-1) for j in range(0,mesh.y_res)]
            interfaces[1]=Interface(mesh,indices)
    '''
    pseudocode
    store previous send data
    while not solved: (count<10?)
        if myRoomNumber%2!=0: #(odd rooms)
            then do calculation
            and then send to neighbours (if nothing has changed=>send finished flag)
            if nothing has changed => return
            otherwise receiveInformation from neighbours
            if received info==finished flag =>done
        else: #(even rooms)
            otherwise receiveInformation from neighbours
            if received info==finished flag =>done
            then do calculation
            and then send to neighbours (if nothing has changed=>send finished flag)
            if nothing has changed => return
    '''
    count=0
    while count<numbIter:
        #(odd rooms)
        if myRoomNumber%2!=0:
            #solve the system
            mesh.solveMesh()
            #send the information to the prev/next room
            sendInterfaceInfo(comm,myRoomNumber,numberRooms,interfaces,arrInterfaceTypesSend[myRoomNumber])
            #reveive the information to the prev/next room
            receiveInterfaceInfo(comm,myRoomNumber,numberRooms,interfaces,arrInterfaceTypesRec[myRoomNumber])
            mesh.doRelaxation(omega)
        #(even rooms)
        else:
            #reveive the information to the prev/next room
            receiveInterfaceInfo(comm,myRoomNumber,numberRooms,interfaces,arrInterfaceTypesRec[myRoomNumber])
            #solve the system
            mesh.solveMesh()
            #send the information to the prev/next room
            sendInterfaceInfo(comm,myRoomNumber,numberRooms,interfaces,arrInterfaceTypesSend[myRoomNumber])
            #do relaxation
            mesh.doRelaxation(omega)
        count=count+1
    return mesh

def sendInterfaceInfo(comm,myRoomNumber,numberRooms,interfaces,nodeTypes):
    '''
        send the information to the next/previous room (if they exist)
    '''
    #send information to the previous room (if there is a prev room)
    if 0<myRoomNumber:
        sendbuffer1=interfaces[0].getValues(nodeTypes[0])
        comm.send(sendbuffer1,myRoomNumber-1,0)
        
    #send information to the next room (if there is a next room)
    if numberRooms>myRoomNumber+1:
        sendbuffer2=interfaces[1].getValues(nodeTypes[1])
        comm.send(sendbuffer2,myRoomNumber+1,0)
def receiveInterfaceInfo(comm,myRoomNumber,numberRooms,interfaces,nodeTypes):
    '''
        receive the information to the next/previous room (if they exist)
    '''
    #receive information from the previous room (if there is a prev room)
    if 0<myRoomNumber:
        status = MPI.Status()
        receiveBuffer1=comm.recv(source=(myRoomNumber-1),status=status)
        interfaces[0].setValues(receiveBuffer1,nodeTypes[0])
    #receive information from the next room (if there is a next room)
    if numberRooms>myRoomNumber+1:
        status = MPI.Status()
        receiveBuffer2=comm.recv(source=(myRoomNumber+1),status=status)
        interfaces[1].setValues(receiveBuffer2,nodeTypes[1])

#run the calculation
mesh=doCalculation()
plotWholeRoom(mesh)
