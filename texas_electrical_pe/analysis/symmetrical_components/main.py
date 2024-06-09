import cmath
import numpy as np

def symmetrical_components(phasors):
    """
    Calculate the symmetrical components of a set of unsymmetrical phasors.
    
    Parameters:
    phasors (list of complex): List of unsymmetrical phasors (phasor_A, phasor_B, phasor_C)
    
    Returns:
    tuple: Positive sequence, negative sequence, and zero sequence components
    """
    a = cmath.exp(1j * 2 * cmath.pi / 3)
    A = np.array([
        [1, 1, 1],
        [1, a, a**2],
        [1, a**2, a]
    ], dtype=complex)
    
    phasor_matrix = np.array(phasors, dtype=complex).reshape(3, 1)
    components = np.linalg.inv(A).dot(phasor_matrix)
    
    return components[0, 0], components[1, 0], components[2, 0]

def resolve_unsymmetrical_phasors(phasor_A, phasor_B, phasor_C):
    """
    Resolve a set of unsymmetrical phasors into a set of 3-phase symmetrical phasors.
    
    Parameters:
    phasor_A (complex): Phasor A
    phasor_B (complex): Phasor B
    phasor_C (complex): Phasor C
    
    Returns:
    tuple: Positive sequence, negative sequence, and zero sequence components
    """
    positive_seq, negative_seq, zero_seq = symmetrical_components([phasor_A, phasor_B, phasor_C])
    
    return positive_seq, negative_seq, zero_seq

def construct_unsymmetrical_phasors(positive_seq, negative_seq, zero_seq):
    """
    Construct a set of unsymmetrical phasors from a set of 3-phase symmetrical phasors.
    
    Parameters:
    positive_seq (complex): Positive sequence component
    negative_seq (complex): Negative sequence component
    zero_seq (complex): Zero sequence component
    
    Returns:
    tuple: Phasor A, Phasor B, Phasor C
    """
    a = cmath.exp(1j * 2 * cmath.pi / 3)
    A_inv = np.array([
        [1, 1, 1],
        [1, a**2, a],
        [1, a, a**2]
    ], dtype=complex)
    
    components = np.array([zero_seq, positive_seq, negative_seq], dtype=complex).reshape(3, 1)
    phasors = A_inv.dot(components)
    
    return phasors[0, 0], phasors[1, 0], phasors[2, 0]

if __name__ == "__main__":
    pass
