# Capstone Project: Voice-to-Manipulation Task

This capstone project integrates all the concepts learned throughout the textbook to build an autonomous humanoid robot capable of performing a voice-to-manipulation task.

## Project Goal

The goal is to enable your simulated humanoid robot to:
1.  Receive a natural language voice command (e.g., "pick up the red block from the table").
2.  Perceive its environment using its sensors (e.g., camera, LiDAR).
3.  Utilize an LLM for high-level task planning and decomposition.
4.  Navigate to the object's location.
5.  Identify and grasp the specified object.
6.  Potentially place it in another designated location.

## Walkthrough Steps

### 1. Environment Setup

Ensure your Isaac Sim environment (`capstone_env.py`) is set up with the humanoid robot and manipulable objects.

### 2. Voice Command Processing

Integrate the `voice_to_action_pipeline.py` to:
-   Simulate or integrate a speech recognition system.
-   Feed the text command to an LLM for task decomposition.
-   Receive high-level planned steps from the LLM.

### 3. Robot Action Execution

Develop or extend the `robot_action_server.py` to:
-   Interpret the planned steps from the LLM.
-   Translate them into a sequence of low-level ROS 2 actions (e.g., navigation goals, joint trajectories for grasping).
-   Execute these actions on the simulated robot.

### 4. Perception Integration

Integrate the VSLAM and object detection capabilities (from Module 3) to enable the robot to perceive its environment and identify the target object.

### 5. Bringing it All Together

Combine all components to demonstrate a full "voice-to-manipulation" pipeline.

## Evaluation

Your project will be evaluated based on the robot's ability to successfully:
-   Understand and decompose various voice commands.
-   Navigate to target objects.
-   Identify and manipulate objects in the environment.
