Name:           ros-indigo-dbw-mkz-can
Version:        1.1.0
Release:        0%{?dist}
Summary:        ROS dbw_mkz_can package

Group:          Development/Libraries
License:        BSD
URL:            http://dataspeedinc.com
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-can-msgs
Requires:       ros-indigo-dataspeed-can-usb
Requires:       ros-indigo-dataspeed-ulc-can
Requires:       ros-indigo-dbw-mkz-description
Requires:       ros-indigo-dbw-mkz-msgs
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roslaunch
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-can-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-dataspeed-can-msg-filters
BuildRequires:  ros-indigo-dbw-mkz-msgs
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslaunch
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs

%description
Drive-by-wire interface to the Dataspeed Inc. Lincoln MKZ DBW kit

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
* Tue Dec 04 2018 Kevin Hallenbeck <khallenbeck@dataspeedinc.com> - 1.1.0-0
- Autogenerated by Bloom

* Sat Oct 27 2018 Kevin Hallenbeck <khallenbeck@dataspeedinc.com> - 1.0.17-0
- Autogenerated by Bloom

* Wed Jun 13 2018 Kevin Hallenbeck <khallenbeck@dataspeedinc.com> - 1.0.13-0
- Autogenerated by Bloom

