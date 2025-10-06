# Use the ROS Jazzy desktop full base image
FROM osrf/ros:jazzy-desktop-full


# Set build-time arguments
ARG USERNAME=ubuntu
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create non-root user
RUN if ! id -u $USER_UID >/dev/null 2>&1; then \
        groupadd --gid $USER_GID $USERNAME && \
        useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME; \
    fi

# Set timezone to Europe/Berlin
RUN echo "Europe/Berlin" > /etc/timezone && \
    ln -snf /usr/share/zoneinfo/Europe/Berlin /etc/localtime && \
    apt-get update && \
    apt-get install -q -y --no-install-recommends tzdata && \
    dpkg-reconfigure -f noninteractive tzdata && \
    rm -rf /var/lib/apt/lists/*

# Install ROS packages, system tools, and other dependencies
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y sudo \
    ffmpeg \
    git \
    python3-pip \
    linux-lowlatency \
    ros-${ROS_DISTRO}-ur \
    ros-${ROS_DISTRO}-moveit \
    ros-${ROS_DISTRO}-controller-manager \
    ros-${ROS_DISTRO}-ros2-control \
    ros-${ROS_DISTRO}-ros2-controllers \
    ros-${ROS_DISTRO}-ros2controlcli \
    ros-${ROS_DISTRO}-sensor-msgs \
    ros-${ROS_DISTRO}-librealsense2* \
    ros-${ROS_DISTRO}-realsense2-* \
    ros-${ROS_DISTRO}-image-transport \
    ros-${ROS_DISTRO}-tf-transformations \
    rt-tests \
    iputils-ping \
    v4l-utils \
    nano \
    tree \
    && rm -rf /var/lib/apt/lists/*

# Add sudo support for the non-root user
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y sudo \
    && echo "$USERNAME ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Add the user to the video group for webcam access
RUN usermod --append --groups video $USERNAME

# Add ROS environment setup to .bashrc
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> /home/$USERNAME/.bashrc && \
    echo "export RCUTILS_COLORIZED_OUTPUT=1" >> /home/$USERNAME/.bashrc

# Create and set permissions for workspace directories
RUN mkdir -p /ros_ws/src && \
    chown -R $USER_UID:$USER_GID /ros_ws
# Install dependencies with rosdep
USER $USERNAME

ENV ROS_DOMAIN_ID=40
# Set entrypoint
ENTRYPOINT ["/bin/bash"]
