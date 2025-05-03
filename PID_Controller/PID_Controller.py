import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define the plant (e.g., a simple first-order system)
# G(s) = 1 / (s + 1)
plant = ctrl.TransferFunction([1], [1, 1])

# PID controller gains
Kp = 100   # Proportional gain
Ki = 0    # Integral gain
Kd = 0    # Derivative gain

# Define the Laplace variable s
s = ctrl.TransferFunction([1, 0], [1])

# Define the PID controller transfer function G_PID(s) = Kp + Ki/s + Kd*s
pid_controller = Kp + Ki / s + Kd * s

# Closed-loop transfer function
closed_loop = ctrl.feedback(pid_controller * plant, 1)

# Time array for simulation
time = np.linspace(0, 10, 1000)

# Generate a step response for the closed-loop system
time, response = ctrl.step_response(closed_loop, time)

# Plot the response
plt.figure(figsize=(8, 6))
plt.plot(time, response, label='PID Controlled Response')
plt.axhline(y=1, color='r', linestyle='--', label='Setpoint (1)')
plt.title('PID Controller Step Response')
plt.xlabel('Time [s]')
plt.ylabel('Output')
plt.legend()
plt.grid(True)
plt.show()
