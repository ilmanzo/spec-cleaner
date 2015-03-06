#
# spec file for package makeparams
#
# Copyright (c) 2013 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%build
make %{?jobs: -j%{jobs}}
make %{?jobs:-j %{jobs}}
make %{?jobs:-j%{jobs}}
make %{?jobs: -j%{jobs}}
make %{?jobs:-j %{jobs}}
make %{?jobs:-j%{jobs}}
make %{?jobs: -j%{jobs}}
make %{?jobs:-j %{jobs}}
make %{?jobs:-j%{jobs}}
make %{?jobs: -j%{jobs}}
make %{?jobs:-j %{jobs}}
make %{?jobs:-j%{jobs}}
make %{?jobs: -j%{jobs}}
make %{?jobs:-j %{jobs}}
make %{?jobs:-j%{jobs}}
make %{?jobs: -j%{jobs}}
make %{?jobs:-j %{jobs}}
make %{?jobs:-j%{jobs}}
make %{_smp_mflags}
make %{_smp_mflags}
make %{?_smp_mflags}
make %{_smp_mflags}
make %{_smp_mflags}
make %{?_smp_mflags}
make %{_smp_mflags}
make %{_smp_mflags}
make %{?_smp_mflags}
make check ||:
make && mv mtr xmtr
make %{?_smp_flags} VERBOSE=1

%install
%{makeinstall} install-etc
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install
make install DESTDIR=%{buildroot}
make install DESTDIR=%{buildroot}
make install DESTDIR=%{buildroot}
make install DESTDIR=%{buildroot}
make install DESTDIR=%{buildroot}
make install DESTDIR=%{buildroot}
make install DESTDIR=%{buildroot}
make install DESTDIR=%{buildroot}
make install DESTDIR=%{buildroot}
make install DESTDIR=%{buildroot}
make install DESTDIR=%{buildroot}
make install DESTDIR=%{buildroot}
%make_install
%make_install

