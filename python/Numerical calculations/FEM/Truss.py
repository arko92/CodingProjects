# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 00:14:01 2023

@author: arkob

Implementation of a TrussElement class in Python, that can be used for Finite Element Method (FEM) analysis on a truss structure

"""

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class TrussElement:
    def __init__(self, node1, node2, area, E):
        self.node1 = node1
        self.node2 = node2
        self.area = area
        self.E = E
        self.length = ((node2.x - node1.x)**2 + (node2.y - node1.y)**2)**0.5

    def compute_stiffness_matrix(self):
        k = self.E * self.area / self.length
        cos_theta = (self.node2.x - self.node1.x) / self.length
        sin_theta = (self.node2.y - self.node1.y) / self.length
        k11 = k * cos_theta**2
        k12 = k * cos_theta * sin_theta
        k21 = k * sin_theta * cos_theta
        k22 = k * sin_theta**2
        return [[k11, k12, -k11, -k12], [k21, k22, -k21, -k22], [-k11, -k21, k11, k21], [-k12, -k22, k12, k22]]

    def compute_local_force_vector(self, Fx, Fy):
        return [Fx, Fy, -Fx, -Fy]

    def compute_global_force_vector(self, T):
        cos_theta = (self.node2.x - self.node1.x) / self.length
        sin_theta = (self.node2.y - self.node1.y) / self.length
        return [T[0]*cos_theta + T[1]*sin_theta, T[0]*sin_theta + T[1]*cos_theta, T[2]*cos_theta + T[3]*sin_theta, T[2]*sin_theta + T[3]*cos_theta]

    def compute_strain(self, T):
        return (T[0] - T[2]) / (self.length * self.E)

    def compute_stress(self, T):
        return self.compute_strain(T) * self.E


# create two nodes
node1 = Node(0, 0)
node2 = Node(1, 0)

# create a truss element between the nodes
truss = TrussElement(node1, node2, area=1, E=1e6)

# compute the stiffness matrix of the element
K = truss.compute_stiffness_matrix()

# apply a force of 1000 N in the x-direction to the element
F = truss.compute_local_force_vector(Fx=1000, Fy=0)

# Compute stress
T = [0, 0, 100, -2]  # displacements
stress = truss.compute_stress(T)
