#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

#plt.rcParams['legend.loc'] = 'best'
#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')

ano = 30.*12.*86400.
mes = 30.*86400.

# Perfil de pressão

inDataLegendP = np.loadtxt('./testeDS/passosPressaoBlocoMacro.dat',unpack=True)
dataLegendP = inDataLegendP[1:]
pnum = len(dataLegendP)
Px0 = np.zeros(pnum)
#pData = np.loadtxt('./expTeste/fort.1111',unpack=True)
#Pr = pData[0]
#Pw = pData[1]
#PI = pData[2]

fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax = fig.add_subplot(111, projection='3d')

ax = plt.subplot(111)

for i in range(1,pnum+1):
    #i_mask = 10*i
    inDataNameP = './testeDS/solP.%d' % i
    xx, yy, P = np.loadtxt(inDataNameP,unpack=True,usecols=[2,3,4])
    print xx
    print yy
    print P
    #fig = plt.figure()
    #ax = fig.gca(projection='3d')
    #ax = fig.add_subplot(111, projection='3d')
    
    if dataLegendP[i-1] == 1.:
        leg = (u"%d mês" % dataLegendP[i-1])
    else:
        leg = ("%d meses" % dataLegendP[i-1])
    Px0[i-1] = P[0]
    #ax.plot(xx,yy,P,'o',label=leg)
    ax.plot(xx,P,'-o',label=leg)
    
    #surf = ax.plot_surface(xx, yy, P, rstride=1, cstride=1, cmap=cm.coolwarm,
        #linewidth=0, antialiased=True)
    #surf = ax.plot_surface(xx, yy, P)
    #plt.show()
    #plt.pcolor(xx,yy,P)
    #ax.contour(xx, yy, P)
    #plt.savefig('./teste/tmpPressao%d.pdf' % i_mask)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel(r'$x^{*}$',fontsize=18)
#ax.set_ylabel('$y^{*}$',fontsize=18)
ax.set_ylabel(r'$p^{*}$',fontsize=18)

#plt.xlabel('$x^{*}$',fontsize=18)
#plt.ylabel('$p^{*}$',fontsize=18,rotation='horizontal')
#plt.grid(b=True, which='major', color='k', linestyle='--')
#ax.legend()
plt.savefig('./testeDS/tmpPressao.pdf')
plt.show()

fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax = fig.add_subplot(111, projection='3d')

ax = plt.subplot(111)

for i in range(1,pnum+1):
    #i_mask = 11*i
    inDataNameGradP = './testeDS/gradPx.%d' % i
    xx, yy, gradP = np.loadtxt(inDataNameGradP,unpack=True,usecols=[2,3,4])
    print xx
    print yy
    print gradP
    #fig = plt.figure()
    #ax = fig.gca(projection='3d')
    #ax = fig.add_subplot(111, projection='3d')
    if dataLegendP[i-1] == 1.:
        leg = (u"%d mês" % dataLegendP[i-1])
    else:
        leg = ("%d meses" % dataLegendP[i-1])
    Px0[i-1] = P[0]
    #ax.plot(xx,yy,gradP,'o',label=leg)
    ax.plot(xx,gradP,'-o',label=leg)
    #surf = ax.plot_surface(xx, yy, P, rstride=1, cstride=1, cmap=cm.coolwarm,
        #linewidth=0, antialiased=True)
    #surf = ax.plot_surface(xx, yy, P)
    #plt.show()
    #plt.pcolor(xx,yy,P)
    #ax.contour(xx, yy, P)
    #plt.savefig('./teste/tmpPressao%d.pdf' % i_mask)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel(r'$x^{*}$',fontsize=18)
#ax.set_ylabel('$y^{*}$',fontsize=18)
ax.set_ylabel(r"$\nabla^* p^{*}$",fontsize=18)
#plt.xlabel('$x^{*}$',fontsize=18)
#plt.ylabel('$p^{*}$',fontsize=18,rotation='horizontal')
#plt.grid(b=True, which='major', color='k', linestyle='--')
#ax.legend()
plt.savefig('./testeDS/tmpgradPressao.pdf')
plt.show()

fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax = fig.add_subplot(111, projection='3d')

ax = plt.subplot(111)

for i in range(1,pnum+1):
    #i_mask = 14*i
    inDataNameV = './testeDS/solVelocity_x.%d' % i
    xx, yy, V = np.loadtxt(inDataNameV,unpack=True,usecols=[2,3,4])
    print xx
    print yy
    print V
    #fig = plt.figure()
    #ax = fig.gca(projection='3d')
    #ax = fig.add_subplot(111, projection='3d')
    if dataLegendP[i-1] == 1.:
        leg = (u"%d mês" % dataLegendP[i-1])
    else:
        leg = ("%d meses" % dataLegendP[i-1])
    Px0[i-1] = P[0]
    #ax.plot(xx,yy,V,'o',label=leg)
    ax.plot(xx,V,'-o',label=leg)
    #surf = ax.plot_surface(xx, yy, P, rstride=1, cstride=1, cmap=cm.coolwarm,
        #linewidth=0, antialiased=True)
    #surf = ax.plot_surface(xx, yy, P)
    #plt.show()
    #plt.pcolor(xx,yy,P)
    #ax.contour(xx, yy, P)
    #plt.savefig('./teste/tmpPressao%d.pdf' % i_mask)

box = ax.get_position()
ax.set_position([0.3*box.x0+box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel(r'$x^{*}$',fontsize=18)
#ax.set_ylabel('$y^{*}$',fontsize=18)
ax.set_ylabel(r"$u_D\,(m/s)$",fontsize=18)
#plt.xlabel('$x^{*}$',fontsize=18)
#plt.ylabel('$p^{*}$',fontsize=18,rotation='horizontal')
#plt.grid(b=True, which='major', color='k', linestyle='--')
#ax.legend()
plt.savefig('./testeDS/tmpV.pdf')
plt.show()

fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax = fig.add_subplot(111, projection='3d')

ax = plt.subplot(111)


for i in range(1,pnum+1):
    #i_mask = 19*i
    inDataNameJ = './testeDS/nodeFlux_x.%d' % i
    xx, yy, J = np.loadtxt(inDataNameJ,unpack=True,usecols=[2,3,4])
    print xx
    print yy
    print J
    #fig = plt.figure()
    #ax = fig.gca(projection='3d')
    #ax = fig.add_subplot(111, projection='3d')
    if dataLegendP[i-1] == 1.:
        leg = (u"%d mês" % dataLegendP[i-1])
    else:
        leg = ("%d meses" % dataLegendP[i-1])
    Px0[i-1] = P[0]
    #ax.plot(xx,yy,J,'.',label=leg)
    #ax.plot(xx,yy,J,'o',label=leg)
    ax.plot(xx,J,'-o',label=leg)
    #surf = ax.plot_surface(xx, yy, P, rstride=1, cstride=1, cmap=cm.coolwarm,
        #linewidth=0, antialiased=True)
    #surf = ax.plot_surface(xx, yy, P)
    #plt.show()
    #plt.pcolor(xx,yy,P)
    #ax.contour(xx, yy, P)
    #plt.savefig('./teste/tmpPressao%d.pdf' % i_mask)

box = ax.get_position()
ax.set_position([0.2*box.x0+box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel('$x^{*}$',fontsize=18)
#ax.set_ylabel(r'$y^{*}$',fontsize=18)
ax.set_ylabel(r'$J \,\left(\frac{kg}{m^2 s}\right)$',fontsize=18)
#plt.xlabel('$x^{*}$',fontsize=18)
#plt.ylabel('$p^{*}$',fontsize=18,rotation='horizontal')
#plt.grid(b=True, which='major', color='k', linestyle='--')
#ax.legend()
plt.savefig('./testeDS/tmpJ.pdf')
plt.show()

fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax = fig.add_subplot(111, projection='3d')

ax = plt.subplot(111)


for i in range(1,pnum+1):
    #i_mask = 23*i
    inDataNameResid = './testeDS/residueFlux_x.%d' % i
    xx, yy, Resid = np.loadtxt(inDataNameResid,unpack=True,usecols=[2,3,4])
    print xx
    print yy
    print Resid
    #fig = plt.figure()
    #ax = fig.gca(projection='3d')
    #ax = fig.add_subplot(111, projection='3d')
    if dataLegendP[i-1] == 1.:
        leg = (u"%d mês" % dataLegendP[i-1])
    else:
        leg = ("%d meses" % dataLegendP[i-1])
    Px0[i-1] = P[0]
    #ax.plot(xx,yy,J,'.',label=leg)
    #ax.plot(xx,yy,J,'o',label=leg)
    ax.plot(xx,Resid,'-o',label=leg)
    #surf = ax.plot_surface(xx, yy, P, rstride=1, cstride=1, cmap=cm.coolwarm,
        #linewidth=0, antialiased=True)
    #surf = ax.plot_surface(xx, yy, P)
    #plt.show()
    #plt.pcolor(xx,yy,P)
    #ax.contour(xx, yy, P)
    #plt.savefig('./teste/tmpPressao%d.pdf' % i_mask)

box = ax.get_position()
ax.set_position([0.2*box.x0+box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel('$x^{*}$',fontsize=18)
#ax.set_ylabel(r'$y^{*}$',fontsize=18)
ax.set_ylabel(u'Resíduo',fontsize=18)
#plt.xlabel('$x^{*}$',fontsize=18)
#plt.ylabel('$p^{*}$',fontsize=18,rotation='horizontal')
#plt.grid(b=True, which='major', color='k', linestyle='--')
#ax.legend()
plt.savefig('./testeDS/tmpResid.pdf')
plt.show()

# Produção do bloco
fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax = fig.add_subplot(111, projection='3d')

ax = plt.subplot(111)

inDataNameJprod = './testeDS/echoProducao.dat'
dt, Jprod = np.loadtxt(inDataNameJprod,unpack=True,usecols=[1,5])
dt = dt/mes
ax.set_xlabel(r'$t\,(meses)$',fontsize=18)
ax.set_ylabel(r'$Produ \c c \~ a o\, \left(kg\right)$',fontsize=16)
ax.plot(dt,Jprod,'-o',label=u'Produção')
box = ax.get_position()
ax.set_position([0.1*box.x0+box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig('./testeDS/Prod.pdf')
plt.show()

# RF barra
fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax = fig.add_subplot(111, projection='3d')

ax = plt.subplot(111)

inDataNameRF_ = './testeDS/echoProducao.dat'
dt, RF_ = np.loadtxt(inDataNameRF_,unpack=True,usecols=[1,6])
dt = dt/mes
ax.set_xlabel(r'$t\,(meses)$',fontsize=18)
ax.set_ylabel(r'$RF_{recuper\'avel}$',fontsize=16)
ax.plot(dt,RF_,'-o',label=u'RF')
box = ax.get_position()
ax.set_position([0.1*box.x0+box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig('./testeDS/RF_.pdf')
plt.show()

# RF
fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax = fig.add_subplot(111, projection='3d')

ax = plt.subplot(111)

inDataNameRF = './testeDS/echoProducao.dat'
dt, RF = np.loadtxt(inDataNameRF,unpack=True,usecols=[1,7])
dt = dt/mes
ax.set_xlabel(r'$t\,(meses)$',fontsize=18)
ax.set_ylabel(r'$RF_{total}$',fontsize=16)
ax.plot(dt,RF,'-o',label=u'RF')
box = ax.get_position()
ax.set_position([0.1*box.x0+box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig('./testeDS/RF.pdf')
plt.show()