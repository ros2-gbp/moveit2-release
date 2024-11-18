/*********************************************************************
 * Software License Agreement (BSD License)
 *
 *  Copyright (c) 2016, Michael 'v4hn' Goerner
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

/* Author: Michael 'v4hn' Goerner */

#pragma once

#include <moveit/move_group/move_group_capability.h>
#include <moveit_msgs/srv/apply_planning_scene.hpp>

namespace move_group
{
/**
 * Provides the ability to update the shared planning scene
 * with a remote blocking call using a ROS-Service
 */
class ApplyPlanningSceneService : public MoveGroupCapability
{
public:
  ApplyPlanningSceneService();

  void initialize() override;

private:
  bool applyScene(const std::shared_ptr<rmw_request_id_t>& request_header,
                  const std::shared_ptr<moveit_msgs::srv::ApplyPlanningScene::Request>& req,
                  const std::shared_ptr<moveit_msgs::srv::ApplyPlanningScene::Response>& res);

  rclcpp::Service<moveit_msgs::srv::ApplyPlanningScene>::SharedPtr service_;
};
}  // namespace move_group
