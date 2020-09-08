%global commit b5cef5985436726b258dc76edc6a83b8a486f977
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}
%global project Viper4Linux
%global homedir %(echo $HOME)
%undefine _disable_source_fetch

Name:           viper4linux
Version:        %{shortcommit}
Release:        2%{?dist}
Summary:        An Adaptive Digital Sound Processor

License:        GPLv3
URL:            https://github.com/Audio4Linux/Viper4Linux
Source0:        https://github.com/Audio4Linux/Viper4Linux/archive/%{commit}/%{project}-%{shortcommit}.tar.gz

Requires:       viperfx-core-binary gstreamer-plugin-viperfx

%description
Viper4Linux - An Adaptive Digital Sound Processor
Making Loonix sound good
This is the second interation of Viper4Linux and aims to focus on features and end-user ease

%prep
%autosetup -n %{project}-%{commit}

%build

%install
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{homedir}/.config/viper4linux
%{__install} -m 0755 viper %{buildroot}%{_bindir}/viper
%{__install} -m 0644 viper4linux/* %{buildroot}%{homedir}/.config/viper4linux

%clean
rm -rf %{buildroot}

%files
%{_bindir}/viper
%config(noreplace) %{homedir}/.config/viper4linux/*

%changelog
* Sun Sep  6 2020 jeffshee <jeffshee8969@gmail.com>
- 
