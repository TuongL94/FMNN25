#  Before you use this file, install mpi4py on your computer
#  anaconda users do this like that:    conda install mpi4py
#
#  in a command window execute then the following command
#
#  mpiexec -n 2 python ~/Desktop/inspect.py
#  (replace "Desktop" by the path o this file and replace the number of
#  processors from 2 to the number you want.)


from mpi4py import MPI
from scipy import *

def doCalculation(stepsize=0.05,numbIter=10,omega=0.8):
    '''
    do the calculation of the heat distribution
    stepsize=distance to the next node
    numberIter=number of iterationsteps
    omega=relaxation-parameter
    '''
    arrRooms=array([[1,1],[2,1],[1,1]])
    numberRooms=len(arrRooms)
    comm=MPI.COMM_WORLD
    rank=comm.Get_rank()
    np=comm.size
    #case to less cpu's
    if np<numberRooms:
        #throw error?
    #case too much cpus (just end the processes on cpu's with higher rank)
    if rank>numberRooms:
        return None
    myRoomNumber=rank
    #do initialization of the rooms and the borders - how to initialize the
    #interface???
    #pseudocode
    '''
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
            mesh.solve()
            #send the information to the prev/next room
            sendInterfaceInfo(myRoomNumber)
            #do relaxation here?
            #reveive the information to the prev/next room
            receiveInterfaceInfo(myRoomNumber)
            #or do relaxation here?
        #(even rooms)
        else:
            #reveive the information to the prev/next room
            receiveInterfaceInfo(myRoomNumber)
            #solve the system
            mesh.solve()
            #send the information to the prev/next room
            sendInterfaceInfo(myRoomNumber)
            #do relaxation
def sendInterfaceInfo(myRoomNumber):
    '''
        send the information to the next/previous room (if they exist)
    '''
    #send information to the previous room (if there is a prev room)
    if 0<myRoomNumber:
        sendbuffer1=interface[myRoomNumber,1].getValues()
        comm.send(sendbuffer1,myRoomNumber-1,0)
    #send information to the next room (if there is a next room)
    if numberRooms>myRoomNumber+1:
        sendbuffer2=interface[myRoomNumber,2].getValues()
        comm.send(sendbuffer1,(myRoomNumber-1)%numberRooms,0)
def receiveInterfaceInfo(myRoomNumber):
    '''
        receive the information to the next/previous room (if they exist)
    '''
    #receive information from the previous room (if there is a prev room)
    if 0<myRoomNumber:
        status = MPI.Status()
        receiveBuffer1=comm.recv(source=(myRoomNumber-1),status=status)
        interface[myRoomNumber,1].setValues(receiveBuffer1)
    #receive information from the next room (if there is a next room)
    if numberRooms>myRoomNumber+1:
        status = MPI.Status()
        receiveBuffer2=comm.recv(source=(myRoomNumber+1),status=status)
        interface[myRoomNumber,2].setValues(receiveBuffer2)

#run the calculation
doCalculation();