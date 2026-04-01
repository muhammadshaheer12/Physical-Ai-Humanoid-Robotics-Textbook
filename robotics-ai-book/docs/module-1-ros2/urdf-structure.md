# Understanding URDF: Unified Robot Description Format

The Unified Robot Description Format (URDF) is an XML format for describing all elements of a robot. It's used to represent the robot's kinematic and dynamic properties, visualize its appearance, and define its collision geometry.

## Structure of a URDF File

A URDF file is composed of `<link>` and `<joint>` elements.

### Links

A `<link>` element defines a rigid body of the robot, such as a wheel, torso, or arm segment. Each link can have:

-   **`<visual>`**: Describes the link's appearance (geometry, material).
-   **`<collision>`**: Defines the link's collision properties (geometry).
-   **`<inertial>`**: Specifies the link's physical properties (mass, inertia).

### Joints

A `<joint>` element defines the connection between two links, specifying their relative motion. Key attributes include:

-   `name`: A unique identifier for the joint.
-   `type`: The type of joint (e.g., `revolute`, `continuous`, `prismatic`, `fixed`).
-   `<parent>`: The name of the parent link.
-   `<child>`: The name of the child link.
-   `<origin>`: The XYZ coordinates and RPY (roll, pitch, yaw) orientation of the child frame with respect to the parent frame.
-   `<axis>`: The axis of rotation for revolute and continuous joints, or the axis of translation for prismatic joints.
-   `<limit>`: Specifies the joint's physical limits (e.g., lower/upper bounds, velocity, effort).

## Example: Simple Two-Link Robot

Let's look at the `robot.urdf` example we created:

```xml
<?xml version="1.0"?>
<robot name="simple_humanoid">
  <link name="base_link">
    <visual>
      <geometry>
        <box size="0.1 0.1 0.2"/>
      </geometry>
      <material name="blue">
        <color rgba="0 0 0.8 1"/>
      </material>
    </visual>
    <collision>
      <geometry>
        <box size="0.1 0.1 0.2"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="1.0"/>
      <inertia ixx="0.01" ixy="0.0" ixz="0.0" iyy="0.01" iyz="0.0" izz="0.01"/>
    </inertial>
  </link>

  <joint name="joint1" type="revolute">
    <parent link="base_link"/>
    <child link="link1"/>
    <origin xyz="0 0 0.15"/>
    <axis xyz="0 0 1"/>
    <limit lower="-1.57" upper="1.57" effort="100" velocity="10"/>
  </joint>

  <link name="link1">
    <visual>
      <geometry>
        <cylinder length="0.2" radius="0.02"/>
      </geometry>
      <material name="green">
        <color rgba="0 0.8 0 1"/>
      </material>
    </visual>
    <collision>
      <geometry>
        <cylinder length="0.2" radius="0.02"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="0.1"/>
      <inertia ixx="0.001" ixy="0.0" ixz="0.0" iyy="0.001" iyz="0.0" izz="0.001"/>
    </inertial>
  </link>
</robot>
```

This URDF defines a robot named "simple_humanoid" with two links (`base_link` and `link1`) connected by one revolute joint (`joint1`). The `base_link` is a blue box, and `link1` is a green cylinder.
