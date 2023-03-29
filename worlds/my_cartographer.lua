include "map_builder.lua"
include "trajectory_builder.lua"

options = {
    map_builder = MAP_BUILDER,
    trajectory_builder = TRAJECTORY_BUILDER,
    map_frame = "map",
    tracking_frame = "odom",
    published_frame = "chassis",
    odom_frame = "odom",
    provide_odom_frame = true,
    use_odometry = false,
    use_nav_sat = true,
    nav_sat_fix_topic: "qps/fix"
    nav_sat_predefined_enu_frame_id: "map"
    nav_sat_use_predefined_enu_frame = true,
    nav_sat_predefined
