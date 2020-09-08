%global commit 5edde17e3787041d8a83126f3405e96f58622044
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}
%global project Viper4Linux-GUI
%undefine _disable_source_fetch

Name:           viper4linux-gui
Version:        %{shortcommit}
Release:        2%{?dist}
Summary:        Official UI for Viper4Linux

License:        GPLv3
URL:            https://github.com/Audio4Linux/Viper4Linux-GUI
Source0:        https://github.com/Audio4Linux/Viper4Linux-GUI/archive/%{commit}/%{project}-%{shortcommit}.tar.gz

BuildRequires:  gstreamer1-plugins-base-devel gstreamer1-devel gstreamer1-plugins-bad-free-devel qt5-qtbase-devel qt5-qtmultimedia-devel qt5-qtsvg-devel
Requires:       gstreamer1 gstreamer1-plugins-bad-free qt5 viperfx-core-binary gstreamer-plugin-viperfx viper4linux

%description
Official UI for Viper4Linux https://github.com/Audio4Linux/Viper4Linux
Telegram: @ThePBone
Supports both Viper4Linux2 and legacy Viper4Linux

%prep
%autosetup -n %{project}-%{commit}

%build
%_qt5_qmake
%make_build

%install
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_datarootdir}/pixmaps
%{__mkdir_p} %{buildroot}%{_datarootdir}/applications
%{__install} -m 0755 V4L_Frontend %{buildroot}%{_bindir}/viper-gui
%{__install} -m 0644 viper.png %{buildroot}%{_datarootdir}/pixmaps/viper-gui.png
%{__cat} <<EOT > %{buildroot}%{_datarootdir}/applications/viper-gui.desktop
[Desktop Entry]
Name=Viper4Linux
GenericName=Equalizer
Comment=User Interface for Viper4Linux
Keywords=equalizer
Categories=AudioVideo;Audio;
Exec=viper-gui
Icon=viper-gui
StartupNotify=false
Terminal=false
Type=Application
EOT

%clean
rm -rf %{buildroot}

%files
%{_bindir}/viper-gui
%{_datarootdir}/pixmaps/viper-gui.png
%{_datarootdir}/applications/viper-gui.desktop

%changelog
* Sun Sep  6 2020 jeffshee <jeffshee8969@gmail.com>
- 
