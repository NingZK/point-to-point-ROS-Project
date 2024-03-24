The ROS package description:

1)This ROS package that will automatically generate point-to-point cubic trajectories connecting pairs of randomly generated points.
2)After install the package and running a single launch file the user should see different random trajectories appearing on the rqt_plot GUI.

To run the package:

1)There are five folders named launch,msg,scripts,src and srv and one CMakeLists.txt and one README.txt and a package.xml in the folder.
2)Build the catkin workspace.
3)When the workspace is ready,enter the following command:
  $ cd catkin_ws
  $ catkin_make
  $ source devel/setup.bash
5)Launch the package by running:
  $ roslaunch point_to_point_gen.launch

