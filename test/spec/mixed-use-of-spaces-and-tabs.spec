Name:			mixed-use-of-spaces-and-tabs
Version:        0
Release:        0
Summary:		mixed-use-of-spaces-and-tabs warning
License:        GPL-2.0-only
Group:          Undefined
URL:            http://rpmlint.zarb.org/#%{name}
Source0:        Source0.tar.gz
Patch0:         patch0.patch
Requires:       php

%description
The specfile mixes use of spaces and tabs for indentation, which is a
cosmetic annoyance.

%prep
  %autosetup

%build

%install
%ifarch
patch0 -P 0
%endif

%files
%{_libdir}/foo

%changelog
