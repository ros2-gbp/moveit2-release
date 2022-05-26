%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-moveit-ros-perception
Version:        2.5.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS moveit_ros_perception package

License:        BSD
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       freeglut-devel
Requires:       glew-devel
Requires:       libomp-devel
Requires:       mesa-libGL-devel
Requires:       mesa-libGLU-devel
Requires:       ros-humble-cv-bridge
Requires:       ros-humble-image-transport
Requires:       ros-humble-message-filters
Requires:       ros-humble-moveit-common
Requires:       ros-humble-moveit-core
Requires:       ros-humble-moveit-msgs
Requires:       ros-humble-moveit-ros-occupancy-map-monitor
Requires:       ros-humble-moveit-ros-planning
Requires:       ros-humble-object-recognition-msgs
Requires:       ros-humble-pluginlib >= 1.11.2
Requires:       ros-humble-rclcpp
Requires:       ros-humble-sensor-msgs
Requires:       ros-humble-tf2
Requires:       ros-humble-tf2-eigen
Requires:       ros-humble-tf2-geometry-msgs
Requires:       ros-humble-tf2-ros
Requires:       ros-humble-urdf
Requires:       ros-humble-ros-workspace
BuildRequires:  eigen3-devel
BuildRequires:  freeglut-devel
BuildRequires:  glew-devel
BuildRequires:  libomp-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-cv-bridge
BuildRequires:  ros-humble-image-transport
BuildRequires:  ros-humble-message-filters
BuildRequires:  ros-humble-moveit-common
BuildRequires:  ros-humble-moveit-core
BuildRequires:  ros-humble-moveit-msgs
BuildRequires:  ros-humble-moveit-ros-occupancy-map-monitor
BuildRequires:  ros-humble-moveit-ros-planning
BuildRequires:  ros-humble-object-recognition-msgs
BuildRequires:  ros-humble-pluginlib >= 1.11.2
BuildRequires:  ros-humble-rclcpp
BuildRequires:  ros-humble-sensor-msgs
BuildRequires:  ros-humble-tf2
BuildRequires:  ros-humble-tf2-eigen
BuildRequires:  ros-humble-tf2-geometry-msgs
BuildRequires:  ros-humble-tf2-ros
BuildRequires:  ros-humble-urdf
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-lint-auto
BuildRequires:  ros-humble-ament-lint-common
%endif

%description
Components of MoveIt connecting to perception

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Thu May 26 2022 Henning Kayser <henningkayser@picknik.ai> - 2.5.0-1
- Autogenerated by Bloom

