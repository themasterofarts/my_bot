include "map_builder.lua"
include "trajectory_builder.lua"
options = {
    tracking_frame = "imu_link",
    published_frame = "map",
    odom_frame = "odom",
    provide_odom_frame = true,
    use_odometry = true,
    use_nav_sat = true,
    nav_sat_use_predefined_enu_frame = true,
    nav_sat_predefined_enu_frame_lat_deg = LATITUDE,
    nav_sat_predefined_enu_frame_lon_deg = LONGITUDE,
    nav_sat_predefined_enu_frame_alt_m = ALTITUDE,
    use_landmarks = false,
  }
