Name:			invalid-url
Version:        0
Release:        0
Summary:		invalid-url warning
License:        GPL-2.0-only
Group:          Undefined
Patch0:         Patch.patch
Patch1:         Patch1.patch

%description
The specfile does not contain invalid-url.

%prep

%build

%install
%patch -P

%files
%{_libdir}/foo

%changelog
