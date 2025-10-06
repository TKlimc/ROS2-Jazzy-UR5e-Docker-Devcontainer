cmake_minimum_required(VERSION 3.8)
project(my_program_managment)

# Compiler-Warnungen aktivieren
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Abhängigkeiten finden
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(geometry_msgs REQUIRED)

# Generiere Service-Interfaces
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/GeneratePoseArray.srv"
  "srv/PlancheckerPose.srv"
  "srv/PlancheckedPoseArray.srv"
  "srv/ReachcheckerPoseArray.srv"
  "srv/TransformPoseArray.srv"
  "srv/CaptureAfterStop.srv"
  DEPENDENCIES geometry_msgs
)

# Exportiere Abhängigkeiten für andere Pakete
ament_export_dependencies(rosidl_default_runtime)

# Installiere Service-Definitionen
install(DIRECTORY srv
  DESTINATION share/${PROJECT_NAME}
)

# Installiere Launch-Dateien
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
