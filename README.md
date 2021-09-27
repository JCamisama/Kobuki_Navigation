<h1>Kobuki Navigation Repository</h1>

<p>
This repository contains the progress that's been made in the ROS Navigation part of FlexManSys. It consists of a ROS Node called FlexmansysCruiser that can receive and navigate to coordinates indicated in the topic
"order" (The topic name can be specified in <i>kobuki_navigation_ws/src/kobuki_basic_navigation_system/scripts/cruiserconfig.py</i>) as well as all the python classes that conform the navigation system bundled in the navigation_system python package .

A publisher CLI has been included in the kobuki_basic_navigation_system ROS package (called FlexmansysTestPublisher.py) for experimental purposes.
</p>




<h3>Required Software</h3>
<ol>
  <li> Ubuntu 16.04: https://releases.ubuntu.com/16.04/</li>
  <li> ROS Kinetic: http://wiki.ros.org/kinetic/Installation/Ubuntu</li>
  <li> Python 2.7 (Default version installed in Ubuntu 16.04)</li>
  <li> Kobuki ROS: http://wiki.ros.org/kobuki/Tutorials/Installation/kinetic</li>
</ol>

<h3>Recommended Software</h3>
<ol>
  <li> Kobuki Gazebo: http://wiki.ros.org/kobuki/Tutorials/Gazebo%20Simulation</li>
  <li> Terminator: sudo apt-get install terminator</li>
</ol>

<h3>Give it a try</h3>
<h5>***Common step in every terminal: <i>source devel/setup.bash</i> </h5>

<ol>
  <li> Navigate to kobuki_navigation_ws: cd kobuki_navigation_ws</li>
  <li> Execute catkin_make</li>
  <li> Open 4 terminals (at least) and apply ***</li>
  <li> First terminal:
      <ul>
        <li>Kobuki turtlebot: roslaunch kobuki_node minimal.launch --screen </li>
        <li>Gazebo simulation: roslaunch kobuki_gazebo kobuki_empty_world.launch --screen </li>
      </ul>
  </li>
  <li> Second terminal: rosrun kobuki_basic_navigation_system FlexmansysTestPublisher.py</li>
  <li> Third terminal: rosrun kobuki_basic_navigation_system FlexmansysCruiser.py</li>
  <li> Fourth terminal: rostopic echo /order</li>
  <li> Write comma separated orders in the second terminal: A0,C3,F4,E2...</li>
  <li> Enjoy the ride.</li>

</ol>
