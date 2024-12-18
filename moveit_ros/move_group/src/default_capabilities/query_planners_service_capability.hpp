/*********************************************************************
 * Software License Agreement (BSD License)
 *
 *  Copyright (c) 2012, Willow Garage, Inc.
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above
 *     copyright notice, this list of conditions and the following
 *     disclaimer in the documentation and/or other materials provided
 *     with the distribution.
 *   * Neither the name of Willow Garage nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 *  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 *  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 *  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 *  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 *  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 *  POSSIBILITY OF SUCH DAMAGE.
 *********************************************************************/

/* Author: Ioan Sucan, Robert Haschke */

#pragma once

#include <moveit/move_group/move_group_capability.hpp>
#include <moveit_msgs/srv/query_planner_interfaces.hpp>
#include <moveit_msgs/srv/get_planner_params.hpp>
#include <moveit_msgs/srv/set_planner_params.hpp>

namespace move_group
{
class MoveGroupQueryPlannersService : public MoveGroupCapability
{
public:
  MoveGroupQueryPlannersService();

  void initialize() override;

private:
  void queryInterface(const std::shared_ptr<moveit_msgs::srv::QueryPlannerInterfaces::Request>& /*req*/,
                      const std::shared_ptr<moveit_msgs::srv::QueryPlannerInterfaces::Response>& res);

  void getParams(const std::shared_ptr<moveit_msgs::srv::GetPlannerParams::Request>& req,
                 const std::shared_ptr<moveit_msgs::srv::GetPlannerParams::Response>& res);
  void setParams(const std::shared_ptr<moveit_msgs::srv::SetPlannerParams::Request>& req,
                 const std::shared_ptr<moveit_msgs::srv::SetPlannerParams::Response>& /*res*/);

  rclcpp::Service<moveit_msgs::srv::QueryPlannerInterfaces>::SharedPtr query_service_;
  rclcpp::Service<moveit_msgs::srv::GetPlannerParams>::SharedPtr get_service_;
  rclcpp::Service<moveit_msgs::srv::SetPlannerParams>::SharedPtr set_service_;
};
}  // namespace move_group
