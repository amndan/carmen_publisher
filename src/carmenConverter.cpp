/*
 * carmenConverter.cpp
 *
 *  Created on: Jan 17, 2016
 *      Author: amndan
 */

using namespace std;

#include "ros/ros.h"
#include "geometry_msgs/PoseStamped.h"
#include <ctime>
#include <cmath>
#include <iostream>
#include <fstream>
#include "tf/transform_datatypes.h"
#include <iomanip>


void calPose(const geometry_msgs::PoseStampedConstPtr& msg);

ros::Subscriber subPose;
ros::NodeHandle* nh = NULL;
std::ofstream ofs("/home/amndan/test.log", ofstream::out);

int main(int argc, char** argv)
{
  ros::init(argc, argv, "carmenConverter");

  nh = new ros::NodeHandle();

  //ofs.clear();
  ofs << fixed << showpoint << setprecision(6);

  subPose = nh->subscribe("pose", 20, &calPose);

  ros::spin();

  ofs.close();
}

void calPose(const geometry_msgs::PoseStampedConstPtr& msg)
{
  // FLASER 0 x y theta x y theta timestamp hostname logger_timestamp

  double theta = tf::getYaw(msg->pose.orientation);
  double timestamp;
  ros::Time rosTimestamp = msg->header.stamp;

  timestamp = rosTimestamp.sec + rosTimestamp.nsec / 1e9;

  ofs << "FLASER 0 "
      << msg->pose.position.x << " "
      << msg->pose.position.y << " "
      << theta << " "
      << msg->pose.position.x << " "
      << msg->pose.position.y << " "
      << theta << " "
      << timestamp << " "
      << "hostname" << " "
      << timestamp << "\n";
}
