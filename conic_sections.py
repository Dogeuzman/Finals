import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20,20)
y = np.linspace(-20,20)
x,y = np.meshgrid(x,y)
fig,ax=plt.subplots()

def axes():
    plt.axhline(0, alpha = .1)
    plt.axvline(0, alpha = .1)
    

def rightLeftParabola(h,k,p):
    # RIGHT/LEFT PARABOLAS
    p = p/4
    V = (h,k)
    axes()
    plt.contour(x+V[0], y+V[1], (y**(2) - 4*p*x), [0], colors='k')
    # Focus.
    plt.plot(V[0]+p,V[1], '.-r')
    # Vertex
    plt.plot(V[0],V[1], '.-b')
    # Directrix.
    plt.axvline(-p+V[0], linestyle='--', color='g')
    # Latus rectum
    lr1 = V[1]+(2*p)
    lr2 = V[1]-(2*p)
    ax.vlines(V[0]+p,lr1,lr2, linestyle='-.', color='m')
    plt.show()

def upDownParabola(h,k,p):
    # UPWARD/DOWNWARD PARABOLA
    p = p/4
    V = (h,k)
    axes()
    plt.contour(x+V[0], y+V[1], (x**(2) - 4*p*y), [0], colors='k')
    # Focus.
    plt.plot(V[0],V[1]+p, '.-r')
    # Vertex
    plt.plot(V[0],V[1], '.-b')
    # Directrix.
    plt.axhline(-p+V[1], linestyle='--', color='g')
    # Latus rectum
    lr1 = V[0]+2*p
    lr2 = V[0]-2*p
    ax.hlines(V[1]+p,lr1,lr2, linestyle='-.', color='m')
    plt.show()

def circle(h,k,r2):
    # CIRCLE
    C = (h,k)
    axes()
    plt.contour(x+C[0], y+C[1], (x**2 + y**2), [r2], colors='k')
    plt.plot(C[0],C[1],'.-r')
    plt.show()


def ellipseXmaj(a,b,h,k):
    # ELLIPSE X-MAJOR
    C  = (h,k)
    axes()
    plt.contour(x+C[0], y+C[1], (x**2/a**2 + y**2/b**2), [1], colors='k')
    #Foci
    c = np.sqrt(a**2 - b**2)
    plt.plot(C[0]+c, C[1], '.-r')
    plt.plot(C[0]-c, C[1], '.-r')
    #Center
    plt.plot(C[0],C[1],'.-r')
    #Vertices
    plt.plot(C[0]+a,C[1],'.-b')
    plt.plot(C[0]-a,C[1],'.-b')
    #Latera Recti
    lr1 = b**2/a
    lr2 = -b**2/a
    ax.vlines(C[0]+c, C[1]+lr1,C[1]+lr2, linestyle='--', color='g')
    ax.vlines(C[0]-c, C[1]+lr1,C[1]+lr2, linestyle='--', color='g')
    plt.show()

def ellipseYmaj(a,b,h,k):
    # ELLIPSE Y-MAJOR  
    C  = (h,k)
    axes()
    plt.contour(x+C[0], y+C[1], (x**2/a**2 + y**2/b**2), [1], colors='k')
    # Foci 
    c = np.sqrt(b**2 - a**2)
    plt.plot(C[0], C[1]-c, '.-r', C[0], C[1]+c, '.-r')
    # Center 
    plt.plot(C[0],C[1],'.-r')
    # Vertices
    plt.plot(C[0],C[1]+b,'.-b')
    plt.plot(C[0],C[1]-b,'.-b')
    #Latera Recti
    lr1 = a**2/b
    lr2 = -a**2/b
    ax.hlines(C[1]+c, C[0]+lr1,C[0]+lr2,'b', linestyle='--', color='g')
    ax.hlines(C[1]-c, C[0]+lr1,C[0]+lr2,'b', linestyle='--', color='g')
    plt.show()

def hyperbolaXmaj(a,b,h,k):
    # HYPERBOLA X-AXIS
    C = (h,k)
    axes()
    plt.contour(x+C[0], y+C[1], (x**2/a**2 - y**2/b**2), [1], colors='k')
    # Foci
    c = np.sqrt(a**2 + b**2)
    plt.plot(C[0]+c, C[1], '.-r', C[0]-c, C[1], '.-r')
    # Center
    plt.plot(C[0],C[1],'.-r')
    # Vertices
    plt.plot(C[0]+a,C[1],'.-b')
    plt.plot(C[0]-a,C[1],'.-b')
    #Asymptotes
    plt.plot(C[0]+x[0,:], C[1]+b/a*x[0,:], '--', alpha=.3)
    plt.plot(C[0]+x[0,:], C[1]-b/a*x[0,:], '--', alpha=.3)
    plt.show()

def hyperbolaYmaj(a,b,h,k):
    # HYPERBOLA Y-AXIS
    C = (h,k)
    axes()
    plt.contour(x+C[0], y+C[1], (y**2/a**2 - x**2/b**2), [1], colors='k')
    # Foci
    c = np.sqrt(a**2 + b**2)
    plt.plot(C[0], C[1]+c, '.-r', C[0], C[1]-c, '.-r')
    # Center
    plt.plot(C[0],C[1],'.-r')
    # Vertices
    plt.plot(C[0],C[1]+a,'.-b')
    plt.plot(C[0],C[1]-a,'.-b')
    #Asymptotes
    plt.plot(C[0]+b/a*x[0,:], C[1]+x[0,:], '--', alpha=.3)
    plt.plot(C[0]-b/a*x[0,:], C[1]+x[0,:], '--', alpha=.3)
    plt.show()