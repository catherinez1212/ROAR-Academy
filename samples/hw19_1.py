import gym
import numpy as np

# PID Controller class
class PID:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.previous_error = 0
        self.integral = 0

    def compute(self, setpoint, measured_value):
        # Calculate error
        error = setpoint - measured_value
        
        # Proportional term
        P = self.Kp * error
        
        # Integral term
        self.integral += error
        I = self.Ki * self.integral
        
        # Derivative term
        derivative = error - self.previous_error
        D = self.Kd * derivative
        
        # Update previous error
        self.previous_error = error
        
        # Calculate control signal
        control_signal = P + I + D
        return control_signal

if __name__ == "__main__":
    env = gym.make('CartPole-v1')
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    
    # PID controller parameters
    Kp = 0.5
    Ki = 0
    Kd = 1.0
    
    pid = PID(Kp, Ki, Kd)
    
    EPISODES = 100
    
    for e in range(EPISODES):
        state = env.reset()
        done = False
        score = 0
        
        while not done:
            env.render()
            
            # Extract the pole angle (state[2]) and angular velocity (state[3])
            pole_angle = state[2]
            pole_angle_velocity = state[3]
            
            # Compute control signal using PID controller
            control_signal = pid.compute(0, pole_angle)  # Desired angle is 0
            
            # Determine action based on control signal
            action = 1 if control_signal > 0 else 0
            
            # Take action in the environment
            next_state, reward, done, _ = env.step(action)
            
            state = next_state
            score += reward
            
            if done:
                print("episode: {}/{}, score: {}".format(e+1, EPISODES, score))
                break

    env.close()
