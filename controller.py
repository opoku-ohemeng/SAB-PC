import numpy as np
from .model import nx, nu, A, B

Q = np.eye(nx)
R = 0.5 * np.eye(nu)

K_lqr = -np.linalg.inv(R) @ B.T @ Q

K_base = 0.08 * K_lqr
K_sab = 0.35 * K_lqr

K_base_modes = [K_base, K_base, K_base]
K_sab_modes  = [K_sab,  K_sab,  K_sab]

def Acl_baseline(A, B, K):
    return A + B @ K

def Acl_sab(A, B, K, d):
    A_pred = np.linalg.matrix_power(A, max(int(d), 0))
    return A + B @ K @ A_pred
