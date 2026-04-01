# Quickstart Guide: Physical AI & Humanoid Robotics Textbook

This guide provides step-by-step instructions to set up your development environment for the "Physical AI & Humanoid Robotics Textbook". Following these instructions precisely will ensure a consistent and reproducible experience throughout the course.

## 1. Hardware Requirements

Ensure your machine meets at least the **minimum specifications**. For optimal performance, especially with NVIDIA Isaac Sim, the **recommended specifications** are highly encouraged.

### Minimum Specification:
- **CPU**: 6-core Intel Core i7 or AMD Ryzen 5
- **RAM**: 16 GB DDR4
- **GPU**: NVIDIA GeForce RTX 2060 (6 GB VRAM) with CUDA support
- **Storage**: 100 GB SSD

### Recommended Specification:
- **CPU**: 8-core Intel Core i9 or AMD Ryzen 7
- **RAM**: 32 GB DDR4
- **GPU**: NVIDIA GeForce RTX 3070 or higher (8+ GB VRAM)
- **Storage**: 200 GB NVMe SSD

**Important**: An NVIDIA GPU with CUDA support is **mandatory** for Module 3 (NVIDIA Isaac).

## 2. Operating System Installation (Ubuntu 22.04 LTS)

The textbook assumes you are running **Ubuntu 22.04 LTS (Jammy Jellyfish)**. If you are using Windows, it is highly recommended to set up a dual-boot system or use a virtual machine (though VM performance may be suboptimal for GPU-intensive tasks).

1.  **Download Ubuntu 22.04 LTS**: Get the ISO from the [official Ubuntu website](https://ubuntu.com/download/desktop).
2.  **Create Bootable USB**: Use a tool like [Rufus](https://rufus.ie/en/) (Windows) or [Etcher](https://www.balena.io/etcher/) (cross-platform) to create a bootable USB drive.
3.  **Install Ubuntu**: Follow the on-screen instructions to install Ubuntu 22.04 LTS on your system. Ensure you allocate sufficient disk space.

## 3. Core Software Installation

All installations should be performed on your Ubuntu 22.04 LTS system.

### 3.1 Python 3.10

Ubuntu 22.04 LTS comes with Python 3.10 pre-installed. Verify its version:
```bash
python3 --version
# Expected output: Python 3.10.x
```
Ensure `pip` is installed and up-to-date:
```bash
sudo apt update
sudo apt install python3-pip
pip install --upgrade pip
```

### 3.2 ROS 2 Humble Hawksbill

Follow the official ROS 2 Humble installation guide for Ubuntu (Debian packages):
1.  **Set up locales**:
    ```bash
    sudo locale-gen en_US en_US.UTF-8
    sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
    export LANG=en_US.UTF-8
    ```
2.  **Set up sources**:
    ```bash
    sudo apt install software-properties-common
    sudo add-apt-repository universe
    sudo apt update && sudo apt install curl -y
    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
    ```
3.  **Install ROS 2 packages**:
    ```bash
    sudo apt update
    sudo apt upgrade
    sudo apt install ros-humble-desktop
    ```
4.  **Environment setup**: Add to your `~/.bashrc`:
    ```bash
    source /opt/ros/humble/setup.bash
    source /usr/share/colcon_cd/function/colcon_cd.sh
    export _colcon_cd_root=/opt/ros/humble/
    source /usr/share/ament_index/resource_index/package_run_dependencies/ros_actions_examples
    ```
    Then `source ~/.bashrc`.

### 3.3 Gazebo Fortress

Install Gazebo Fortress using the official instructions:
1.  **Set up sources**:
    ```bash
    sudo apt update
    sudo apt install lsb-release
    sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
    wget https://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
    sudo apt update
    ```
2.  **Install Gazebo Fortress**:
    ```bash
    sudo apt install gazebo-fortress
    sudo apt install libignition-common-ign6-dev # For development headers
    ```
3.  Verify installation: `ign gazebo`

### 3.4 Unity 2022.3 LTS (for Environment Building)

1.  **Download Unity Hub**: Download the `.AppImage` from [Unity Hub website](https://unity.com/download) for Linux.
2.  **Install Unity Editor**: Use Unity Hub to install **Unity Editor version 2022.3 LTS**. Select the "Linux Build Support (Mono)" module.

### 3.5 NVIDIA Drivers & CUDA Toolkit

This is critical for NVIDIA Isaac Sim and Isaac ROS.
1.  **Install NVIDIA Drivers**: Ensure you have the latest proprietary NVIDIA drivers installed. Go to "Software & Updates" -> "Additional Drivers" and select the latest tested proprietary driver.
2.  **Install CUDA Toolkit**: Follow the [official NVIDIA CUDA Toolkit documentation](https://developer.nvidia.com/cuda-downloads) for Ubuntu 22.04.

### 3.6 NVIDIA Isaac Sim 2023.1.1

Isaac Sim runs on NVIDIA Omniverse Launcher.
1.  **Download Omniverse Launcher**: Download and install from [NVIDIA Omniverse website](https://www.nvidia.com/omniverse/download/launcher/).
2.  **Install Isaac Sim**: Within the Omniverse Launcher, navigate to the "Exchange" tab, search for "Isaac Sim", and install **version 2023.1.1** (or the latest stable compatible with your CUDA version).

## 4. Code and Asset Repository

The textbook's code examples and simulation assets are hosted on GitHub.
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/YourOrganization/Physical-AI-Humanoid-Robotics-Textbook-Assets.git
    cd Physical-AI-Humanoid-Robotics-Textbook-Assets
    ```
    *(Note: Replace `YourOrganization/Physical-AI-Humanoid-Robotics-Textbook-Assets.git` with the actual repository URL once it's created.)*
2.  **Install Python dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

You are now ready to begin your journey through the textbook!
