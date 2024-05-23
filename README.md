# cs732-project-2

Clone repo into workspace
```bash
cd catkin_ws/src
git clone https:github.com/apaik458/cs732-project-2.git
git clone -b melodic-devel https://github.com/paulbovbel/frontier_exploration.git
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

Launch gmapping node
```bash
roslaunch turtlebot_navigation gmapping_demo.launch
```

Launch frontier exploration node
```bash
roslaunch exploration_server exploration.launch
```

Launch rviz
```bash
roslaunch turtlebot_rviz_launchers view_navigation.launch
```
