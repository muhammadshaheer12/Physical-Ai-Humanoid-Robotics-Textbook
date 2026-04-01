# Research: Foundational Decisions for Robotics Textbook

This document outlines the foundational decisions made to ensure a stable, reproducible, and effective learning environment for the "Physical AI & Humanoid Robotics Textbook".

## 1. Software Versioning

**Decision**: The textbook will standardize on the following Long-Term Support (LTS) or latest stable versions to maximize stability and support longevity. All tutorials, code, and installation instructions will be tested against these specific versions.

- **ROS 2**: Humble Hawksbill (LTS)
- **Ubuntu**: 22.04 (Jammy Jellyfish)
- **Gazebo**: Fortress (formerly Ignition)
- **Unity**: 2022.3 LTS
- **NVIDIA Isaac Sim**: 2023.1.1 (or latest stable version at time of writing)
- **Python**: 3.10

**Rationale**: Using LTS versions of ROS 2 and Ubuntu provides a stable base with years of community and security support, reducing the risk of breaking changes for students. The latest stable versions of simulation tools are chosen to provide access to modern features while avoiding bleeding-edge instability.

**Alternatives Considered**:
- Using the absolute latest versions of all software: Rejected due to the high risk of encountering bugs, dependency conflicts, and breaking API changes, which would frustrate learners.
- Supporting multiple versions: Rejected as it would exponentially increase the complexity of the content, testing, and student support.

## 2. Hardware Requirements

**Decision**: The textbook will define both a minimum and a recommended hardware specification.

- **Minimum Specification**:
    - **CPU**: 6-core Intel Core i7 or AMD Ryzen 5
    - **RAM**: 16 GB DDR4
    - **GPU**: NVIDIA GeForce RTX 2060 (6 GB VRAM) with CUDA support
    - **Storage**: 100 GB SSD

- **Recommended Specification**:
    - **CPU**: 8-core Intel Core i9 or AMD Ryzen 7
    - **RAM**: 32 GB DDR4
    - **GPU**: NVIDIA GeForce RTX 3070 or higher (8+ GB VRAM)
    - **Storage**: 200 GB NVMe SSD

**Rationale**: The minimum spec is designed to handle the core ROS 2 and Gazebo simulations. The recommended spec is necessary for a smooth experience with the more demanding NVIDIA Isaac Sim, especially for synthetic data generation and photorealistic rendering. An NVIDIA GPU is a hard requirement for Module 3.

**Alternatives Considered**:
- Lowering the minimum spec: Rejected because it would lead to a poor user experience, with slow simulation speeds and potential crashes, hindering the learning process.
- Not specifying a recommended spec: Rejected because it would not give students a clear target for optimal performance, especially for the advanced modules.

## 3. Code and Asset Distribution

**Decision**: All source code, URDF files, simulation worlds, configuration files, and other assets will be hosted in a single, public GitHub repository. The textbook content will link directly to this repository.

- **Repository Structure**:
  ```
  /
  ├── module_1_ros2/
  │   ├── src/
  │   └── launch/
  ├── module_2_simulation/
  │   ├── worlds/
  │   └── models/
  ├── module_3_isaac/
  │   └── ...
  ├── module_4_vla/
  │   └── capstone_project/
  └── README.md
  ```

**Rationale**: A central GitHub repository is the industry standard for distributing open-source software and assets. It provides version control, issue tracking, and a single source of truth for students. This approach encourages good software development practices.

**Alternatives Considered**:
- Bundling assets in a `.zip` file: Rejected as it's difficult to version, update, and manage.
- Using a separate repository for each module: Rejected as it would complicate setup and management for students who will be working through the entire textbook sequentially.
