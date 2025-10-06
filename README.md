# ROS2-Jazzy-UR5e-Docker-Devcontainer

This repository provides a **simple and beginner-friendly setup** for using the **Universal Robots UR5e** with **ROS 2**.  
It is based on a ROS 2 Docker image and includes a preconfigured **VS Code Devcontainer** to make development quick and consistent — ideal for beginners who want to get started without complex configuration.
---

## License

This project is licensed under the **MIT License**.

### Third-Party Components

This project uses and integrates several open-source components:

- **Universal Robots ROS 2 Driver**  
  Source: [UniversalRobots/Universal_Robots_ROS2_Driver](https://github.com/UniversalRobots/Universal_Robots_ROS2_Driver)  
  Licensed under the **BSD 3-Clause License**, © Universal Robots A/S  

- **Universal Robots ROS 2 Description**  
  Source: [UniversalRobots/Universal_Robots_ROS2_Description](https://github.com/UniversalRobots/Universal_Robots_ROS2_Description)  
  Licensed under the **BSD 3-Clause License**, © Universal Robots A/S  
  *Note:* URDF and mesh files are subject to additional usage terms as described in the repository.

This project is an **independent development** and is **not affiliated with or endorsed by Universal Robots A/S**.  
All original work in this repository is released under the MIT License.  
All third-party components retain their original licenses.

---

## System Requirements

The setup should also work on **Windows** with minimal adjustments.  
You will need:
- **Docker**
- **WSL2**

**Recommendation:** Use Windows only for coding and testing, not for working with a real robot.  
(Windows is not real-time capable — see [Universal Robots Documentation](https://docs.universal-robots.com/Universal_Robots_ROS2_Documentation/doc/ur_client_library/doc/real_time.html))

This project was tested on **Ubuntu 24.04.2 LTS** with **VS Code**.

---

## Getting Started

### 1. Enable X Server for graphical ROS 2 applications

Before starting VS Code, open a terminal and run:

```bash
xhost +local:docker
```

This allows graphical user interfaces (like RViz) from within the Docker container to be displayed on your host system.

### 2. Start the URSim simulation (optional)
If you don’t have a real robot and want to work with a simulated one, run:

```bash
docker run --rm -it -p 5900:5900 -p 6080:6080 \
-v ${HOME}/.ursim/urcaps:/urcaps \
-v ${HOME}/.ursim/programs:/ursim/programs \
--net ursim_net --ip 192.168.56.101 \
universalrobots/ursim_e-series
```
This will start the URSim software for a virtual robot simulation. Click the Link in the Terminal, poweron the Robor, start the Robot. Click the Programtab in the top left corner, select URCaps and External Control then click play in the botton right corner.
External Control enables you to move the Robot with ROS2 but also allows you to move the real or in this case the simulated robot.
https://docs.universal-robots.com/Universal_Robots_ROS2_Documentation/doc/ur_robot_driver/ur_robot_driver/doc/operation_modes.html

### 3. Open the project in VS Code

Open the project folder in VS Code

Open the Command Palette (Ctrl+Shift+P)

Select “Reopen in Container”

The Devcontainer will now build the environment.
This process may take a few minutes the first time.

### 4. Configure the robot IP address

Edit the following file:
src/my_robot_cell/my_robot_cell_control/start_robot.launch.py

Change the default value to your robot’s IP address:
default_value="192.168.137.127"  # replace with your real robot IP

If you are using the simulated robot, use:
default_value="192.168.56.101"

### 5. Build the project

Open a new terminal inside the Devcontainer and run:

```bash
colcon build --symlink-install
source install/setup.bash
```

This will build the project and set up your workspace.

### 6. Start the project

```bash
ros2 launch my_program_managment start_all_moveit.launch.py
```

If your simulation container from step 2 is running,
you can now start the robot program inside the simulation container (bottom right corner of the URSim interface).
After starting it, you should receive a confirmation message in VS Code indicating that everything is working.

You can now move the simulated robot within the URSim interface and observe its movement in ROS 2 RViz in real time.
Your base setup is now complete, and you can start writing your own ROS 2 packages to control the robot using MoveIt.