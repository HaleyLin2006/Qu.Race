from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import pygame
from Button import Button 
from numpy import pi

pygame.init()

class Q_Circuit():
    def __init__(self, qubits):
        qubit = QuantumRegister(qubits,'q')
        for i in range(qubits):
            bits = ClassicalRegister(i, 'c')
            circuit = QuantumCircuit(qubit, bits)
        return circuit

#Gates
    #1 Qubit
    def H(self, circuit, q_circuit, qubit):
        circuit.h(q_circuit[qubit])

    def NOT(self, circuit, q_circuit, qubit):
        circuit.x(q_circuit[qubit])

    def Y(self, circuit, q_circuit, qubit):
        circuit.y(q_circuit[qubit])

    def Z(self, circuit, q_circuit, qubit):
        circuit.z(q_circuit[qubit])

    #2 Qubit
    def CNOT(self, circuit, q_circuit, q_1, q_2):
        circuit.cx(q_circuit[q_1], q_circuit[q_2])
    
    def Swap(self, circuit, q_circuit, q_1, q_2):
        circuit.swap(q_circuit[q_1], q_circuit[q_2])
    #Phase
    #pi/4
    def S(self, circuit, q_circuit, qubit):
        circuit.s(q_circuit[qubit])
    #pi/2
    def T(self, circuit, q_circuit, qubit):
        circuit.t(q_circuit[qubit])

