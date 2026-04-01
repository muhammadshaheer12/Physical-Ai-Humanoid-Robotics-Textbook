# Data Model: Physical AI & Humanoid Robotics Textbook

This document describes the key entities and their relationships within the "Physical AI & Humanoid Robotics Textbook" project. This is a conceptual data model focused on the structure and content of the educational material, rather than a software-specific database schema.

## Entities

### 1. Textbook

Represents the entire educational offering.

-   **Name**: Textbook
-   **Description**: The complete educational curriculum, including all modules, projects, and learning materials. It encapsulates the overall pedagogical approach and learning outcomes.
-   **Attributes**:
    -   `title`: (String) "Physical AI & Humanoid Robotics Textbook"
    -   `theme`: (String) "AI systems operating in the physical world through embodied intelligence."
    -   `goal`: (String) The primary educational objective for students.
    -   `target_audience`: (List of Strings) Describes the intended learners (e.g., advanced undergraduate, graduate).
    -   `pedagogical_approach`: (List of Strings) Key teaching methods (e.g., concept-first, hands-on).
    -   `outcome`: (String) The overall student capability after completing the textbook.
-   **Relationships**:
    -   `has_many` Modules (One-to-Many)
    -   `has_many` Projects (Implicit, within Modules)

### 2. Module

A discrete unit of the textbook content.

-   **Name**: Module
-   **Description**: A self-contained section of the textbook focusing on a specific technology or concept stack (e.g., ROS 2, Digital Twins, VLA). Each module has specific learning objectives.
-   **Attributes**:
    -   `module_number`: (Integer) Unique identifier (1, 2, 3, 4).
    -   `title`: (String) Name of the module (e.g., "The Robotic Nervous System (ROS 2)").
    -   `focus`: (String) Main area of learning for the module.
    -   `key_topics`: (List of Strings) Detailed list of subjects covered.
    -   `learning_outcome`: (String) What students will be able to do after completing the module.
-   **Relationships**:
    -   `belongs_to` Textbook (Many-to-One)
    -   `may_contain` Projects (One-to-One or One-to-Many, especially the Capstone)

### 3. Robot Model (URDF)

A critical asset for hands-on learning.

-   **Name**: Robot Model (URDF - Unified Robot Description Format)
-   **Description**: A standardized XML-based file defining the robot's physical structure (links, joints), visual properties, collision properties, and inertial properties. It is central to simulation and real-world deployment.
-   **Attributes**:
    -   `name`: (String) Unique identifier for the robot model.
    -   `description_file_path`: (String) Relative path to the `.urdf` or `.xacro` file in the GitHub repository.
    -   `components`: (List of Strings) List of major parts (e.g., "arms", "legs", "head", "sensors").
    -   `physical_properties`: (Implicit) Defined within URDF (mass, inertia, etc.).
    -   `joint_definitions`: (Implicit) Defined within URDF (type, limits, etc.).
-   **Relationships**:
    -   `used_in` Module (Many-to-Many, likely multiple modules use/build upon robot models)
    -   `instantiated_in` Digital Twin (One-to-Many)

### 4. Digital Twin

The simulated environment for robot testing.

-   **Name**: Digital Twin
-   **Description**: A high-fidelity simulation of the robot and its environment, including physics (gravity, collisions), sensor data streams, and potentially human-robot interaction. Used for safe testing and development.
-   **Attributes**:
    -   `simulator_platform`: (String) E.g., "Gazebo", "Unity".
    -   `world_file_path`: (String) Relative path to the simulation world definition.
    -   `environmental_elements`: (List of Strings) Objects, terrain, lighting in the simulation.
    -   `physics_parameters`: (Implicit) Gravity, friction coefficients.
    -   `simulated_sensors`: (List of Strings) Types of sensors simulated (e.g., "LiDAR", "Depth Camera").
-   **Relationships**:
    -   `hosts` Robot Model (One-to-Many)
    -   `interacts_with` AI Agent (One-to-Many)

### 5. AI Agent

The "brain" of the robot.

-   **Name**: AI Agent
-   **Description**: The software, primarily written in Python, that constitutes the robot's intelligence. Responsible for interpreting sensor data, making decisions (planning), and issuing commands (control).
-   **Attributes**:
    -   `framework`: (String) E.g., "ROS 2 (`rclpy`)", "NVIDIA Isaac ROS".
    -   `functionality`: (List of Strings) E.g., "Perception", "Navigation", "Task Planning", "Motor Control".
    -   `programming_language`: (String) Python.
    -   `data_inputs`: (List of Strings) Sensor data streams it processes.
    -   `data_outputs`: (List of Strings) Commands it issues (e.g., joint velocities).
-   **Relationships**:
    -   `controls` Robot Model (One-to-One or One-to-Many)
    -   `processes_data_from` Digital Twin (Many-to-Many, via simulated sensors)

### 6. VLA System

A specialized AI Agent for language interaction.

-   **Name**: VLA System (Vision-Language-Action System)
-   **Description**: A specific type of AI agent that integrates vision, language, and action models to perform tasks based on natural language instructions. Enables human-robot interaction through voice commands.
-   **Attributes**:
    -   `components`: (List of Strings) E.g., "Speech Recognition", "Natural Language Understanding (LLM)", "Task Planner", "Motor Control Interface".
    -   `interaction_method`: (String) E.g., "Voice Commands".
    -   `LLM_integration`: (Boolean) Indicates reliance on Large Language Models for planning.
-   **Relationships**:
    -   `is_a` AI Agent (Inheritance)
    -   `utilizes` Robot Model (One-to-One)
    -   `operates_within` Digital Twin (Many-to-One)

## Relationships Overview

-   **Textbook** `has_many` **Modules**.
-   **Modules** `belong_to` **Textbook**.
-   **Modules** `utilize` **Robot Models**, **Digital Twins**, **AI Agents**, and **VLA Systems**.
-   **Robot Models** are `instantiated_in` **Digital Twins**.
-   **AI Agents** `control` **Robot Models** and `process_data_from` **Digital Twins**.
-   **VLA Systems** `are_a_type_of` **AI Agent**.