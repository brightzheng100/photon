Summary:        The Sysstat package contains utilities to monitor system performance and usage activity
Name:           sysstat
Version:        11.4.2
Release:        1%{?dist}
License:        GPLv2
URL:            http://sebastien.godard.pagesperso-orange.fr/
Group:          Development/Debuggers
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        http://perso.wanadoo.fr/sebastien.godard/%{name}-%{version}.tar.xz
%define sha1    sysstat=84ac7feba76049f201e203c7ce0cc750479a9d43
BuildRequires:  cronie
Requires:       cronie
%description
 The Sysstat package contains utilities to monitor system performance and usage activity. Sysstat contains the sar utility, common to many commercial Unixes, and tools you can schedule via cron to collect and historize performance and activity data.

%prep
%setup -q
%build

./configure --prefix=%{_prefix} \
            --enable-install-cron \
            --enable-copy-only \
            --disable-file-attr \
            sa_lib_dir=%{_libdir}/sa \
            --mandir=%{_mandir}
make %{?_smp_mflags}
%install
make install
mkdir -p %{buildroot}/usr/lib/systemd/system/
install -D -m 0644 %{_builddir}/%{name}-%{version}/sysstat.service %{buildroot}/usr/lib/systemd/system/
install -D -m 0644 %{_builddir}/%{name}-%{version}/cron/sysstat-summary.timer %{buildroot}/usr/lib/systemd/system/
install -D -m 0644 %{_builddir}/%{name}-%{version}/cron/sysstat-summary.service %{buildroot}/usr/lib/systemd/system/
install -D -m 0644 %{_builddir}/%{name}-%{version}/cron/sysstat-collect.timer %{buildroot}/usr/lib/systemd/system/
install -D -m 0644 %{_builddir}/%{name}-%{version}/cron/sysstat-collect.service %{buildroot}/usr/lib/systemd/system/

%find_lang %{name}
%clean
rm -rf %{buildroot}/*

%files -f %{name}.lang
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/sysconfig/*
%config(noreplace) %{_sysconfdir}/cron.d/*
%exclude %{_sysconfdir}/rc.d/init.d/sysstat
%{_bindir}/*
%{_libdir}/sa/*
%{_datadir}/doc/%{name}-%{version}/*
%{_mandir}/man*/*
%{_libdir}/systemd/system/*


%changelog
*   Thu Jan 05 2017 Xiaolin Li <xiaolinl@vmware.com> 11.4.2-1
-   Updated to version 11.4.2 and enable install cron.
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 11.2.0-3
-   GA - Bump release of all rpms
*   Wed May 4 2016 Divya Thaluru <dthaluru@vmware.com> 11.2.0-2
-   Adding systemd service file
*   Wed Jan 20 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 11.2.0-1
-   Update to 11.2.0-1.
*   Mon Nov 30 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 11.1.8-1
-   Initial build.  First version
