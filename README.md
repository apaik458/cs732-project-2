# cs732-project-2

Clone repo into workspace
```bash
cd catkin_ws/src
git clone https:github.com/apaik458/cs732-project-2.git
```

Make and source project files
```bash
cd catkin_ws
catkin_make
source devel/setup.bash
```

Launch Gazebo world
```bash
roslaunch turtlebot_worlds world_1.launch
```

Run object detection and visual servoing nodes
```bash
rosrun python_nodes vision.py
rosrun python_nodes movement.py
```
