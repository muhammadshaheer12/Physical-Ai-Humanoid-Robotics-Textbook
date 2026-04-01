# ADR-1: Standardized Development Environment for Robotics Textbook

- **Status**: Proposed
- **Date**: 2025-12-31

## Context

The "Physical AI & Humanoid Robotics Textbook" requires a consistent, reproducible, and stable environment for all students to successfully complete the hands-on projects and tutorials. The choice of operating system, core software tools, and hardware has a significant impact on the student experience, the complexity of the course material, and long-term maintainability. The decision must balance access to modern features with the need for stability and a low-friction setup process.

## Decision

We will standardize the entire textbook on a specific, unified development environment:

- **Operating System**: Ubuntu 22.04 LTS (Jammy Jellyfish)
- **Core Robotics/Simulation Toolchain**:
    - ROS 2: Humble Hawksbill (LTS)
    - Gazebo: Fortress
    - Unity: 2022.3 LTS
    - NVIDIA Isaac Sim: 2023.1.1
- **Hardware**: A defined minimum and recommended specification, with an NVIDIA GPU being a mandatory requirement for Module 3.
- **Content Delivery Platform**: Docusaurus for the static textbook site.

All code examples, installation scripts, and tutorials will be exclusively tested against and written for this exact environment.

## Consequences

- **Positive**:
    - **High Reproducibility**: Students will have a clear, single path to a working environment, dramatically reducing "it works on my machine" issues and support overhead.
    - **Stability**: Using LTS versions of Ubuntu and ROS 2 provides a stable foundation with long-term support.
    - **Simplified Content**: The tutorials and instructions can be written for a single target, making them clearer and more concise.
    - **Focused Learning**: Students can focus on robotics concepts instead of debugging environment incompatibilities.

- **Negative**:
    - **Reduced Flexibility**: Students with different operating systems (Windows, macOS) or different existing software versions will face a higher barrier to entry (requiring dual-boot or a dedicated machine).
    - **Hardware Constraint**: The mandatory NVIDIA GPU for the Isaac module excludes users with AMD or integrated graphics from completing the entire textbook.
    - **Version Lock-in**: The textbook will not immediately benefit from new features in subsequent releases of the core tools until it is explicitly updated.

## Alternatives

- **Support Multiple Environments (e.g., Ubuntu 20.04/22.04, ROS 2 Foxy/Humble)**:
    - **Pros**: Greater flexibility for users with existing setups.
    - **Cons**: Rejected due to the exponential increase in complexity for content creation, testing, and student support. It would make the project infeasible for a small team.
- **Use Only Containerized Environments (Docker)**:
    - **Pros**: Excellent reproducibility and isolation.
    - **Cons**: Rejected due to the significant performance overhead for GPU-intensive simulation, the complexity of managing GUI applications within containers, and the added conceptual load for students who may not be familiar with Docker.
- **Lower Hardware Requirements**:
    - **Pros**: Increased accessibility for users with less powerful machines.
    - **Cons**: Rejected because it would provide a poor, laggy, and frustrating user experience for the simulation-heavy modules, ultimately hindering the learning objectives.

## References

- `specs/2-humanoid-robotics-textbook/plan.md`
- `specs/2-humanoid-robotics-textbook/research.md`
