%global commit f6b4d8b1f2dccbe162f2257fc950de13f1582950
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}
%global project gst-plugin-viperfx
%undefine _disable_source_fetch

Name:           gstreamer-plugin-viperfx
Version:        %{shortcommit}
Release:        1%{?dist}
Summary:        ViPER FX core wrapper plug-in for GStreamer1

License:        Non-GPL
URL:            https://github.com/Audio4Linux/gst-plugin-viperfx
Source0:        https://github.com/Audio4Linux/gst-plugin-viperfx/archive/%{commit}/%{project}-%{shortcommit}.tar.gz

BuildRequires:  cmake autoconf automake libtool gstreamer1-plugins-base-devel gcc-c++
Requires:       gstreamer1 

%description
ViPER FX core wrapper plug-in for GStreamer1
In order to use this plug-in, you need the ViPER FX core
Please check https://github.com/vipersaudio/viperfx_core_binary for more information
This version is tailored for use with the new Viper4Linux
Dynamic system was added by ThePBone D-Bus interface also by ThePBone

%prep
%autosetup -n %{project}-%{commit}

%build
# %cmake .
# %make_build
%cmake -B build -S .
%make_build -C build

%install
%{__mkdir_p} %{buildroot}%{_libdir}/gstreamer-1.0
%{__install} -m 0755 build/libgstviperfx.so %{buildroot}%{_libdir}/gstreamer-1.0/libgstviperfx.so

%clean
rm -rf %{buildroot}

%files
%{_libdir}/gstreamer-1.0/libgstviperfx.so

%changelog
* Sun Sep  6 2020 jeffshee <jeffshee8969@gmail.com>
- 
