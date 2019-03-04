Name:           ros-indigo-dbw-mkz-twist-controller
Version:        1.1.1
Release:        0%{?dist}
Summary:        ROS dbw_mkz_twist_controller package

Group:          Development/Libraries
License:        BSD
URL:            http://dataspeedinc.com
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-dbw-mkz-msgs
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-dbw-mkz-msgs
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs

%description
Twist (speed and angular rate) controller for brake/throttle/steering

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Mar 04 2019 Micho Radovnikovich <mradovnikovich@dataspeedinc.com> - 1.1.1-0
- Autogenerated by Bloom

* Tue Dec 04 2018 Micho Radovnikovich <mradovnikovich@dataspeedinc.com> - 1.1.0-0
- Autogenerated by Bloom

* Sat Oct 27 2018 Micho Radovnikovich <mradovnikovich@dataspeedinc.com> - 1.0.17-0
- Autogenerated by Bloom

* Wed Jun 13 2018 Micho Radovnikovich <mradovnikovich@dataspeedinc.com> - 1.0.13-0
- Autogenerated by Bloom

