#include <moveit/robot_state/conversions.h>
#include <moveit/planning_interface/planning_interface.h>
#include <moveit_msgs/MotionPlanRequest.h>
#include <moveit/planning_scene/planning_scene.h>

#include <ros/console.h>

#include <Eigen/Geometry>

#include <trajopt_interface/trajopt_planning_context.h>
#include <trajopt_interface/trajopt_interface.h>

namespace trajopt_interface
{
TrajOptPlanningContext::TrajOptPlanningContext(const std::string& context_name, const std::string& group_name,
                                               const moveit::core::RobotModelConstPtr& model)
  : planning_interface::PlanningContext(context_name, group_name), robot_model_(model)
{
  ROS_INFO(" ======================================= TrajOptPlanningContext is constructed");
  trajopt_interface_ = std::make_shared<TrajOptInterface>();
}

bool TrajOptPlanningContext::solve(planning_interface::MotionPlanDetailedResponse& res)
{
  moveit_msgs::MotionPlanDetailedResponse res_msg;
  bool trajopt_solved = trajopt_interface_->solve(planning_scene_, request_, res_msg);

  if (trajopt_solved)
  {
    res.trajectory.resize(1);
    res.trajectory[0] = std::make_shared<robot_trajectory::RobotTrajectory>(robot_model_, getGroupName());

    moveit::core::RobotState start_state(robot_model_);
    moveit::core::robotStateMsgToRobotState(res_msg.trajectory_start, start_state);
    res.trajectory[0]->setRobotTrajectoryMsg(start_state, res_msg.trajectory[0]);

    res.description.push_back("plan");
    // TODO: Add the initial trajectory to res (MotionPlanDetailedResponse)
    res.processing_time = res_msg.processing_time;
    res.error_code = res_msg.error_code;
    return true;
  }
  else
  {
    res.error_code = res_msg.error_code;
    return false;
  }
}

bool TrajOptPlanningContext::solve(planning_interface::MotionPlanResponse& res)
{
  planning_interface::MotionPlanDetailedResponse res_detailed;
  bool planning_success = solve(res_detailed);

  res.error_code = res_detailed.error_code;

  if (planning_success)
  {
    res.trajectory = res_detailed.trajectory[0];
    res.planning_time = res_detailed.processing_time[0];
  }

  return planning_success;
}

bool TrajOptPlanningContext::terminate()
{
  ROS_ERROR_STREAM_NAMED("trajopt_planning_context", "TrajOpt is not interruptible yet");
  return false;
}
void TrajOptPlanningContext::clear()
{
}

}  // namespace trajopt_interface
