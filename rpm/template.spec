%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-moveit-kinematics
Version:        2.12.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS moveit_kinematics package

License:        BSD-3-Clause
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       python%{python3_pkgversion}-lxml
Requires:       ros-jazzy-class-loader
Requires:       ros-jazzy-generate-parameter-library
Requires:       ros-jazzy-moveit-common
Requires:       ros-jazzy-moveit-core
Requires:       ros-jazzy-moveit-msgs
Requires:       ros-jazzy-moveit-ros-planning
Requires:       ros-jazzy-orocos-kdl-vendor
Requires:       ros-jazzy-pluginlib
Requires:       ros-jazzy-rsl
Requires:       ros-jazzy-tf2
Requires:       ros-jazzy-tf2-kdl
Requires:       ros-jazzy-urdfdom
Requires:       ros-jazzy-ros-workspace
BuildRequires:  eigen3-devel
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-class-loader
BuildRequires:  ros-jazzy-generate-parameter-library
BuildRequires:  ros-jazzy-moveit-common
BuildRequires:  ros-jazzy-moveit-core
BuildRequires:  ros-jazzy-moveit-msgs
BuildRequires:  ros-jazzy-moveit-ros-planning
BuildRequires:  ros-jazzy-orocos-kdl-vendor
BuildRequires:  ros-jazzy-pluginlib
BuildRequires:  ros-jazzy-rsl
BuildRequires:  ros-jazzy-tf2
BuildRequires:  ros-jazzy-tf2-kdl
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-cmake-gtest
BuildRequires:  ros-jazzy-launch-param-builder
BuildRequires:  ros-jazzy-moveit-configs-utils
BuildRequires:  ros-jazzy-moveit-resources-fanuc-description
BuildRequires:  ros-jazzy-moveit-resources-fanuc-moveit-config
BuildRequires:  ros-jazzy-moveit-resources-panda-description
BuildRequires:  ros-jazzy-moveit-resources-panda-moveit-config
BuildRequires:  ros-jazzy-ros-testing
%endif

%description
Package for all inverse kinematics solvers in MoveIt

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
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
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Tue Apr 15 2025 Henning Kayser <henningkayser@picknik.ai> - 2.12.3-1
- Autogenerated by Bloom

* Sun Feb 16 2025 Henning Kayser <henningkayser@picknik.ai> - 2.12.2-1
- Autogenerated by Bloom

* Wed Dec 18 2024 Henning Kayser <henningkayser@picknik.ai> - 2.12.1-1
- Autogenerated by Bloom

* Fri Nov 29 2024 Henning Kayser <henningkayser@picknik.ai> - 2.12.0-1
- Autogenerated by Bloom

* Fri Jun 14 2024 Henning Kayser <henningkayser@picknik.ai> - 2.10.0-1
- Autogenerated by Bloom

* Mon Apr 22 2024 Henning Kayser <henningkayser@picknik.ai> - 2.9.0-1
- Autogenerated by Bloom

