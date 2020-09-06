%global commit 6f7d0da725affe854f083baf5d90c70e172e4488
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}
%global project viperfx_core_binary
%undefine _disable_source_fetch

Name:           viperfx-core-binary
Version:        %{shortcommit}
Release:        1%{?dist}
Summary:        The ViPER FX core

License:        No License
URL:            https://github.com/vipersaudio/viperfx_core_binary
Source0:        https://github.com/vipersaudio/viperfx_core_binary/archive/%{commit}/%{project}-%{shortcommit}.tar.gz

%description
The ViPER FX core

%prep
%autosetup -n %{project}-%{commit}

%build

%install
%{__mkdir_p} %{buildroot}%{_libdir}
%{__install} -m 0644 libviperfx_x64_linux.so %{buildroot}%{_libdir}/libviperfx.so

%clean
rm -rf %{buildroot}

%files
%{_libdir}/libviperfx.so

%changelog
* Sun Sep  6 2020 jeffshee <jeffshee8969@gmail.com>
- 
